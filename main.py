import streamlit as st
from database.db import init_db
from views.login import login_page
from views.dashboard import dashboard_page

# 初始化数据库和创建测试用户
init_db()

def main():
    # 设置页面标题和隐藏汉堡菜单
    st.set_page_config(
        page_title="用户评分系统",
        menu_items=None  # 隐藏汉堡菜单
    )
    
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