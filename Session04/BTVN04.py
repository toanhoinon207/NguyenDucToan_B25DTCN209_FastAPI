from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app =FastAPI()
students = [
    {
        "id": 1,
        "full_name": "Nguyen Van B",
        "email": "existing@gmail.com",
        "age": 21,
        "course": "python",
        "phone": "0988888888"
    }
]

class Student(BaseModel):
    full_name: str = Field(..., min_length = 3)
    email: EmailStr
    age: int
    course: str
    phone: str

@app.post("/students")
def create_student(student: Student):
    for s in students:
        if s["email"] == student.email:
            raise HTTPException(
                status_code = 400,
                detail = "Email đã tồn tại trong hệ thống"
            )
    new_student = {
        "id": len(students) + 1,
        "full_name": student.full_name,
        "email": student.email,
        "age": student.age,
        "course": student.course,
        "phone": student.phone
    }
    students.append(new_student)
    return new_student