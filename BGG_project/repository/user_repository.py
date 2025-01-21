from .connect_db import connect
from sqlmodel import Session, select
from ..model.user_model import User

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(User)
        return session.exec(query).all()
    

def select_userb_by_email(email: str):
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.username == email)
        return session.exec(query).one_or_none()
    

def create_user(User):
    pass