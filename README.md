# 用户评分系统

这是一个基于Streamlit开发的Web应用程序，提供用户登录、鉴权和互相评分功能。

## 项目结构

project_root/
├── README.md
├── main.py # 主程序入口
├── config/
│ └── config.py # 配置文件（数据库配置、应用配置等）
├── database/
│ └── db.py # 数据库操作和模型定义
├── models/
│ ├── user.py # 用户模型
│ └── rating.py # 评分模型
├── pages/
│ ├── login.py # 登录页面
│ ├── register.py # 注册页面
│ ├── dashboard.py # 用户仪表盘
│ └── rating.py # 评分页面
├── utils/
│ ├── auth.py # 认证工具
│ └── session.py # 会话管理
└── requirements.txt # 项目依赖

## 功能特性

1. 用户管理
    - 用户注册：新用户可以注册账号
    - 用户登录：已注册用户可以登录系统
    - 会话管理：维护用户登录状态

2. 评分系统
    - 用户互评：用户之间可以互相评分
    - 评分历史：查看历史评分记录
    - 评分统计：统计和展示评分数据

## 技术栈

- Python 3.8+
- Streamlit
- SQLite
- SQLAlchemy
- bcrypt（密码加密）

## 安装和运行

1. 克隆项目：

```bash
git clone https://github.com/your-username/user-rating-system.git
cd user-rating-system
```

2. 创建虚拟环境（推荐）：

```bash
python -m venv venv
source venv/bin/activate
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

4. 运行应用：

```bash
streamlit run main.py
```

## 使用说明

1. 首次访问时，需要注册账号
2. 使用注册的账号登录系统
3. 登录后可以：
    - 在仪表盘查看个人信息和评分统计
    - 在评分页面对其他用户进行评分
    - 查看历史评分记录

## 开发计划

[x] 基础框架搭建
[ ] 用户认证系统
[ ] 评分功能实现
[ ] 数据可视化
[ ] 用户界面优化

## 注意事项

本项目使用 SQLite 数据库，无需额外配置数据库服务
所有密码都经过加密存储
建议在虚拟环境中运行项目

## 创建项目结构

```bash
mkdir -p project_root/{config,database,models,pages,utils}
cd project_root
touch main.py
touch config/config.py
touch database/db.py
touch models/{user.py,rating.py}
touch pages/{login.py,register.py,dashboard.py,rating.py}
touch utils/{auth.py,session.py}
touch requirements.txt
```
