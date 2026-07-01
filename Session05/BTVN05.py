from fastapi import FastAPI, HTTPException

app = FastAPI()
products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "is_active": True},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "is_active": True},
    {"id": 3, "code": "SP003", "name": "Monitor", "price": 2500000, "is_active": False}
]

@app.patch("/products/{product_id}")
def update_status(product_id: int):
    for product in products:
        if product["id"] == product_id:
            if product["is_active"] == False:
                raise HTTPException(
                    status_code = 400,
                    detail = "Product already inactive"
                )
            product["is_active"] = False
            return {
                "message": "Ngừng kinh doanh sản phẩm thành công",
                "data": product
            }
    raise HTTPException(
        status_code = 404,
        detail = "Product not found"
    )