# 1. INPUT: nhận dữ liệu từ Request Body dạng JSON, gồm {"student_id": 1, "course_id": 2}
# 2. OUTPUT (thành công): Trả về HTTP Status Code 201 Created, trả về thông tin phiếu đăng ký vừa được tạo.
# 3. OUTPUT (Thất bại): API trả về mã lỗi phù hợp kèm thông báo rõ ràng: Học viên không tồn tại, khóa học không tồn tại, học viên đã đăng ký khóa học, khóa học đã đủ sĩ số

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()
students = [
    {"id": 1, "name": "Nguyen Van A"},
    {"id": 2, "name": "Tran Thi B"},
    {"id": 3, "name": "Le Van C"}
]

courses = [
    {"id": 1, "name": "FastAPI Basic", "capacity": 2},
    {"id": 2, "name": "Python OOP", "capacity": 2}
]

registrations = [
    {"id": 1, "student_id": 1, "course_id": 1},
    {"id": 2, "student_id": 2, "course_id": 1}
]

class Registration(BaseModel):
    student_id: int
    course_id: int

@app.post("/registrations", status_code=status.HTTP_201_CREATED)
def register_course(register: Registration):
    is_exists = False
    for student in students:
        if student["id"] == register.student_id:
            is_exists = True
            break
    if not is_exists:
        raise HTTPException(
            status_code = 404,
            detail = "Student not found"
        )
    course = None
    for c in courses:
        if c["id"] == register.course_id:
            course = c
            break
    if course is None:
        raise HTTPException(
            status_code = 404,
            detail = "Course not found"
        )
    for registration in registrations:
        if registration["student_id"] == register.student_id and registration["course_id"] == register.course_id:
            raise HTTPException(
                status_code = 400,
                detail = "Student already registered this course"
            )
    total_student = 0
    for registration in registrations:
        if registration["course_id"] == register.course_id:
            total_student += 1
    if total_student >= course["capacity"]:
        raise HTTPException(
            status_code = 400,
            detail = "Course is full"
        )
    new_registration = {
        "id": len(registrations) + 1,
        "student_id": register.student_id,
        "course_id": register.course_id
    }
    registrations.append(new_registration)
    return new_registration