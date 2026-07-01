from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "stock": 10},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "stock": 5}
]

class ProductUpdate(BaseModel):
    code: str
    name: str = Field(min_length = 1)
    price: float = Field(gt = 0)
    stock: int = Field(ge = 0)

@app.put("/product/{product_id}")
def update_product(product_id: int, update_product: ProductUpdate):
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    if product is None:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )
    for p in products:
        if p["code"] == update_product.code and p["id"] != product_id:
            raise HTTPException(
                status_code = 400,
                detail = "Product code already exists"
            )
    product["code"] = update_product.code
    product["name"] = update_product.name
    product["price"] = update_product.price
    product["stock"] = update_product.stock
    return product