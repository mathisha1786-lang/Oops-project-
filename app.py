import streamlit as st

st.title("Calculator")

# store expression
if "exp" not in st.session_state:
    st.session_state.exp = ""

# display
st.text_input("Display", st.session_state.exp, disabled=True)

def press(val):
    st.session_state.exp += str(val)

def clear():
    st.session_state.exp = ""

def calculate():
    try:
        st.session_state.exp = str(eval(st.session_state.exp))
    except:
        st.session_state.exp = "Error"

# calculator buttons
buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"]
]

for row in buttons:
    cols = st.columns(4, gap="small")
    for i, val in enumerate(row):
        if val == "=":
            if cols[i].button(val, use_container_width=True):
                calculate()
        else:
            if cols[i].button(val, use_container_width=True):
                press(val)

st.button("Clear", use_container_width=True, on_click=clear)
 