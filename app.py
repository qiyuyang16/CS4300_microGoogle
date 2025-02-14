import streamlit as st
from multiapp import MultiApp
import v1_app
import v2_app
import v3_app
# import st_sandbox

app = MultiApp()
st.set_page_config(layout="wide",page_title='1e94: microGoogle', page_icon='📖')
st.image('logo.png')


# Add all your application here
app.add_app("Version 3", v3_app.app)
app.add_app("Version 2", v2_app.app)
app.add_app("Version 1", v1_app.app)
app.run()
#app.add_app("Model", model.app)
# The main app
