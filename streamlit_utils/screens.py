import time
import streamlit as st


        
        
        
def login_screen():
    with st.form(key="auth_form"):
        st.text_input('Login', value='', key='login_input')
        st.text_input('Password', value='', type='password',
                      key='password_input')
        st.form_submit_button('Enter', on_click=on_login)
        st.form_submit_button("Don't have account? Register",
                              on_click=on_register)
   
def add_money_screen():
    st.header('Add money', divider='rainbow')

    with st.form(key="money_form", border=False, clear_on_submit=True):
        st.number_input("Insert a number", value=None,
                        min_value=0.1, key='money_to_add')
        st.form_submit_button('Add money', on_click=on_add_money)

    st.button('Back', on_click=on_return_to_predict)


def prediction_screen():
    st.header('Make a predict', divider='blue')

    if 'current_prediction' in st.session_state:
        col_1, col_2 = st.columns(2)
        with col_1:
            st.markdown("## :blue[Predicted class:]")
        with col_2:
            st.markdown(f"## :red[{st.session_state['current_prediction']}]")

    with st.form(key="predict_form", border=False, clear_on_submit=True):
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.number_input("SEQN",
                            value=73564, key='SEQN')
            st.number_input("RIAGENDR",
                            value=2, key='RIAGENDR')
        with c2:
            st.number_input("PAQ605",
                            value=2, key='PAQ605')
            st.number_input("BMXBMI",
                            value=35.7, key='BMXBMI')
        with c3:
            st.number_input("LBXGLU",
                            value=110, key='LBXGLU')
            st.number_input("DIQ010",
                            value=2, key='DIQ010')
        with c4:
            st.number_input("LBXGLT",
                            value=150, key='LBXGLT')
            st.number_input("LBXIN",
                            value=14.91, key='LBXIN')

        st.form_submit_button('PREDICT', type='primary',
                              on_click=on_make_predict)
    st.button('Add money', on_click=on_go_to_add_money)
