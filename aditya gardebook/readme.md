

## Overview

Welcome to the **GradeBook Analyzer**, a Python-based application designed for educators to efficiently analyze student performance. This tool automates the process of calculating statistics, assigning grades, and generating reports from manually entered student data.

## Course Information

- **Course**: Programming for Problem Solving using Python
- **Assignment Title**: Analyzing and Reporting Student Grades
- **Type**: Individual Mini Project
- **Duration**: 3-4 hours
- **Weightage**: 15% of course grade (5 marks)

## Real-World Context

In educational settings, teachers frequently need to quickly assess class performance after exams. The GradeBook Analyzer replaces manual calculations and spreadsheet work with a streamlined Python script that handles data input, statistical computations, grade assignments, and formatted reporting.

## Key Learning Outcomes

Upon completion, participants will demonstrate proficiency in:
- Data handling with Python dictionaries and lists.
- Implementation of statistical algorithms (average, median, min, max).
- Conditional logic for grade assignment.
- List comprehensions for data filtering.
- Modular programming with functions and iterative structures.
- Output formatting using f-strings.

## Core Functionality

### 1. Data Input
- Prompt user for the number of students.
- Collect names and marks (0-100) for each student.
- Store data in a dictionary for easy access.

### 2. Statistical Computations
- Compute average, median, maximum, and minimum scores.
- Display results with associated student names where applicable.

### 3. Grade Assignment
- Assign letter grades based on standard thresholds:
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: Below 60
- Generate a grade distribution summary.

### 4. Pass/Fail Analysis
- Categorize students into passed (marks >= 40) and failed lists.
- Utilize list comprehensions for efficient filtering.

### 5. Report Generation
- Produce a tabular display of student names, marks, and grades.
- Include counts for passed/failed students.

### 6. Interactive Loop
- Allow users to rerun analyses or exit the program.

## Technical Requirements

- **Python Version**: 3.x (recommended 3.8 or higher)
- **Dependencies**: None (built-in modules only)
- **Execution**: Run via command line: `python gradebook.py`

## Installation Guide

1. Download or clone the project repository.
2. Navigate to the `gradebook_analyzer/` directory.
3. Ensure Python is installed and accessible.
4. Launch the script to begin.

## User Guide

1. **Launch**: Execute `python gradebook.py`.
2. **Input Data**:
   - Specify student count.
   - Enter each student's name and score.
3. **View Results**:
   - Review statistical summaries.
   - Check grade distributions.
   - Examine pass/fail lists.
   - Inspect the results table.
4. **Repeat or Exit**: Choose to analyze another set or quit.

### Sample Interaction

```
Welcome to the GradeBook Analyzer!
This tool helps analyze student grades.

How many students are in the class? 3
Enter name for student 1: Alice
Enter marks for Alice: 78
Enter name for student 2: Bob
Enter marks for Bob: 92
Enter name for student 3: Carol
Enter marks for Carol: 56

Statistical Analysis:
Average: 75.33
Median: 78.0
Max Score: 92 (Bob)
Min Score: 56 (Carol)

Grade Distribution:
A: 1
B: 0
C: 1
D: 0
F: 1

Passed Students (2): ['Alice', 'Bob']
Failed Students (1): ['Carol']

Results Table:
Name       Marks     Grade
--------------------------
Aditya       78         C
aliya         92         A
rohan       56         F

Do you want to run the analysis again? (y/n): n
Goodbye!
```

## Project Structure

- `gradebook.py`: The primary script implementing all features.
- `README.md`: Comprehensive documentation (this file).

## Testing Recommendations

- Conduct tests with varying student counts (e.g., 1, 5, 10).
- Test boundary conditions: perfect scores, failing marks, identical scores.
- Validate input handling for non-numeric entries and out-of-range values.

## Author Details

- **Name**: Aditya choudhary
- **Date**: 6/11/25
- **Affiliation**: Programming for Problem Solving using Python Course

## Submission Guidelines

- Ensure `gradebook.py` includes all required tasks.
- Code should be well-structured, modular, and include comments.
- Test thoroughly before submission.
- Marks Allocation: 5 points total.