# Student-timetable-
# Student Timetable Conflict Detection System

## 1. Project Overview

The **Student Timetable Conflict Detection System** is a Python-based application designed to identify conflicts in student course schedules.

The system compares course schedules represented using strings and tuples, detects overlapping class periods, identifies unavailable classrooms, and validates proposed timetables.

It helps students and academic administrators prepare conflict-free timetables and avoid scheduling problems.

## 2. Objectives

- To represent course schedules using tuples and strings.
- To compare existing and proposed course schedules.
- To detect overlapping class periods.
- To identify classroom scheduling conflicts.
- To identify unavailable classrooms.
- To validate proposed timetables.
- To display all detected scheduling conflicts.
- To determine whether a proposed timetable is valid or invalid.

## 3. Assumptions

1. Every course has a unique course ID.
2. Each course has a specified day, time period, and classroom.
3. Time is represented using the 24-hour format.
4. Two classes cannot overlap in the same student's timetable.
5. Two courses cannot use the same room during overlapping periods.
6. Unavailable rooms cannot be assigned during blocked periods.
7. Existing schedules are stored using tuples.
8. Proposed schedules are compared against existing schedules and unavailable room records.
9. Classes ending exactly when another class starts are not considered overlapping.

## 4. Tuple Structure

Each course schedule is represented as:

```python
(course_name, day, time, room)
```

Example:

```python
("CS105", "Monday", "09:30-10:30", "A101")
```

| Element | Description |
|---|---|
| CS105 | Course ID |
| Monday | Day of the week |
| 09:30-10:30 | Class time |
| A101 | Classroom number |

### Unavailable Room Structure

```python
(room, day, unavailable_time)
```

Example:

```python
("A101", "Monday", "10:00-12:00")
```

## 5. Formulas and Conditions Used

### Time Conversion

Time is converted into minutes.

For example:

09:30 = (9 × 60) + 30 = 570 minutes.

### Overlapping Period Condition

Two class periods overlap when:

```text
Start1 < End2 AND Start2 < End1
```

### Timetable Validation

A proposed timetable is valid when:

- No course periods overlap.
- No classroom is assigned to multiple courses at overlapping times.
- No unavailable classroom is assigned.
- All proposed days and time periods are valid.

## 6. Algorithm

1. Start the program.
2. Define the existing course schedules.
3. Define unavailable classroom schedules.
4. Define the proposed timetable.
5. Display the existing timetable.
6. Display the proposed timetable.
7. Validate the proposed days and time periods.
8. Convert time strings into minutes.
9. Compare proposed courses with existing courses.
10. Check for overlapping class periods.
11. Check whether the same classroom is assigned during overlapping periods.
12. Compare proposed classrooms with unavailable room schedules.
13. Compare courses within the proposed timetable.
14. Store all detected conflicts in a list.
15. If no conflicts exist, display VALID TIMETABLE.
16. Otherwise, display INVALID TIMETABLE and the conflict details.
17. Display the completion message.
18. Stop the program.

## 7. Pseudocode

```text
START

DEFINE existing course schedules
DEFINE unavailable room schedules
DEFINE proposed timetable

FUNCTION convert_time(time):

    CONVERT hours into minutes
    CONVERT minutes into total minutes

    RETURN total minutes

FUNCTION check_overlap(time1, time2):

    EXTRACT start and end times

    CONVERT times into minutes

    IF start1 < end2 AND start2 < end1:
        RETURN TRUE

    ELSE:
        RETURN FALSE

FUNCTION detect_conflicts(proposed):

    CREATE empty conflict list

    FOR each proposed course:

        COMPARE with existing courses

        IF same day AND overlapping time:

            ADD course conflict

            IF same room:
                ADD room conflict

        CHECK unavailable room schedules

        IF same room AND same day AND overlapping time:
            ADD room unavailable conflict

        COMPARE with other proposed courses

        IF same day AND overlapping time:
            ADD timetable conflict

    RETURN conflict list

DISPLAY existing timetable
DISPLAY proposed timetable

VALIDATE proposed days and time periods

IF invalid records exist:

    DISPLAY invalid timetable details

ELSE:

    CALL detect_conflicts()

    IF conflict list is empty:

        DISPLAY VALID TIMETABLE

    ELSE:

        DISPLAY INVALID TIMETABLE
        DISPLAY all conflicts

DISPLAY completion message

STOP
```

