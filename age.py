import streamlit as st
import datetime

today = datetime.date.today()
olddate = datetime.datetime(1900, 1, 1)

st.title('Age Calculator')
birth = st.date_input(
    "Date of Birth:", today, min_value = olddate)

st.write("Your date of birth is", birth)

age = today - birth

st.write('You have been alive {} days.'.format(age.days))