# GradeBook Analyzer
# Author: Aditya Choudhary
# Date: [2/11/25
# Course: Programming for Problem Solving using Python
# Assignment: Analyzing and Reporting Student Grades

def calculate_average(marks_dict):
    """Calculate and return the average of the marks."""
    if not marks_dict:
        return 0.0
    total = sum(marks_dict.values())
    return total / len(marks_dict)

def calculate_median(marks_dict):
    """Calculate and return the median of the marks."""
    if not marks_dict:
        return 0.0
    marks_list = sorted(marks_dict.values())
    n = len(marks_list)
    if n % 2 == 0:
        return (marks_list[n//2 - 1] + marks_list[n//2]) / 2
    else:
        return marks_list[n//2]

def find_max_score(marks_dict):
    """Find and return the max score and the student name."""
    if not marks_dict:
        return 0, "None"
    max_mark = max(marks_dict.values())
    for name, mark in marks_dict.items():
        if mark == max_mark:
            return max_mark, name

def find_min_score(marks_dict):
    """Find and return the min score and the student name."""
    if not marks_dict:
        return 0, "None"
    min_mark = min(marks_dict.values())
    for name, mark in marks_dict.items():
        if mark == min_mark:
            return min_mark, name

def assign_grades(marks_dict):
    """Assign grades based on marks and return a grades dictionary."""
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def grade_distribution(grades_dict):
    """Count and return the distribution of grades."""
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades_dict.values():
        distribution[grade] += 1
    return distribution

def main():
    print("Welcome to the GradeBook Analyzer!")
    print("This tool helps analyze student grades.\n")
    
    while True:
        # Task 2: Data Entry
        try:
            num_students = int(input("How many students are in the class? "))
            if num_students <= 0:
                print("Number of students must be positive. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        marks = {}
        for i in range(1, num_students + 1):
            name = input(f"Enter name for student {i}: ").strip()
            while True:
                try:
                    mark = float(input(f"Enter marks for {name}: "))
                    if 0 <= mark <= 100:
                        marks[name] = mark
                        break
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        # Task 3: Statistical Analysis
        avg = calculate_average(marks)
        median = calculate_median(marks)
        max_score, max_student = find_max_score(marks)
        min_score, min_student = find_min_score(marks)
        
        print("\nStatistical Analysis:")
        print(f"Average: {avg:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Max Score: {max_score} ({max_student})")
        print(f"Min Score: {min_score} ({min_student})")
        
        # Task 4: Grade Assignment and Distribution
        grades = assign_grades(marks)
        distribution = grade_distribution(grades)
        
        print("\nGrade Distribution:")
        for grade, count in distribution.items():
            print(f"{grade}: {count}")
        
        # Task 5: Pass/Fail Filter
        passed_students = [name for name, m in marks.items() if m >= 40]
        failed_students = [name for name, m in marks.items() if m < 40]
        
        print(f"\nPassed Students ({len(passed_students)}): {passed_students}")
        print(f"Failed Students ({len(failed_students)}): {failed_students}")
        
        # Task 6: Results Table
        print("\nResults Table:")
        print("Name".ljust(10) + "Marks".ljust(10) + "Grade")
        print("-" * 30)
        for name in marks:
            print(f"{name.ljust(10)}{str(marks[name]).ljust(10)}{grades[name]}")
        
        # Loop for re-run
        choice = input("\nDo you want to run the analysis again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
