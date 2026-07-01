from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, field_validator

app = FastAPI()

class StudentRegister(BaseModel):
    full_name: str = Field(min_length = 3)
    email: EmailStr
    age: int = Field(ge = 15, le = 60)
    phone: str = Field(min_length = 10, max_length = 11)
    course: str
    note: str | None = Field(default = None, max_length = 200)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if not value.isdigit():
            raise ValueError("Phone chỉ được chứa chữ số")
        return value
    
@app.post("/students/register")
def register_student(student: StudentRegister):
    return {
        "message": "Đăng ký học viên thành công",
        "data": {
            "full_name": student.full_name,
            "email": student.email,
            "age": student.age,
            "phone": student.phone,
            "course": student.course,
            "note": student.note if student.note else None
        }
    }