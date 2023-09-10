from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Time
from config.db import engine, meta_data

tasks = Table("task", meta_data,
              Column("id", Integer, primary_key=True),
              Column("creationDate", DateTime, nullable=False),
              Column("code", String(100), nullable=False),
              Column("status", String(100), nullable=False),
              Column("taskType", String(10), nullable=False),
              Column("isFinish", Integer, nullable=False),
              Column("checkTime", Time, nullable=True),
              Column("finishDate", DateTime, nullable=True),
              Column("userId", Integer, nullable=False)
             )      

meta_data.create_all(engine)