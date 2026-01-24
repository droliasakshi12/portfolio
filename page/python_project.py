import streamlit as st

st.header("Python Project",divider="blue")
    
up7down="https://github.com/droliasakshi12/pythonprojects/blob/main/7%20up%207%20down.py"
dice="https://github.com/droliasakshi12/pythonprojects/blob/main/Dice%20Rolling%20Simulator.py"
password="https://github.com/droliasakshi12/pythonprojects/blob/main/Without%20GUI%20password%20strength%20checker.py"
game="https://github.com/droliasakshi12/pythonprojects/blob/main/snake_and_ladders.py"

st.markdown("**The 7 up 7 down project is build using python language where  the user is suppose to guess wheather it is up, down or exact , if the user guessed it correct they will win the game and vice versa.**",unsafe_allow_html=True)
st.caption("<h5> To view the project  please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="7 UP 7 DOWN",url=up7down,icon="🎰")

st.divider()
st.markdown("**Here in this project you will see the actual presentation of dice which is done using random module where it will generate values between 1 to 6 and accordingly the dice will be shown.**")
st.caption("<h5> To view the project please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="DICE ROLLING SIMULATOR",url=dice,icon="🎲")

st.divider()
st.markdown("**The password strength checker checks the strength of the password wheather the password is strong enough to decode it returns the values[strong,moderate,week] according to the password set by you.**")
st.caption("<h5> To view the project please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="Password Strength Checker",url=password,icon="🔑")

st.divider()
st.markdown("**The snake and ladder game has been played manually and also digitally it is exact game made using python programming language the user has to press roll the dice and the dice will generate random numbers using random module.**")
st.caption("<h5> To view the project please click on the button below !!<h5>",unsafe_allow_html=True)
st.link_button(label="Snake And Ladder Game",url=game,icon="🐍")
   




