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

def main():
  st.write('hello jwt')
  st.write(st.session_state.token)
  username = st.text_input("Username")
  st.write(username)

if __name__ == '__main__':
  main()