## 8. Test Cases

| Test Case | Existing Schedule | Proposed Schedule | Expected Result |
|---|---|---|---|
| 1 | Monday 09:00–10:00 | Monday 09:30–10:30 | Time conflict |
| 2 | Monday 09:00–10:00, Room A101 | Monday 09:30–10:30, Room A101 | Time and room conflict |
| 3 | Room A101 unavailable 10:00–12:00 | Monday 10:30–11:30, Room A101 | Unavailable room |
| 4 | Monday 09:00–10:00 | Monday 10:00–11:00 | No overlap |
| 5 | Tuesday 09:00–10:00 | Wednesday 09:00–10:00 | No time conflict |

### Sample Test Case Explanation

**Test Case 1: Overlapping Classes**

- Existing class: 09:00–10:00.
- Proposed class: 09:30–10:30.
- Overlapping period: 09:30–10:00.
- Result: Conflict detected.

**Test Case 2: Room Conflict**

- Existing class uses room A101.
- Proposed class also uses room A101.
- Both classes overlap.
- Result: Room conflict detected.

**Test Case 3: Unavailable Classroom**

- Room A101 is unavailable from 10:00 to 12:00.
- Proposed class is scheduled from 10:30 to 11:30.
- Result: Unavailable classroom detected.

**Test Case 4: Consecutive Classes**

- Existing class: 09:00–10:00.
- Proposed class: 10:00–11:00.
- Result: No overlap because the first class ends when the next begins.

## 9. Sample Output

```text
==========================================
 STUDENT TIMETABLE CONFLICT DETECTION
==========================================

CONFLICT ANALYSIS

Timetable conflicts detected:

- CS105 overlaps with existing course MATH101
- Room conflict: A101 is already assigned to MATH101
- CS105 overlaps with existing course PHY102
- Room A101 is unavailable on Monday
- MAT107 overlaps with existing course CHE104
- Room conflict: A102 is already assigned to CHE104

Proposed timetable is INVALID.

==========================================
Timetable analysis completed.
==========================================
```

## 10. Python Concepts Used

- Variables and data types
- Input and output statements
- Tuples
- Lists
- String operations
- String methods
- Conditional statements (if and else)
- For loops
- Functions
- Function arguments and return values
- Arithmetic operators
- Logical operators
- Exception handling

## 11. Conclusion

The Student Timetable Conflict Detection System successfully compares existing and proposed course schedules using Python.

It identifies overlapping class periods, classroom conflicts, and unavailable rooms. It also validates the proposed timetable and displays the reasons for scheduling conflicts.

This project demonstrates the practical application of Python concepts such as tuples, strings, lists, loops, functions, and conditional statements in solving real-world academic scheduling problems.

## 12. Project Structure

```text
Student-Timetable-Conflict/
│
├── timetable_conflict.py
├── README.md
│
└── screenshots/
    └── output.png
```

## 13. Execution Instructions

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `timetable_conflict.py`.
4. Run the program using:

```bash
python timetable_conflict.py
```

5. View the existing and proposed course schedules.
6. Check the detected timetable conflicts.
7. Modify the sample tuples to test different schedules.
8. Capture the actual program output screenshot.
9. Upload the Python file, README, and screenshot to GitHub.

## 14. Author Details

- **Name:** v.v.s.s.gayathri
- **Roll Number:** N26V01A0388
- **Branch:** CSE
- **Section:** Section-5
- **Subject:** Python Programming
- **Project:** Student timetable 
