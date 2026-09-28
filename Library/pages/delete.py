import streamlit as st
from library import BookListCreateRetrieveUpdateDelete

st.title("Delete Specific Record")

id = st.text_input("Enter Book ID")

btn= st.button("Show Details")
if btn:
    if id:
        b = BookListCreateRetrieveUpdateDelete()
        record = b.delete(id)
        if record==True:
            st.success("deleted sucessfully")
        else:
            st.warning("no record found")
    else:
        st.warning("Please enter Book ID")


