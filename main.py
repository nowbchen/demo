import streamlit as st
from database.db import engine, Base
from pages.login import login_page
from pages.dashboard import dashboard_page

# 初始化数据库表
Base.metadata.create_all(bind=engine)

def main():
    # 设置页面标题
    st.set_page_config(page_title="用户评分系统")
    
    # 检查登录状态
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    
    # 根据登录状态显示不同页面
    if st.session_state['logged_in']:
        dashboard_page()
    else:
        login_page()

if __name__ == "__main__":
    main()