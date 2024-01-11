import streamlit as st
import pandas as pd
import numpy as np
import requests
import time




def main():
    states = {
        'auth': login_screen,
        'registration': 'Registration',
        'prediction': prediction_screen,
        'money': 'Money'
    }

    if 'jwt' not in st.session_state and 'current_window' not in st.session_state:
        st.session_state['jwt'] = ''
        st.session_state['current_window'] = 'auth'
       

    # st.header(st.session_state['current_window'].value)
    st.session_state

    # states[st.session_state['current_window']]() # ?

    if st.session_state['current_window'] == 'auth': # ?
        login_screen()
    elif st.session_state['current_window'] == 'prediction':
        prediction_screen()
    else:
        raise Exception



def on_login():  
    # url = "https://timeout1.p.rapidapi.com/timeout/5000"

    # response = requests.get(url, headers={
    #     "X-RapidAPI-Key": "9fe800dd15msh882eee06332427dp19a59cjsn3da8503b413b",
    #     "X-RapidAPI-Host": "timeout1.p.rapidapi.com"
    # })
    # if response.status_code == 200:
    #     st.session_state['jwt'] == 'TEST_TOKEN'
    #     st.session_state['current_window'] = 'prediction'

    time.sleep(2.5)
    st.session_state['current_window'] = 'prediction'
 


def login_screen():
    with st.form(key="my_form"):
        st.text_input('Login', value='', key='login_input')
        st.text_input('Password', value='', type='password',
                      key='password_input')
        st.form_submit_button('Enter', on_click=on_login)


def prediction_screen():
    st.write("Sucess")


def register_screen():
    pass


def add_money_screen():
    pass


if __name__ == '__main__':
    main()


