import streamlit as st

qp = st.experimental_get_query_params()
print(qp)

try:
  query_token = qp['token'][0]
  st.session_state.token = query_token # this will set if there is a query_token
except:
  pass

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

"""
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

def main():
  st.write('hello jwt')
  st.write(st.session_state.token)
  username = st.text_input("Username")
  st.write(username)

if __name__ == '__main__':
  main()