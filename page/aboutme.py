import streamlit as st 

left_col , right_col=st.columns(2,gap="large",vertical_alignment="top",)

with left_col:
    st.image(image="image.png",width=240)
    st.write("</br></br><br></br>",unsafe_allow_html=True)



with right_col:
    st.header("SAKSHI DROLIA",divider="blue",anchor=False)
    st.write("<h5>I am currently pursuing bachelor's of computer application(BCA) DEGREE</h5>",unsafe_allow_html=True)
    st.write('''<h5>Motivated BCA student with foundational skills in programming and database management,enthusiastic to learn  detail oriented Generative AI  with hands on experience in building LLM based tools.Eager to apply AI skills in an internship that challenges me to develop real world AI applications.
</h5>''',unsafe_allow_html=True)



    
st.header(":orange[EDUCATION]",divider="blue",anchor=False)

left,right=st.columns(2)
with left:
    st.write("<h5>SDJ International College</br>•Bacholer's of Computer Applications</br>•2023-2026</br>•Present</h5>",unsafe_allow_html=True)
st.write("<h5>L.P Savani Academy</br>•Class 12</br>•2022-2023</br>•Percentage-91.6%</h5></br>",unsafe_allow_html=True)


st.header(":orange[Skills]",divider= True,anchor=False)
left,right=st.columns(2)
with left:
    st.markdown("<h4>Programming Language</h4>",unsafe_allow_html=True)
    st.write("<h5>-Python</br>-Sql</br></h5></br>",unsafe_allow_html=True)
    st.write("<h4>Python Libraries</h4><h5>-Pandas</br>-Numpy</br>-Matplotlib</br>-Seaborn</br>-Langchain</br>-LangGraph</br>-Flask</br>-FastAPI<h5>",unsafe_allow_html=True)
    st.write("<h4>•Indian Classical Music </br>•Writing</br>•Team Work</h4>",unsafe_allow_html=True)


st.header(":orange[Language]",divider="blue")
st.write("<h5>•English</br>•Hindi</h5>",unsafe_allow_html=True)



