# 导入SQLAlchemy所需的组件
from sqlalchemy import create_engine, Column, Integer, String  # 导入数据库引擎创建、列类型等工具
from sqlalchemy.ext.declarative import declarative_base  # 导入声明性基类
from sqlalchemy.orm import sessionmaker  # 导入会话生成器
import sqlite3
from pathlib import Path
import bcrypt

# 创建SQLite数据库引擎
# sqlite:///user_rating.db 指定了SQLite数据库文件的路径
# echo=True 表示启用SQL语句输出,方便调试
engine = create_engine('sqlite:///user_rating.db', echo=True)

# 创建数据库会话类
# sessionmaker用于创建会话工厂,绑定到我们的数据库引擎
SessionLocal = sessionmaker(bind=engine)

# 创建声明性基类
# Base类将用作所有模型类的基类,用于声明数据库模型
Base = declarative_base()

# 创建数据库会话的生成器函数
def get_db():
    # 创建新的数据库会话
    db = SessionLocal()
    try:
        # yield语句使这个函数成为一个生成器,允许在with语句中使用
        yield db
    finally:
        # 确保在使用完毕后关闭数据库连接
        db.close()

class Database:
    def __init__(self):
        self.db_path = Path("database/users.db")
        self.init_database()
        self.create_test_user()
    
    def init_database(self):
        """初始化数据库表"""
        conn = sqlite3.connect(str(self.db_path))
        c = conn.cursor()
        
        # 创建用户表
        c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # 创建评分表
        c.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_user_id INTEGER,
            to_user_id INTEGER,
            score INTEGER,
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (from_user_id) REFERENCES users (id),
            FOREIGN KEY (to_user_id) REFERENCES users (id)
        )
        ''')
        
        conn.commit()
        conn.close()

    def create_test_user(self):
        """创建测试用户"""
        conn = sqlite3.connect(str(self.db_path))
        c = conn.cursor()
        
        # 检查测试用户是否已存在
        c.execute('SELECT id FROM users WHERE username = ?', ('test',))
        if c.fetchone() is None:
            # 对密码进行加密
            password = 'test123456'
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            # 创建测试用户
            c.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
            ''', ('test', hashed.decode('utf-8')))
            
            conn.commit()
            print("测试用户创建成功！用户名：test，密码：test123456")
        
        conn.close()