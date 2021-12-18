import streamlit as st
import pandas as  pd
import numpy as np

st.set_page_config(layout="wide")
st.title("Pruhfessional Enjuneer")

st.subheader("Congragulations! If you are reading this, then you are officially a Pruhfessional Enjuneer $^{TM}$")
st.write("")
st.write("Note: This does not reflect any qualifications past, present, or future relating to licensure as a")
st.write("Professional Engineer, as such a designation would be generally frowned upon and probably illegal.")
st.write("")
st.write("Below is an assortment of tools esigned to aid you on your quest as you pursue a career as a Prufessional Engineer")
st.write("")

#
# Pi Calculator
#
st.subheader("Calculations involving $\pi$ ")


st.write("$\pi$ is an irrational, nonterminating, non repeating mathematical constant that frequently arises in standard enjumeineering calculation ")
st.write("To perform sensitivity analyses, one must be able to quickly and accurately determine the value of $\pi$ to an arbitrary precision...")
st.write("")

st.write("")
st.number_input("enter number of decimals to calculate",0,10000000)


pi_button = st.button("CALCULATE")
if pi_button  == True:
	st.latex("\pi\ = 3.14")


st.write("")

st.latex("SIN( theta )\ Estimation")

st.write("In your day to day activities, you may also need to calculate the value of sin(theta). ")
st.header( "FEAR NOT!")

theta = st.number_input("enter theta",0,10000000)
theta_button = st.button("CALCULATE SIN(THETA)")
if theta_button == True:
	st.write("sin(theta) = ", theta)


st.write("")


st.subheader("Checking Safety Factors")

st.write("Employing sufficient safety factors is critical for ensuring structural integrity and continuous employment.")
st.write("Select your use case and expected force limit and this app will calculate the required safety factor")

from random import random


st.write("")

problem = st.selectbox('Select a use case', ['Truss Bridge','Steel Beams', 'Steel Memes','that one weird ass example from that one class that was actually kind of interesting but not in the least bit practical'])
force = st.number_input("force expected ( in femtoNewtons)",0,10000000)
force_button = st.button("Estimate Force Button!")
if force_button == True:
	force_number = force*(random()-.5)*1000000
	st.write("Recommended Safety Factor = ", force_number)



st.write("")

st.subheader("Handy Dandy Inequalities")

st.write("Out in the field, it can sometimes be necessary to make estimations to establish boundary conditions")
st.write("Below are some useful inequalities to aid you in making quick-and-dirty estimations out in the field")
st.write("")
st.latex(r''' \$(python) < \$(MATLAB)  ''')
st.latex(r''' 2^{python} > 2^{MATLAB}  ''')
st.write("(power set of python is greater than the power set of MATLAB)")
st.latex(r''' python > MATLAB ''')




st.write("")

st.subheader("Decision Matrixing")

st.write("Remember, when you are faced with a difficult decision, tabularizing your data into a decision matrix can help lead the way")
st.write("")
st.write("Take, for example this decision matrix to determine which humanities courses to take. (in megafucks given)")

st.write("")


zero_array = np.zeros((100,100))
zero_df = pd.DataFrame(zero_array)
st.dataframe(zero_df)





############
############
#Right about now... video
############
############
