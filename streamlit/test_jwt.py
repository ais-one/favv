import streamlit as st
import requests
import json

def sso_logout():
  try:
    del st.session_state['token']
  except:
    pass

def sso_get_token_query(query_name='token'):
  try:
    qp = st.experimental_get_query_params()
    st.write(qp[query_name][0])
    return qp[query_name][0]
  except Exception as err:
    # st.write(f"Unexpected {err=}, {type(err)=}")
    return ''

def sso_login(token, verify_url, params=None, headers=None):
  st.write('SSO Login...', token)
  try:
    if (headers == None):
      headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
      }
    res = requests.get(
      verify_url,
      params=params,
      headers=headers,
    )
    if (res.status_code != 200):
      sso_logout()
      return False
    else:
      if 'token' not in st.session_state:
        st.session_state['token'] = token
      return True
  except Exception as err:
    # st.write(f"Unexpected {err=}, {type(err)=}")
    sso_logout()
    return False

st.write('Start SSO Test')

VERIFY_URL='http://127.0.0.1:3000/verify'
LOGIN_URL='http://127.0.0.1:3000/login'

token = sso_get_token_query(query_name='token')
isLoggedIn = sso_login(
  token=token,
  verify_url=VERIFY_URL,
  params={ 'token': token }
)

if (isLoggedIn != True):
  login_url=LOGIN_URL
  st.write('Login Fail')
  st.write(f'''
    <a target="_self" href="{login_url}"><button>Login</button></a>
  ''', unsafe_allow_html=True)
  st.stop()
else:
  st.write('SSO pass: my first hello world')
  st.write(f'''
    <a target="_self" href="/"><button>Logout</button></a>
  ''', unsafe_allow_html=True)
  st.stop()


## MANUAL REDIRECT
# if st.button('Go to Streamlit'):
#     js = "window.open('https://www.streamlit.io/')"  # New tab or window
#     js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
#     html = '<img src onerror="{}">'.format(js)
#     div = Div(text=html)
#     st.bokeh_chart(div)

## AUTO REDIRECT
# import webbrowser
# url = 'https://www.streamlit.io/'
# if st.button('Open browser'):
#     webbrowser.open_new_tab(url)

# if 'token' not in st.session_state:
#  redirect
# JWT - https://auth0.com/blog/how-to-handle-jwt-in-python
# verify the token signature here, and also get payload...
# if token error or no token, redirect to IDP
# else pass continue

todo = """
# https://pyjwt.readthedocs.io/en/latest/usage.html

pip install pyjwt[crypto]

import jwt
from cryptography.hazmat.primitives import serialization
from jwt.exceptions import ExpiredSignatureError


# HS256
payload_data = {
  "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=30)
  "sub": "4242",
  "name": "Jessica Temporal",
  "nickname": "Jess"
}
my_secret = 'my_super_secret'
token = jwt.encode(
    payload=payload_data,
    key=my_secret,
    leeway=10 # or datetime.timedelta(seconds=10)
)

header_data = jwt.get_unverified_header(token)
# {'typ': 'JWT', 'alg': 'RS256'}

try:
  payload = jwt.decode(
    token,
    key='my_super_secret',
    algorithms=[header_data['alg'], ]
  )
except ExpiredSignatureError as error:
  print(f'Unable to decode the token, error: {error}')


# RS256
# read and load the key
private_key = open('.ssh/id_rsa', 'r').read()
key = serialization.load_ssh_private_key(private_key.encode(), password=b'')
new_token = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='RS256'
)

public_key = open('.ssh/id_rsa.pub', 'r').read()
key = serialization.load_ssh_public_key(public_key.encode())
jwt.decode(jwt=token, key=key, algorithms=['RS256', ])
"""

# def main():
#   st.write('hello jwt')
#   st.write(st.session_state.token)
#   username = st.text_input("Username")
#   st.write(username)

# if __name__ == '__main__':
#   main()