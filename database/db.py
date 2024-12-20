from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import bcrypt
from database.base import Base
from app.user import User  # 这个导入移到函数内部

# 创建SQLite数据库引擎
engine = create_engine('sqlite:///database/users.db', echo=True)

# 创建数据库会话类
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """初始化数据库并创建测试用户"""
    # 在这里导入 User 模型，避免循环导入
    from app.user import User
    
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
    from app.user import User  # 在函数内部导入
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and user.verify_password(password):
            return user
        return None
    except Exception as e:
        print(f"认证用户时出错: {e}")
        return None