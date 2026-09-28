import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIVE','UPDATE','DELETE'])
b=BookListCreateRetrieveUpdateDelete()

with tab1:
    st.title("Add:")
with tab2:
    st.title("READ:")
with tab3:
    st.title("RETRIVE:")
with tab4:
    st.title("DELETE:")
with tab5:
    st.title("UPDATE:")