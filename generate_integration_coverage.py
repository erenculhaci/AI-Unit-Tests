import os
import sys
import subprocess
import shutil
from pathlib import Path
import json
import datetime


class IntegrationTestRunner:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.integration_tests_dir = self.base_dir / "Integration Tests"
        self.output_dir = self.base_dir / "coverage_output_integration_tests"
        self.code_file = self.integration_tests_dir / "combined_modified_code.py" # change this file if you want tot ests combined_unmodified_code.py
        self.handwritten_tests = self.integration_tests_dir / "handwritten_tests.py"
        self.llm_tests = self.integration_tests_dir / "tests_by_llm.py"
        
    def validate_setup(self):
        """Validate that all required files exist."""
        print("Validating test setup...")
        
        missing_files = []
        for file_path in [self.code_file, self.handwritten_tests, self.llm_tests]:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        if missing_files:
            print("Missing required files:")
            for file in missing_files:
                print(f"   - {file}")
            return False
        
        print("All required files found")
        return True
    
    def setup_output_directory(self):
        """Create and clean the output directory."""
        print(f"Setting up output directory: {self.output_dir}")
        
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        
        self.output_dir.mkdir(exist_ok=True)
        (self.output_dir / "reports").mkdir(exist_ok=True)
        (self.output_dir / "logs").mkdir(exist_ok=True)
        
        print("Output directory ready")
    
    def install_coverage_if_needed(self):
        """Install coverage.py if not already installed."""
        try:
            import coverage
            print("Coverage.py already available")
        except ImportError:
            print("Installing coverage.py...")
            subprocess.run([sys.executable, "-m", "pip", "install", "coverage"], 
                         check=True, capture_output=True)
            print("Coverage.py installed")
    
    def run_tests_with_coverage(self, test_file, test_name):
        """Run a test file with coverage analysis."""
        print(f"Running {test_name}...")
        
        coverage_file = self.output_dir / f".coverage_{test_name.lower().replace(' ', '_')}"
        log_file = self.output_dir / "logs" / f"{test_name.lower().replace(' ', '_')}.log"
        
        # Prepare environment
        env = os.environ.copy()
        env['COVERAGE_FILE'] = str(coverage_file)
        env['PYTHONPATH'] = str(self.integration_tests_dir) + os.pathsep + env.get('PYTHONPATH', '')
        
        # Run tests with coverage
        cmd = [
            sys.executable, "-m", "coverage", "run",
            "--source", str(self.integration_tests_dir),
            "--omit", f"*{os.sep}test*",
            str(test_file)
        ]
        
        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.integration_tests_dir),
                env=env,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            # Write logs
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write(f"Command: {' '.join(cmd)}\n")
                f.write(f"Return code: {result.returncode}\n")
                f.write(f"STDOUT:\n{result.stdout}\n")
                f.write(f"STDERR:\n{result.stderr}\n")
            
            if result.returncode == 0:
                print(f"{test_name} completed successfully")
            else:
                print(f"{test_name} completed with warnings/errors (return code: {result.returncode})")
            
            return coverage_file, result.returncode == 0
            
        except subprocess.TimeoutExpired:
            print(f"{test_name} timed out after 5 minutes")
            return coverage_file, False
        except Exception as e:
            print(f"Error running {test_name}: {str(e)}")
            return coverage_file, False
    
    def generate_coverage_reports(self, coverage_files, test_names):
        """Generate coverage reports from all test runs."""
        print("Generating coverage reports...")
        
        for coverage_file, test_name in zip(coverage_files, test_names):
            if not coverage_file.exists():
                print(f"Coverage file not found for {test_name}")
                continue
            
            report_name = test_name.lower().replace(' ', '_')
            
            # Set environment for this coverage file
            env = os.environ.copy()
            env['COVERAGE_FILE'] = str(coverage_file)
            
            # Generate HTML report
            html_dir = self.output_dir / "reports" / f"{report_name}_html"
            try:
                subprocess.run([
                    sys.executable, "-m", "coverage", "html",
                    "-d", str(html_dir)
                ], env=env, check=True, capture_output=True)
                print(f"HTML report generated for {test_name}: {html_dir}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to generate HTML report for {test_name}")
            
            # Generate text report
            try:
                result = subprocess.run([
                    sys.executable, "-m", "coverage", "report"
                ], env=env, capture_output=True, text=True, check=True)
                
                report_file = self.output_dir / "reports" / f"{report_name}_report.txt"
                with open(report_file, 'w', encoding='utf-8') as f:
                    f.write(result.stdout)
                print(f"Text report generated for {test_name}: {report_file}")
            except subprocess.CalledProcessError:
                print(f"Failed to generate text report for {test_name}")
    
    def combine_coverage_reports(self, coverage_files):
        """Combine all coverage data into a single report."""
        print("Combining coverage reports...")
        
        combined_coverage = self.output_dir / ".coverage_combined"
        env = os.environ.copy()
        env['COVERAGE_FILE'] = str(combined_coverage)
        
        # Combine coverage files
        existing_files = [f for f in coverage_files if f.exists()]
        if not existing_files:
            print("No coverage files to combine")
            return
        
        try:
            cmd = [sys.executable, "-m", "coverage", "combine"] + [str(f) for f in existing_files]
            subprocess.run(cmd, env=env, check=True, capture_output=True)
            
            # Generate combined HTML report
            combined_html = self.output_dir / "reports" / "combined_coverage_html"
            subprocess.run([
                sys.executable, "-m", "coverage", "html",
                "-d", str(combined_html)
            ], env=env, check=True, capture_output=True)
            
            # Generate combined text report
            result = subprocess.run([
                sys.executable, "-m", "coverage", "report"
            ], env=env, capture_output=True, text=True, check=True)
            
            combined_report = self.output_dir / "reports" / "combined_coverage_report.txt"
            with open(combined_report, 'w', encoding='utf-8') as f:
                f.write("COMBINED COVERAGE REPORT\n")
                f.write("=" * 50 + "\n\n")
                f.write(result.stdout)
            
            print(f"Combined coverage report generated: {combined_html}")
            print(f"Combined text report generated: {combined_report}")
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Failed to combine coverage reports: {e}")
    
    def run(self):
        """Main execution method."""
        print("Starting Integration Test Runner")
        print("=" * 50)
        
        # Validate setup
        if not self.validate_setup():
            return False
        
        # Setup environment
        self.setup_output_directory()
        self.install_coverage_if_needed()
        
        # Run tests
        test_files = [self.handwritten_tests, self.llm_tests]
        test_names = ["Handwritten Tests", "LLM Tests"]
        coverage_files = []
        results = {}
        
        for test_file, test_name in zip(test_files, test_names):
            coverage_file, success = self.run_tests_with_coverage(test_file, test_name)
            coverage_files.append(coverage_file)
            results[test_name] = success
        
        # Generate reports
        self.generate_coverage_reports(coverage_files, test_names)
        self.combine_coverage_reports(coverage_files)
                
        print("\n" + "=" * 50)
        print("Integration test execution completed!")
        print(f"Results available in: {self.output_dir}")
        print(f"Open {self.output_dir / 'reports' / 'combined_coverage_html' / 'index.html'} for coverage visualization")
        
        return all(results.values())


def main():
    """Main entry point."""
    runner = IntegrationTestRunner()
    success = runner.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()