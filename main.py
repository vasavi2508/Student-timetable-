
# Student Timetable Conflict Detection System

# Function to convert time into minutes
def convert_time(time):

    hours, minutes = time.split(":")

    return int(hours) * 60 + int(minutes)


# Function to check overlapping periods
def check_overlap(time1, time2):

    start1, end1 = time1.split("-")
    start2, end2 = time2.split("-")

    start1 = convert_time(start1)
    end1 = convert_time(end1)

    start2 = convert_time(start2)
    end2 = convert_time(end2)

    if start1 < end2 and start2 < end1:
        return True

    return False


# Function to validate time format
def validate_time(time):

    try:
        start, end = time.split("-")

        start = convert_time(start)
        end = convert_time(end)

        if start < 0 or end > 1440 or start >= end:
            return False

        return True

    except (ValueError, AttributeError):
        return False


# Existing course schedules
# Tuple format: (Course, Day, Time, Room)

existing_schedule = [
    ("MATH101", "Monday", "09:00-10:00", "A101"),
    ("PHY102", "Monday", "10:00-11:00", "B201"),
    ("ENG103", "Tuesday", "09:00-10:00", "C301"),
    ("CHE104", "Wednesday", "11:00-12:00", "A102")
]


# Unavailable room schedules
# Tuple format: (Room, Day, Unavailable Time)

unavailable_rooms = [
    ("A101", "Monday", "10:00-12:00"),
    ("B201", "Tuesday", "09:00-11:00"),
    ("C301", "Wednesday", "10:00-12:00")
]


# Proposed timetable
proposed_timetable = [
    ("CS105", "Monday", "09:30-10:30", "A101"),
    ("BIO106", "Tuesday", "11:00-12:00", "D101"),
    ("MAT107", "Wednesday", "11:30-12:30", "A102")
]


# Function to detect conflicts
def detect_conflicts(proposed):

    conflicts = []

    # Check every proposed course
    for i in range(len(proposed)):

        course1 = proposed[i]

        name1 = course1[0]
        day1 = course1[1]
        time1 = course1[2]
        room1 = course1[3]

        # Check against existing courses
        for existing in existing_schedule:

            name2 = existing[0]
            day2 = existing[1]
            time2 = existing[2]
            room2 = existing[3]

            if day1 == day2 and check_overlap(time1, time2):

                conflicts.append(
                    name1 + " overlaps with existing course " + name2
                )

                if room1 == room2:
                    conflicts.append(
                        "Room conflict: " + room1 +
                        " is already assigned to " + name2
                    )

        # Check unavailable rooms
        for room in unavailable_rooms:

            unavailable_room = room[0]
            unavailable_day = room[1]
            unavailable_time = room[2]

            if (room1 == unavailable_room and
                day1 == unavailable_day and
                check_overlap(time1, unavailable_time)):

                conflicts.append(
                    "Room " + room1 +
                    " is unavailable on " + day1
                )

        # Check conflicts within proposed timetable
        for j in range(i + 1, len(proposed)):

            course2 = proposed[j]

            name2 = course2[0]
            day2 = course2[1]
            time2 = course2[2]
            room2 = course2[3]

            if day1 == day2 and check_overlap(time1, time2):

                conflicts.append(
                    name1 + " overlaps with " + name2
                )

                if room1 == room2:
                    conflicts.append(
                        "Both courses are assigned to room " + room1
                    )

    return conflicts


# Main program
print("==========================================")
print(" STUDENT TIMETABLE CONFLICT DETECTION")
print("==========================================")

print("\nEXISTING COURSE SCHEDULE")

for course in existing_schedule:

    print(
        course[0], "|",
        course[1], "|",
        course[2], "|",
        course[3]
    )


print("\nPROPOSED TIMETABLE")

for course in proposed_timetable:

    print(
        course[0], "|",
        course[1], "|",
        course[2], "|",
        course[3]
    )


# Validate proposed time formats
invalid_records = []

for course in proposed_timetable:

    if course[1] not in [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]:
        invalid_records.append(
            course[0] + ": Invalid day."
        )

    if not validate_time(course[2]):
        invalid_records.append(
            course[0] + ": Invalid time period."
        )


# Check conflicts
if invalid_records:

    print("\nINVALID TIMETABLE DETAILS")

    for error in invalid_records:
        print("-", error)

else:

    conflicts = detect_conflicts(proposed_timetable)

    print("\n==========================================")
    print("          CONFLICT ANALYSIS")
    print("==========================================")

    if len(conflicts) == 0:

        print("No timetable conflicts detected.")
        print("Proposed timetable is VALID.")

    else:

        print("Timetable conflicts detected:")

        for conflict in conflicts:
            print("-", conflict)

        print("\nProposed timetable is INVALID.")


print("\n==========================================")
print("Timetable analysis completed.")
print("==========================================")
