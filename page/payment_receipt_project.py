import streamlit as st 

st.header("WELCOME TO OUR STORE :) ",divider="blue")
st.subheader("PLEASE FILL YOUR DETAILS BELOW ")

class payment_receipt:
    def info(self,c_name,amount,pay_method):
        self.c_name=c_name
        self.amount=amount
        self.pay_method=pay_method

    def generate_receipt(self):
        r=(f"""
        HERE IS YOUR BILL :
        -----------------------------
         CUSTOMER NAME :{self.c_name}

         TOTAL AMOUNT : ${self.amount:2f}

         PAYMENT METHOD: {self.pay_method}
        
        ---------------------------------

        THANK YOU! VISIT AGAIN .........  

        """)
        return r 
      
    

    
obj=payment_receipt()

n=st.text_input("CUSTOMER NAME:")
a=st.number_input("AMOUNT:")
m=st.text_input("PAYMENT METHOD:")

obj.info(n,a,m)
z=obj.generate_receipt()
st.write(z)