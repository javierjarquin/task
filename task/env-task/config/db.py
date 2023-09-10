from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:javier1606jarquin@localhost:3306/task")

meta_data = MetaData()