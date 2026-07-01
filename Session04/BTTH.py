from fastapi import FastAPI
from typing import Optional

app = FastAPI()
courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online"
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline"
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online"
    }
]

@app.get("/course")
def get_courses():
    return {
        "message": "Lấy danh sách khóa học thành công",
        "data": courses
    }
        
@app.get("/courses/search")
def search_course(
    mode: Optional[str] = None,
    category: Optional[str] = None
):
    result = []
    for course in courses:
        if mode is not None and course["mode"] != mode:
            continue
        if category is not None and course["category"] != category:
            continue
        result.append(course)
    return result

@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return {
                "message": "Tìm thấy khóa học",
                "data": course
            }
    return {
        "message": "Không tìm thấy khóa học"
    }