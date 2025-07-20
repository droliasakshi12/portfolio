import streamlit as st 

left_col , right_col=st.columns(2,gap="small",vertical_alignment="top")

with left_col:
    st.image(image="girl.jpeg",width=250)
    st.write("</br></br><br></br>",unsafe_allow_html=True)
    


with right_col:
    st.header("SAKHSI DROLIA",divider="blue",anchor=False)
    st.write("<h6>I am currently pursuing bachelor's of computer application(BCA) DEGREE</h6>",unsafe_allow_html=True)
    st.write('''<h6>Motivated BCA student with foundational skills in programming and database management,enthusiastic to learn  detail oriented Generative AI  with hands on experience in building LLM based tools.Eager to apply AI skills in an internship that challenges me to develop real world AI applications.
</h6>''',unsafe_allow_html=True)



    
st.header("EDUCATION",divider="blue",anchor=False)
left,right=st.columns(2)
with left:
    st.write("<h5>SDJ International College</br>•Bacholer's of Computer Applications</br>•2023-2026</br>•Present</h5>",unsafe_allow_html=True)
st.write("<h5>L.P Savani Academy</br>•Class 12</br>•2022-2023</br>•Percentage-91.6%</h5></br>",unsafe_allow_html=True)


st.header("Skills",divider= True,anchor=False)
st.write("<h5>•Programming</br>•Indian Classical Music</br>•Writing</br>•Team Work</h5></br>",unsafe_allow_html=True)


st.header("Language",divider="blue")
st.write("<h5>•English</br>•Hindi</h5>",unsafe_allow_html=True)

