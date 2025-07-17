from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id: int
    title: str
    resolved: bool
    user_id: int

todos = []

@app.get("/todos")
def get_all():
    return todos

@app.post("/todos")
def create(todo: ToDo):
    todos.append(todo)
    return todo
