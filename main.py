import streamlit as st
from pages import Log_In,Help_Page,File_Upload_Utility,Over_Under_Size_File_Identifier,User_Management,Log_Out


app_selection = st.sidebar.selectbox("Utility",("Log_In","Help_Page","File_Upload_Utility","Over_Under_Size_File_Identifier","User_Management","Log_Out"))


st.set_page_config(
  layout="wide",
  page_title="App_Utility"
)



app_functions =  {

  "Log_In" : Log_In.app,
  "Help_Page": Help_Page.app,
  "File_Upload_Utility": File_Upload_Utility.app,
  "Over_Under_Size_File_Identifier" : Over_Under_Size_File_Identifier.app,
  "User_Management" : User_Management.app,
  "Log_Out" : Log_Out.app
}


if app_selection in app_functions:
  app_functions[app_selection]()
else:
  st.error("Apps not found")

