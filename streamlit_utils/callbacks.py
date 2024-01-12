import time
import streamlit as st


def on_return_to_predict():
    st.session_state['current_window'] = 'prediction'

def on_make_predict():
    time.sleep(2.5)  #!!!

    st.session_state['current_prediction'] = 'Adult'
 
def on_go_to_add_money():
    if 'current_prediction' in st.session_state:
        del st.session_state['current_prediction']
    st.session_state['current_window'] = 'money'

def on_return_to_predict():
    st.session_state['current_window'] = 'prediction'
    
def on_login():
    login = st.session_state['login_input']
    password = st.session_state['password_input']
    # url = "https://timeout1.p.rapidapi.com/timeout/5000"

    # response = requests.get(url, headers={
    #     "X-RapidAPI-Key": "9fe800dd15msh882eee06332427dp19a59cjsn3da8503b413b",
    #     "X-RapidAPI-Host": "timeout1.p.rapidapi.com"
    # })
    # if response.status_code == 200:
    #     st.session_state['jwt'] == 'TEST_TOKEN'
    #     st.session_state['current_window'] = 'prediction'

    time.sleep(2.5)  #!!!

    if login == 'abc':  # * DEBUG
        st.info('Wrong user or password', icon="❗")
    else:
        st.session_state['current_window'] = 'prediction'


def on_register():
    login = st.session_state['login_input']
    password = st.session_state['password_input']

    time.sleep(2.5)  #!!!

    if login == 'abc':  # * DEBUG
        st.info('Successfully registered', icon="ℹ️")
    else:
        st.info('User already exists', icon="❗")


def on_add_money():
    money = st.session_state['money_to_add']

    time.sleep(2.5)  #!!!

    if money >= 30:  # * DEBUG
        st.info('Successfully added money', icon="ℹ️")
    else:
        st.info('Internal error', icon="❗")