import streamlit as st
from library import BookListCreateRetrieveUpdateDelete

st.title("Read all Book Record")
b=BookListCreateRetrieveUpdateDelete()
records=b.list()
st.table(records)
