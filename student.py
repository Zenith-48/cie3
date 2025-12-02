import pytest
def student_details(id,name,course,year):
    result = (
        f"Student ID: {id}\n"
        f"Student name: {name}\n"
        f"Course: {course}\n"
        f"Year: {year}\n"
    )
    return result 
if __name__=="__main__":
    id="E101"
    name="shalina"
    course="BCA"
    year=2026
    print(student_details(id,name,course,year))
