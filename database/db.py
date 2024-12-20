from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt
from datetime import datetime
from app.user import User  # 导入User模型

# 创建SQLite数据库引擎
engine = create_engine('sqlite:///database/users.db', echo=True)

# 创建数据库会话类
# sessionmaker用于创建会话工厂,绑定到我们的数据库引擎
SessionLocal = sessionmaker(bind=engine)

# 创建声明性基类
# Base类将用作所有模型类的基类,用于声明数据库模型
Base = declarative_base()

def init_db():
    """初始化数据库并创建测试用户"""
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 检查测试用户是否存在
        test_user = db.query(User).filter(User.username == 'test').first()
        
        if not test_user:
            # 创建测试用户
            password = 'test123456'
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            test_user = User(
                username='test',
                password_hash=hashed.decode('utf-8'),
                level=1,  # 设置用户层级
                parent_id=0  # 测试账号的上级用户为0
            )
            
            db.add(test_user)
            db.commit()
            print("测试用户创建成功！用户名：test，密码：test123456")
    
    except Exception as e:
        print(f"创建测试用户时出错: {e}")
        db.rollback()
    finally:
        db.close()

# 创建数据库会话的生成器函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 用户认证函数
def authenticate_user(username: str, password: str):
    """验证用户登录信息"""
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and user.verify_password(password):
            return user
        return None
    finally:
        db.close()