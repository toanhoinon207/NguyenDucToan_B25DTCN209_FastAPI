# 1. INPUT: Danh sách products, 2 Query Parameters (keyword: str, max_price: float)
# 2. OUTPUT: API trả về danh sách sản phẩm thỏa mãn điều kiện tìm kiếm.
# Nếu không truyền tham số nào, trả về toàn bộ danh sách sản phẩm.
# Nếu truyền keyword, trả về các sản phẩm có tên chứa từ khóa (không phân biệt chữ hoa, chữ thường).
# Nếu truyền max_price, trả về các sản phẩm có giá nhỏ hơn hoặc bằng max_price.
# Nếu truyền cả keyword và max_price, trả về các sản phẩm thỏa mãn cả hai điều kiện.
# Nếu max_price < 0, trả về lỗi
# 3. Sử dụng Query Parameters keyword và max_price.
# Kiểm tra tính hợp lệ của max_price.
# Nếu max_price < 0 thì trả về lỗi 400 Bad Request.
# Duyệt qua danh sách sản phẩm bằng vòng lặp for.
# Kiểm tra từng điều kiện:
# Nếu có keyword, so sánh tên sản phẩm bằng lower() để không phân biệt chữ hoa, chữ thường.
# Nếu có max_price, chỉ lấy sản phẩm có giá nhỏ hơn hoặc bằng giá trị này.
# Thêm các sản phẩm thỏa mãn điều kiện vào danh sách kết quả và trả về.
# 4. Khởi tạo ứng dụng FastAPI.
# Khai báo danh sách products.
# Tạo endpoint GET /products.
# Nhận hai Query Parameter keyword và max_price.
# Kiểm tra max_price:
# Nếu nhỏ hơn 0, trả về lỗi 400.
# Tạo danh sách kết quả rỗng.
# Duyệt từng sản phẩm trong danh sách.
# Nếu có keyword, kiểm tra tên sản phẩm có chứa từ khóa hay không.
# Nếu có max_price, kiểm tra giá sản phẩm có nhỏ hơn hoặc bằng giá trị truyền vào hay không.
# Thêm các sản phẩm thỏa mãn điều kiện vào danh sách kết quả.
# Trả về danh sách sản phẩm phù hợp.

from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()
products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products")
def get_products(
    keyword: Optional[str] = None,
    max_price: Optional[float] = None
):
    if max_price is not None and max_price < 0:
        raise HTTPException(
            status_code = 400,
            detail = "max_price không được âm"
        )
    result = []
    for product in products:
        if keyword is not None:
            if keyword.lower() not in product["name"].lower():
                continue
        if max_price is not None:
            if product["price"] > max_price:
                continue
        result.append(product)
    return result