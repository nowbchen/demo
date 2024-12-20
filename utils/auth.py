from app.user import User
from sqlalchemy.orm import Session
from database.db import authenticate_user as db_authenticate

def authenticate_user(username: str, password: str):
    """验证用户凭据"""
    return db_authenticate(username, password)

def get_user_info(db: Session, username: str):
    """获取用户信息"""
    return db.query(User).filter(User.username == username).first()