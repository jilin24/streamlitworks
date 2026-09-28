import streamlit as st
from library import BookListCreateRetrieveUpdateDelete

st.title("Read Specific Record")

id = st.text_input("Enter Book ID")

btn= st.button("Show Details")
if btn:
    if id:
        b = BookListCreateRetrieveUpdateDelete()
        record = b.retrieve(id)

        if record:
            st.write("Title:", record[1])
            st.write("Author:", record[2])
            st.write("Price:", record[3])
            st.write("Pages:", record[4])
            st.write("Language:", record[5])
        else:
            st.write("No record found")
    else:
        st.warning("Please enter Book ID")