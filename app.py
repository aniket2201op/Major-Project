import pickle
from pathlib import Path

import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


# --- USER AUTHENTICATION ---
# names = ["Peter Parker", "Rebecca Miller"]
# usernames = ["pparker", "rmiller"]
credentials = {
        "usernames":{
            "jsmith92":{
                "name":"john smith",
                "password":"$2b$12$HUxcAwtMpfPNS60/g190cujUgbTVD9Xl0ai65Oy7k7Kt8GhbxtsUe�a"
                }
                     
            }
        }

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(credentials,
    "sales_dashboard", "abcdef", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    # ---- READ EXCEL ----
    st.write("Hello World")
