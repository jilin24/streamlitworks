import streamlit as st
from donor import DonorListCreateRetrieveUpdateDelete
from datetime import date

st.title("Blood Donor Management System")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["ADD", "READ", "RETRIEVE", "UPDATE", "DELETE"]
)

b = DonorListCreateRetrieveUpdateDelete()


with tab1:
    st.header("Add New Donor")

    name = st.text_input("Enter Donor Name")

    blood_group = st.selectbox(
        "Select Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    phone = st.text_input("Enter Phone Number")
    city = st.text_input("Enter City")

    last_donation = st.date_input(
        "Last Donation Date",
        value=date.today()
    )

    if st.button("Add Donor"):
        try:
            if name and phone and city:
                b.create(
                    name, blood_group, phone, city, last_donation
                )
                st.success("Donor added successfully")
            else:
                st.warning("Please fill all fields")
        except Exception as e:
            st.error(str(e))



with tab2:
    st.header("All Donors")

    if st.button("Show All Donors"):
        records = b.list()

        if records:
            st.dataframe(records)
        else:
            st.warning("No records found")


with tab3:
    st.header("Retrieve Donor")

    donor_id = st.number_input(
        "Enter Donor ID",
        min_value=1,
        step=1,
        key="retrieve_id"
    )

    if st.button("Retrieve Donor"):
        record = b.retrieve(donor_id)

        if record:
            st.write("ID:", record[0])
            st.write("Name:", record[1])
            st.write("Blood Group:", record[2])
            st.write("Phone:", record[3])
            st.write("City:", record[4])
            st.write("Last Donation:", record[5])
        else:
            st.warning("No donor found")



with tab4:
    st.header("Update Donor")

    donor_id = st.number_input(
        "Enter Donor ID to Update",
        min_value=1,
        step=1,
        key="update_id"
    )

    name = st.text_input("Enter New Name", key="update_name")

    blood_group = st.selectbox(
        "Select New Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
        key="update_group"
    )

    phone = st.text_input("Enter New Phone", key="update_phone")
    city = st.text_input("Enter New City", key="update_city")

    last_donation = st.date_input(
        "Select New Last Donation Date",
        value=date.today(),
        key="update_date"
    )

    if st.button("Update Donor"):
        try:
            result = b.update(
                donor_id, name, blood_group, phone, city, last_donation
            )

            if result:
                st.success("Donor updated successfully")
            else:
                st.warning("No donor found")
        except Exception as e:
            st.error(str(e))


with tab5:
    st.header("Delete Donor")

    donor_id = st.number_input(
        "Enter Donor ID to Delete",
        min_value=1,
        step=1,
        key="delete_id"
    )

    if st.button("Delete Donor"):
        try:
            result = b.delete(donor_id)

            if result:
                st.success("Donor deleted successfully")
            else:
                st.warning("No donor found")
        except Exception as e:
            st.error(str(e))