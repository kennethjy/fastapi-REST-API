import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import mysql.connector
import datetime

connect = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1223334444',
    database='todo-db'
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

students = {
    "1": {'a' : 'b'},
    "2": {'a' : 'c'}
}

def generateID():
    newid = ""
    for _ in range(20):
        newid += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[random.randint(0, 61)]
    return newid

@app.get("/")
def index():
    return {'a':'b'}

@app.get("/gettodoforuser/{uid}")
def gettodoforuser(uid):
    db = connect.cursor()
    db.execute("SELECT * FROM tasks "
               "WHERE tasks.uid = %s;",
               (uid,))

    return [{"id": i[0],
             "description": i[1],
             "date": i[2],
             "isChecked": i[3]}
            for i in db.fetchall()]

@app.get("/gettodo/{id}")
def gettodo(id):
    db = connect.cursor()
    db.execute("SELECT * FROM tasks "
               "WHERE tasks.taskid = %s;",
               (id,))
    item = db.fetchone()
    if item is not None:
        return {"id": item[0],
                "description": item[1],
                "date": item[2],
                "isChecked": item[3]}
    return None

@app.post("/newtodo/{uid}")
def newTodo(uid):
    db = connect.cursor()
    id = generateID()
    db.execute("INSERT INTO tasks (taskid, description, date, isChecked, uid) "
               "VALUES (%s, %s, %s, %s, %s);",
               (id, "New Task", str(datetime.date.today()),
                0, uid))
    connect.commit()
    return id


@app.delete("/deletetodo/{id}")
def deleteTodo(id):
    db = connect.cursor()
    db.execute("DELETE FROM tasks "
               "WHERE taskid = %s;",
               (id,))
    connect.commit()

@app.put("/checktodo/{id}")
def checkTodo(id):
    db = connect.cursor()
    db.execute("UPDATE tasks SET isChecked = !isChecked WHERE taskid = %s",
               (id,))
    connect.commit()

@app.put("/changedesc/{id}/{desc}")
def changedesc(id, desc):
    db = connect.cursor()
    db.execute("UPDATE tasks SET description = %s WHERE taskid = %s",
               (desc, id))
    connect.commit()