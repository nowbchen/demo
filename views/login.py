import streamlit as st
from database.db import SessionLocal
from utils.auth import authenticate_user
import time

def login_page():
    st.title("用户登录")
    
    # 创建登录表单
    with st.form("login_form"):
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        submit = st.form_submit_button("登录")
        
        if submit:
            if not username or not password:
                st.error("用户名和密码不能为空！")
                return
            
            # 验证用户
            db = SessionLocal()
            user = authenticate_user(db, username, password)
            
            if user:
                # 登录成功，设置会话状态
                st.session_state['logged_in'] = True
                st.session_state['user_id'] = user.id
                st.session_state['username'] = user.username
                
                with st.spinner('登录成功，正在跳转...'):
                    time.sleep(1)  # 添加一个短暂的延迟
                st.rerun()
            else:
                st.error("用户名或密码错误！")
            
            db.close()

    # 添加注册链接
    st.markdown("还没有账号？[点击注册](/register)")