import streamlit as st
from multiapp import Multiapp
from pages import Log_In,Help_Page,File_Upload_Utility,Over_Under_Size_File_Identifier,User_Management,Log_Out
app = Multiapp()

app.add_ap("Log_In",Log_In.app)
app.add_ap("Help_Page",Help_Page.app)
app.add_ap("File_Upload_Utility",File_Upload_Utility.app)
app.add_ap("Over_Under_Size_File_Identifier",Over_Under_Size_File_Identifier.app)
app.add_ap("User_Management",User_Management.app)
app.add_ap("Log_Out",Log_Out.app)

app.run 
