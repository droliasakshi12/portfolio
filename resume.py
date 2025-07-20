import streamlit as st
import pathlib


def load_css(css_file):
    with open(css_file) as f:
        st.html(f"<style>{f.read()}</style>")


css_file=pathlib.Path("assets/style.css")
load_css(css_file)



about_me = st.Page(

    page="page/aboutme.py",
    default=True,
    icon=":material/home:",
    title="AboutMe",
)


payrec=st.Page(
    page="page/payment_receipt_project.py",
    icon="📑",
    title="PAYMENT RECEIPT PROJECT"

)

project=st.Page(

    page="page/python_project.py",
    icon="📑",
    title="PYTHON PROJECT"
)

oop=st.Page(

    page="page/python_oop.py",
    icon="📑",
    title="PYTHON OOP PROJECT"
)






pg=st.navigation(
    {
        "INFO":[about_me],
        "BASIC PROJECTS":[project],
        "ADVANCE    PYTHON PROJECTS":[oop],
        "STREAMLIT PROJECTS":[payrec]

        }
)


pg.run()

