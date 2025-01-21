from ..repository.user_repository import select_all, select_userb_by_email, create_user, delete_user
from ..model.user_model import User


def select_all_user_service():
	users = select_all()
	print(users)
	return users


def select_user_by_email_service(email:str):
	if email:
		return select_userb_by_email(email)
	else:
		return select_all()
	

def create_user_service(username: str, password: str,name: str):
	user = select_userb_by_email(username)
	if not user:
		user_save = User(username=username, password=password, name=name)
		return create_user(user_save)
	else:
		print("User already exists")
		raise BaseException("User already exists")
	

def delete_user_service(email:str):
	return delete_user(email=email)