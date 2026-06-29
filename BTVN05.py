from fastapi import FastAPI

app = FastAPI()
@app.get("/books")
def get_books():
    return {
        "message": "Danh sách sách"
    }

@app.get("/books/detail")
def get_course_detail():
    return {
        "message": "Chi tiết sách"
    }

@app.post("/books")
def create_book():
    return {
        "message": "Thêm sách thành công"
    }

@app.put("/books/update")
def update_book():
    return {
        "message": "Cập nhật sách thành công"
    }

@app.delete("/books/delete")
def delete_book():
    return {
        "message": "Xóa sách thành công"
    }

@app.get("/books/statistics")
def book_statistic():
    return {
        "message": "Xem thống kê sách"
    }

@app.get("/books/newest")
def newest_books():
    return {
        "message": "Danh sách sách mới nhất"
    }

@app.get("/books/popular")
def popular_books():
    return {
        "message": "Danh sách sách phổ biến"
    }

