from sqlmodel import create_engine

def connect():
    #engine = create_engine("mysql+pymysql://username:password@host_of_data_base:port/name_data_base")
    engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/BGG_project", echo=False)
    return engine