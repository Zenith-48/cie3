from student import student_details
def test_student_details():
    expected_output = (
        "Student ID: E101\n"
        "Student name: shalina\n"
        "Course: BCA\n"
        "Year: 2026\n"
    )
    assert student_details("E101","shalina","BCA","2026") == expected_output
