import streamlit as st


st.title("Notes")
st.subheader("Add notes and stuff")






css = '''
<style>
    .element-container:has(>.stTextArea), .stTextArea {
        width: 800px !important;
    }
    .stTextArea textarea {
        height: 400px;
    }
</style>
'''

st.text_area("")
#response = st.text_area("Thoughts:")
#st.write(response)
st.write(css, unsafe_allow_html=True)