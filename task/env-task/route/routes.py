from fastapi import APIRouter, Response
from schema.task_schema import taskSchema
from schema.users_schema import usersSchema
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from config.db import engine
from model.taks import tasks
from model.users import users
from typing import List

task = APIRouter()

@task.get("/")
def root():
    return {"message": "Si"}
    
@task.post("/api/task", status_code=HTTP_201_CREATED)
def create_task(data_task: taskSchema):
    with engine.connect() as conn:
        new_task = data_task.dict()
        conn.execute(tasks.insert().values(new_task))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    
@task.get("/api/task", response_model=List[taskSchema])
def get_task():
    with engine.connect() as conn:
        return conn.execute(tasks.select()).fetchall()
    
@task.get("/api/task/{task_id}", response_model= taskSchema)
def get_user(task_id: str):
    with engine.connect() as conn:
        return conn.execute(tasks.select().where(tasks.c.id == task_id)).first()
    
@task.put("/api/task/{task_id}", response_model=taskSchema)
def update_task(task_update: taskSchema, task_id: str):
    with engine.connect() as conn:
        conn.execute(tasks.update().values(status=task_update.status, isFinish=task_update.isFinish, checkTime=task_update.checkTime, finishDate=task_update.finishDate, userId=task_update.userId).where(tasks.c.id==task_id))
        conn.commit()
        return conn.execute(tasks.select().where(tasks.c.id == task_id)).first()
    
@task.delete("/api/task/{task_id}", status_code=HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    with engine.connect() as conn:
        conn.execute(tasks.delete().where(tasks.c.id == task_id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
    
@task.get("/api/user/{user_id}",response_model=List[usersSchema])
def get_user(user_id: str):
    with engine.connect() as conn:
        return conn.execute(users.select().where(users.c.id==user_id))

@task.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: usersSchema):
    with engine.connect() as conn:
        conn.execute(users.insert().values(data_user.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    