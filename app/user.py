from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
import bcrypt

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(100))
    level = Column(Integer, default=1)
    parent_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    
    parent = relationship("User", remote_side=[id], backref="subordinates")
    
    @staticmethod
    def hash_password(password):
        """将密码转换为哈希值"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def verify_password(self, password):
        """验证密码"""
        try:
            return bcrypt.checkpw(
                password.encode('utf-8'),
                self.password_hash.encode('utf-8')
            )
        except Exception as e:
            print(f"密码验证出错: {e}")
            return False
    
    def __repr__(self):
        return f"<User {self.username}>"