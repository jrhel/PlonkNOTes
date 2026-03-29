from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from dao import db_connection_handler
from dao import userDAO


def initialize_logic():
    db_connection_handler.verify_database()

def create_user(username: str, password: str):
    password_hash = generate_password_hash(password)
    userDAO.create_user(username, password_hash)

def verify_login(username: str, password: str):
    password_hash = userDAO.get_user(username)["password_hash"]
    if check_password_hash(password_hash, password):
        return True
    else:
        return False