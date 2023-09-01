import pickle
from pathlib import Path

import streamlit_authenticator as stauth

credentials = {
        "usernames":{
            "jsmith92":{
                "name":"john smith",
                "password":"abc123"
                }
                     
            }
        }
hashed_passwords = stauth.Hasher(credentials['usernames']['jsmith92']['password']).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
