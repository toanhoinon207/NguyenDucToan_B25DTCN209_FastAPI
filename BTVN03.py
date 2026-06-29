# 1. INPUT: Danh sách students
# 2. OUTPUT: Hiển thị danh sách các sinh viên có trạng thái active, nếu không có hiển thị thông báo phù hợp
# 3. Điều kiện để xác định sách sắp hết hàng là status == "active"

from fastapi import FastAPI

app = FastAPI()
students = [
    {"id": 1, "name": "An", "status": "a"},
    {"id": 2, "name": "Binh", "status": "ina"},
    {"id": 3, "name": "Cuong", "status": "a"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students/active")
def get_active_students():
    active_students = []
    for student in students:
        if student["status"] == "active":
            active_students.append(student)
    if not active_students:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }
    return {
        "message": "Danh sách sinh viên đang học",
        "data": active_students
    }