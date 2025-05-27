# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def numerical_letter_grade(grades):
    letter_grades = []
    
    for gpa in grades:
        # Check for invalid inputs
        if not isinstance(gpa, (int, float)):
            raise TypeError("All grades must be numeric")
        if gpa > 4.0 or gpa < 0.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        
        if gpa == 4.0:
            letter_grades.append("A+")
        elif gpa > 3.7:
            letter_grades.append("A")
        elif gpa > 3.3:
            letter_grades.append("A-")
        elif gpa > 3.0:
            letter_grades.append("B+")
        elif gpa > 2.7:
            letter_grades.append("B")
        elif gpa > 2.3:
            letter_grades.append("B-")
        elif gpa > 2.0:
            letter_grades.append("C+")
        elif gpa > 1.7:
            letter_grades.append("C")
        elif gpa > 1.3:
            letter_grades.append("C-")
        elif gpa > 1.0:
            letter_grades.append("D+")
        elif gpa > 0.7:
            letter_grades.append("D")
        elif gpa > 0.0:
            letter_grades.append("D-")
        else:
            letter_grades.append("E")
    
    return letter_grades