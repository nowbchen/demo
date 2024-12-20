import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base

# 数据库文件路径
DB_PATH = 'database/users.db'

# 创建SQLite数据库引擎
engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)

# 创建数据库会话类
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """初始化数据库并创建测试用户"""
    from app.user import User
    
    # 如果数据库文件存在，先删除它
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("删除旧的数据库文件")
    
    # 确保database目录存在
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    print("创建新的数据库表")
    
    # 创建数据库会话
    db = SessionLocal()
    
    try:
        # 创建测试用户
        test_user = User(
            username='test',
            password_hash=User.hash_password('test123456').decode('utf-8'),
            level=1,
            parent_id=None
        )
        
        db.add(test_user)
        db.commit()
        print("测试用户创建成功！用户名：test，密码：test123456")
    
    except Exception as e:
        print(f"创建测试用户时出错: {e}")
        db.rollback()
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(db, username: str, password: str):
    """验证用户登录信息"""
    from app.user import User
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and user.verify_password(password):
            return user
        return None
    except Exception as e:
        print(f"认证用户时出错: {e}")
        return None