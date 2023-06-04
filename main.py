import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)


with col2:
    st.title("Shubham Biswas")
    content = """
    Hello world, My name is Shubham, I am a front-end developer. I am pursuing my major in Data Science. And currently I am learning different tools of DevOps. I am based out of Kolkata, India. Besides tech, I love to play chess and listening to music.
    """
    st.info(content)
