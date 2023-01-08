import streamlit as st
import pandas

companyName = "Best Company in World"
aboutCompany = '''
                A company profile is a professional written summary or introduction of a business. 
                Its objective is to make others know your company. 
                It also make others know all your business’ activities, the reputation of your company, and the products that your company can offer. 
                With a company profile, you can get a capital through investors. It is a promotional tool that can make them attracted to your brand. 
                You will just have to show them your business profile and if they like it, they can raise a capital for your company. 
                '''

st.header(companyName)
st.write(aboutCompany)

st.subheader("Our Team")
col1,col2,col3=st.columns(3)

emp_df= pandas.read_csv('data.csv')

with col1:
    for index, row in emp_df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in emp_df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in emp_df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])