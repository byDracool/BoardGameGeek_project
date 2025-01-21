from sqlmodel import create_engine

def connect():
    engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/BGG_project", echo=False)
    return engine