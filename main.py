from fastapi import FastAPI

app = FastAPI(title="API của Dương", description="Những API của Dương")


books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": True
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": False
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": True
    }
]

@app.get("/health")
def get_health():
  return{"message": "Library API is running"}
@app.get("/books")
def get_book():
  return

@app.get("/books/available")
def get_books_available():
    books_available = []
    for s in books:
       if s["is_available"] == True:
          books_available.append(s)
    return books_available
@app.get("/books/borrowed")
def get_books_unavailable():
    books_unavailable = []
    for s in books:
       if s["is_available"] == False:
          books_unavailable.append(s)
    return books_unavailable
