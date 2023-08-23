import streamlit as st
from multiapp import Multiapp
from pages import 2_Help_Page,3_File_Upload_Utility,4_Over_Under_Size_File_Identifier,5_User_Management,6_Log_Out
app = Multiapp ()

app.add_ap("2_Help_Page",2_Help_Page.app)
app.add_ap("3_File_Upload_Utility",3_File_Upload_Utility.app)
app.add_ap("4_Over_Under_Size_File_Identifier",4_Over_Under_Size_File_Identifier.app)
app.add_ap("5_User_Management",5_User_Management.app)
app.add_ap("6_Log_Out",6_Log_Out.app)

app.run 
