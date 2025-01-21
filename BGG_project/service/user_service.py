from ..repository.user_repository import select_all, select_userb_by_email, create_user, delete_user
from ..model.user_model import User


def select_all_user_service():
	users = select_all()
	print(users)
	return users


def select_user_by_email_service(email:str):
	if (len(email) != 0):
		return select_userb_by_email(email)
	else:
		return select_all()
	

def create_user_service(username: str, password: str,phone: str,name: str):
	user = select_userb_by_email(username)
	if(len(user) == 0):
		user_save = User(username=username, password=password, phone=phone, name=name)
		return create_user(user_save)
	else:
		print("El usuario ya existe")
		raise BaseException("El usuario ya existe")
	

def delete_user_service(email:str):
	return delete_user(email=email)