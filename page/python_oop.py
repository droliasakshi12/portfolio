import streamlit as st

st.subheader("Python OOP Project",divider="blue")

desk="https://github.com/droliasakshi12/python-oop-project/blob/main/desktop_notification_project.py"
emoji="https://github.com/droliasakshi12/python-oop-project/blob/main/emoji_converter.py"
mouse="https://github.com/droliasakshi12/python-oop-project/blob/main/mouse_clicking.py"
generator="https://github.com/droliasakshi12/python-oop-project/blob/main/qr_code_generator.py"
decoder="https://github.com/droliasakshi12/python-oop-project/blob/main/qrcode_decoder.py"





st.markdown("**The desktop notification project is all about the notification displayed on the desktop , in this project we have made the use of python object oriented programming which includes the use of classes and object.**")
st.caption("<h5> To view the project  please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="DESKTOP NOTIFICATION PROJECT",url=desk,icon="💻")
st.divider()


st.markdown("**In the emoji converter project wecan convert the emoji into the name of the emoji.**")    
st.caption("<h5> To view the project  please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="EMOJI CONVERTER",url=emoji,icon="😊")
st.divider()


st.markdown("**In mouse clicking project whenever you hover or click anywhere that app will get open.This project is also made using python object oriented programming language.**")
st.caption("<h5> To view the project  please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="MOUSE CLICKING",url=mouse,icon="🖱")
st.divider()

st.markdown("**The QRcode generator project is used to generate the qrcode of any website or link you input.Here the user just have to import the link of which they want to generate the qrcode and it will simiply generate it for you!.**")
st.caption("<h5> To view the project  please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="QR CODE GENERATOR",url=generator,icon=":material/qr_code:")
st.divider()

st.markdown("**QRcode decoder project is the reverse of the qrcode generator project where you ave to provide the image of the qrcode and it will decode it and return you the link of that qrcode.**")
st.caption("<h5> To view the project  please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="QR CODE DECODER",url=decoder,icon=":material/qr_code_2:")




