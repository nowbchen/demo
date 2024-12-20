from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
import bcrypt

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    level = Column(Integer, default=1)  # 用户层级
    parent_id = Column(Integer, ForeignKey('users.id'), nullable=True)  # 上级用户ID
    
    # 建立与上级用户的关系
    # 建立用户之间的层级关系:
    # - parent: 通过relationship定义与上级用户(parent)的关系,remote_side指定关联的是自身的id字段
    # - backref="subordinates": 反向定义下级用户集合,可通过parent.subordinates访问所有下属
    # 例如:
    # user1.parent 获取user1的上级用户
    # user1.subordinates 获取user1的所有下属用户列表
    parent = relationship("User", remote_side=[id], backref="subordinates")
    
    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))