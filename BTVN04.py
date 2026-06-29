# 1. INPUT: Danh sách books
# 2. OUTPUT: Hiển thị sách sắp hết hàng, nếu không có thì hiển thị thông báo phù hợp
# 3. Điều kiện để xác định sách sắp hết hàng là quantity <= 5
# GP1: Dùng vòng lặp for
# GP2: Dùng List Comprehension
# Tiêu chí	            |  Vòng lặp for	 |  List Comprehension
# Độ dễ hiểu	        |      Cao       |      Trung bình
# Độ ngắn gọn	        |   Trung bình	 |         Cao
# Dễ xử lý bẫy dữ liệu	|      Cao	     |      Trung bình
# Dễ bảo trì	        |      Cao	     |         Khá
# Chọn vòng lặp for vì nó dễ đọc, dễ thêm các điều kiện kiểm tra, dễ bảo trì khi chương trình lớn hơn.

from fastapi import FastAPI

app = FastAPI()
books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20}
]

@app.get("/books/low-stock")
def get_low_stock_books():
    low_stock = []
    for book in books:
        if "quantity" not in book:
            continue
        if book["quantity"] < 0:
            continue
        if book["quantity"] < 5:
            books.append(book)
    if not low_stock:
        return {
            "message": "Không có sách nào sắp hết hàng",
            "data": []
        }
    return {
        "message": "Danh sách sách sắp hết hàng",
        "data": low_stock
    }
    