from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Double
from config.db import engine, meta_data

users = Table("users", meta_data,
              Column("id", Integer, primary_key=True),
              Column("name", String, nullable=False),
              Column("surname", String, nullable=False),
              Column("weight", Double, nullable=True)
              )

meta_data.create_all(engine)