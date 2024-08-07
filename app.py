import streamlit as st
import math

st.title("Attendance")

# User inputs for number of classes held and attended
classs = st.number_input("Number of classes held", value=0, step=1, format="%d")
atten = st.number_input("Number of classes attended", value=0, step=1, format="%d")

# User selects the required attendance percentage
min_p = st.selectbox("Required attendance percentage:", ['65%', '70%', '75%', '80%'])
percent = int(min_p[:2])

# Calculate required classes to meet the desired attendance percentage
if classs > 0:
    min_75 = math.ceil(classs * 0.01 * percent)
    req = min_75 - atten
    remaining = classs - atten
    bunks = remaining - req

if st.button('Check attendance'):
    if atten > classs:
        st.error("Classes held should be more than the classes attended.")
    elif classs == 0:
        st.error("Number of classes held cannot be 0.")
    else:
        max_percen = ((atten + remaining) / classs) * 100
        max_percen = round(max_percen, 2)
        current_percen = (atten / classs) * 100
        current_percen = round(current_percen, 2)
        if atten >= min_75:
            st.success(f"Attendance: {current_percen}%")
            st.info(f"Classes needed to attend to maintain {percent}% attendance: 0")
        elif req > remaining:
            st.error(f"Cannot reach {percent}% even if all remaining classes are attended.")
        else:
            st.success(f"Attendance: {current_percen}%")
            st.info(f"Classes needed to maintain {percent}% attendance: {min_75 - atten}")

footer = """
<style>
.footer {
    position: relative;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: var(--footer-background-color);
    color: var(--footer-text-color);
    text-align: center;
    padding: 10px;
    margin-top: 20px;
}
@media (prefers-color-scheme: dark) {
    :root {
        --footer-background-color: #333;
        --footer-text-color: #f1f1f1;
    }
}
@media (prefers-color-scheme: light) {
    :root {
        --footer-background-color: #f1f1f1;
        --footer-text-color: #333;
    }
}
</style>
<div class="footer">
    <p>Developed by Sowmya Devalla</p>
    <p>Contact: 245122750006@vce.edu.in</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
