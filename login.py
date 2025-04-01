import streamlit as st
import database  # Import database functions

def login():
    st.title("Login Page")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_btn"):
        if database.verify_user(username, password):
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password")


def register():
    st.title("Register")

    username = st.text_input("Choose a Username", key="register_username")
    password = st.text_input("Choose a Password", type="password", key="register_password")

    if st.button("Register", key="register_btn"):
        if database.add_user(username, password):
            st.success("Registration Successful! You can now log in.")
        else:
            st.error("Username already taken. Try another one.")

# Maintain authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# If logged in, show a logout button
if st.session_state["authenticated"]:
    st.write(f"✅ You are logged in as **{st.session_state['user']}**")
    
    if st.button("Logout", key="logout_btn"):
        st.session_state["authenticated"] = False
        st.session_state["user"] = None
        st.experimental_rerun()
else:
    option = st.radio("Choose:", ["Login", "Register"])
    
    if option == "Login":
        login()
    else:
        register()
