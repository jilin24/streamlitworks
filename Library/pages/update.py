import streamlit as st
from library import BookListCreateRetrieveUpdateDelete
st.title("update  Record")

title=st.text_input("Title")
author=st.text_input("Author")
price=st.number_input("Price",min_value=0)
pages=st.number_input("Pages",min_value=0)
language=st.text_input("Language")
id = st.text_input("Enter Book ID")

btn= st.button("Update")
if btn:
    if id:
        b = BookListCreateRetrieveUpdateDelete()
        record = b.update(id,title,author,price,pages,language)
        if record==True:
            st.success("Updated sucessfully")
        else:
            st.warning("no record found")
    else:
        st.warning("Please enter Book ID")



