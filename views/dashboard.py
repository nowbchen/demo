import streamlit as st
from database.db import SessionLocal
from app.user import User
import plotly.express as px
import pandas as pd

def dashboard_page():
    # 检查登录状态
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.warning("请先登录！")
        st.stop()
    
    # 创建侧边栏
    with st.sidebar:
        st.title("功能菜单")
        selected_page = st.radio(
            "选择功能",
            ["个人信息", "评分管理", "数据统计"]
        )
        
        # 登出按钮
        if st.button("退出登录"):
            st.session_state['logged_in'] = False
            st.session_state['user_id'] = None
            st.session_state['username'] = None
            st.rerun()
    
    # 主页面标题
    st.title(f"欢迎回来, {st.session_state['username']}!")
    
    # 根据选择显示不同内容
    if selected_page == "个人信息":
        show_profile()
    elif selected_page == "评分管理":
        show_rating_management()
    else:
        show_statistics()

def show_profile():
    st.header("个人信息")
    
    # 创建两列布局
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("基本信息")
        st.write(f"用户名：{st.session_state['username']}")
        st.write("用户ID：", st.session_state['user_id'])
        st.write("注册时间：2024-01-01")  # 示例数据
        
        # 编辑个人信息按钮
        if st.button("编辑个人信息"):
            st.info("功能开发中...")
    
    with col2:
        st.subheader("账户状态")
        st.write("活跃状态：正常")
        st.write("上次登录：2024-03-20")  # 示例数据
        st.write("评分权限：已开启")

def show_rating_management():
    st.header("评分管理")
    
    # 创建标签页
    tab1, tab2 = st.tabs(["我的评分", "收到的评分"])
    
    with tab1:
        # 示例数据
        my_ratings = pd.DataFrame({
            '被评分用户': ['用户A', '用户B', '用户C'],
            '评分': [4.5, 3.8, 5.0],
            '评分时间': ['2024-03-19', '2024-03-18', '2024-03-17']
        })
        st.dataframe(my_ratings)
        
        if st.button("新建评分"):
            st.info("功能开发中...")
    
    with tab2:
        # 示例数据
        received_ratings = pd.DataFrame({
            '评分用户': ['用户X', '用户Y', '用户Z'],
            '评分': [4.8, 4.2, 4.6],
            '评分时间': ['2024-03-20', '2024-03-19', '2024-03-18']
        })
        st.dataframe(received_ratings)

def show_statistics():
    st.header("数据统计")
    
    # 创建示例数据
    ratings_data = pd.DataFrame({
        '月份': ['1月', '2月', '3月'],
        '平均评分': [4.2, 4.5, 4.8],
        '评分次数': [5, 8, 12]
    })
    
    # 显示统计图表
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("评分趋势")
        fig1 = px.line(ratings_data, x='月份', y='平均评分')
        st.plotly_chart(fig1)
    
    with col2:
        st.subheader("评分活跃度")
        fig2 = px.bar(ratings_data, x='月份', y='评分次数')
        st.plotly_chart(fig2)
    
    # 显示统计摘要
    st.subheader("统计摘要")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.metric(label="总评分次数", value="25次")
    with col4:
        st.metric(label="平均评分", value="4.5分")
    with col5:
        st.metric(label="本月排名", value="第3名") 