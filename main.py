from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI(title="API của Dương", description="Những API của Dương")


products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
]


class ProductModel(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


@app.post("/products")
def add_product(product: ProductModel):
    newData = {
        "id": max(product["id"] for product in products) + 1,
        "name": product.name,
        "price": product.price,
    }

    products.append(newData)
    return {"message": "thêm thành công", "data": newData}


@app.get("/products")
def get_all_pro():
    if not products:
        return {"message": "Danh sách rỗng!"}

    return products


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"Message": "Xóa thành công"}
    return {"Message": "Không tìm thấy sản phẩm"}
