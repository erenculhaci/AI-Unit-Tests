import os
import subprocess

# Constants
BASE_DIR = "After Update/Prompts 1-10"
OUTPUT_DIR = "coverage_output_after_modifications"
MODELS = {
    "gpt": "OpenAI-GPT",
    "claude": "Antrophic-Claude"
}

# Create base output directories
os.makedirs(f"{OUTPUT_DIR}/gpt", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/claude", exist_ok=True)

# Loop through prompts
for i in range(1, 11):
    prompt_name = f"Prompt-{i}"
    for model_key, model_folder in MODELS.items():
        prompt_path = os.path.join(BASE_DIR, prompt_name, model_folder)
        
        if not os.path.exists(prompt_path):
            print(f"Skipping missing directory: {prompt_path}")
            continue
        
        print(f"Running coverage for {model_key.upper()} - {prompt_name}...")

        # Clear previous coverage data
        subprocess.run(["coverage", "erase"], cwd=prompt_path)

        # Run tests
        subprocess.run(["coverage", "run", "tests.py"], cwd=prompt_path)

        # Generate HTML report
        output_path = os.path.abspath(f"{OUTPUT_DIR}/{model_key}/prompt_{i}")
        subprocess.run(["coverage", "html", "-d", output_path], cwd=prompt_path)

print("✅ All coverage reports generated in 'coverage_output' folder.")
