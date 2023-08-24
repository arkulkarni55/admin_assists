
import streamlit as st

  st.set_page_config(
    layout="wide",
    page_title="App_Utility"
)
    
app_selection = st.sidebar.selectbox("Utility",("Log_In","Help_Page","File_Upload_Utility","Over_Under_Size_File_Identifier","User_Management","Log_Out"))

from pages import Log_In,Help_Page,File_Upload_Utility,Over_Under_Size_File_Identifier,User_Management,Log_Out

app_functions = {

  "Log_In" : Log_In.app,
  "Help_Page": Help_Page.app,
  "File_Upload_Utility": File_Upload_Utility.app,
  "Over_Under_Size_File_Identifier" : Over_Under_Size_File_Identifier.app,
  "User_Management" : User_Management.app ,
  "Log_Out" : Log_Out.app
  
}


if app_selection in app_functions:
  app_functions[app_selection]()
else:
  st.error("Apps not found")




# from pages import Log_In,Help_Page,File_Upload_Utility,Over_Under_Size_File_Identifier,User_Management,Log_Out


# app = MultiApp()

# st.markdown("""
# # Multi-Page App

# # This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

# """)

# # Add all your application here
# app.add_app("Log_In" : Log_In.app),
# app.add_app("Help_Page": Help_Page.app),
# app.add_app("File_Upload_Utility": File_Upload_Utility.app),
# app.add_app("Over_Under_Size_File_Identifier" : Over_Under_Size_File_Identifier.app),
# app.add_app("User_Management" : User_Management.app),
# app.add_app("Log_Out" : Log_Out.app)

# # The main app
# app.run()
