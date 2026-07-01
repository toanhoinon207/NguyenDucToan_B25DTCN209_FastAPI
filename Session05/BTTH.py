from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()
products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000}
]

class Product(BaseModel):
    name: str = Field(min_length = 1)
    price: float = Field(gt = 0)

@app.post("/product", status_code = status.HTTP_201_CREATED)
def create_product(product: Product):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }
    products.append(new_product)
    return new_product

@app.get("/products")
def get_products():
    return products

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return products.remove(product)
    raise HTTPException(
        status_code = 404,
        detail = "Product not found"
    ) 