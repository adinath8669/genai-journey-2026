# 📝 Day 10 Notes – FastAPI Basics

## 1. What is FastAPI?

FastAPI is a modern, high-performance Python framework used to build REST APIs. It is easy to learn, supports asynchronous programming, and uses Python type hints for automatic validation.

---

## 2. Why is FastAPI Popular?

* Fast and high performance
* Easy to learn and use
* Automatic API documentation (Swagger UI)
* Built-in data validation with Pydantic
* Supports asynchronous programming
* Ideal for AI and Machine Learning backends

---

## 3. GET Request

A **GET** request is used to retrieve data from the server.

**Example:**

```python
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

---

## 4. POST Request

A **POST** request is used to send data to the server.

**Example:**

```python
@app.post("/ask")
def ask():
    return {"answer": "Response"}
```

---

## 5. Path Parameter

A **path parameter** is a value passed as part of the URL.

**Example:**

```python
@app.get("/user/{id}")
def get_user(id: int):
    return {"id": id}
```

Request:

```text
/user/10
```

---

## 6. Query Parameter

A **query parameter** is passed after the `?` in the URL.

**Example:**

```python
@app.get("/search")
def search(name: str):
    return {"name": name}
```

Request:

```text
/search?name=Adinath
```

---

## 7. Request Body

A **request body** contains data sent by the client, usually in JSON format with a POST request.

**Example:**

```json
{
  "question": "Explain AI"
}
```

---

## 8. Swagger UI

Swagger UI is an automatically generated web interface that lets you test and explore your API.

Open:

```text
http://127.0.0.1:8000/docs
```

Features:

* Test API endpoints
* View request and response formats
* Read API documentation

---

## 9. Uvicorn

**Uvicorn** is a lightweight ASGI server used to run FastAPI applications.

Run the server:

```bash
python -m uvicorn app:app --reload
```

* `app` → Python file (`app.py`)
* `app` → FastAPI application object
* `--reload` → Automatically reloads the server when code changes

---
