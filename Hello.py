import base64
import streamlit as st
from streamlit.logger import get_logger
import pandas as pd

LOGGER = get_logger(__name__)

def load_custom_css():
    css = """
    <style>
        /* Target the grid layout of Streamlit columns directly */
        .st-cd {
            gap: 20px; /* Adjust the gap between columns */
        }
        /* Adjustments for all images in the columns */
        .stImage img {
            width: 100%; /* Makes images responsive within the column width */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def run():
    st.set_page_config(page_title="NYU-MOT-CDW", page_icon="👋")
    load_custom_css() 
    st.write("# Welcome to 2024 CDW Project! 👋")
    st.markdown("""
    ### Project Introduction
    This website, as the final phase of the capstone project, will contain all deliverables of the project and serve as a publicly accessible site for displaying maps.
    
    In this web application, based on the Streamlit framework, the team developed an interactive dashboard to visualize CDW flows in a variety of graphical views. This tool is useful in policy development for CDW recycling and reuse, providing insight into annual flow trends by material type, transaction, and destination, potentially facilitating a more sustainable approach to CDW management.
    
    This project is part of a long-term collaboration between New York University (NYU) and the New York City Department of Design and Construction (DDC). This collaboration is embodied in the Town+Gown platform, a city-wide applied research platform designed to connect practitioners, including New York City organizations, with academics. Through this platform, students in NYU's Master of Science in Technology Management and Innovation program are able to engage in real-world research on urban problems and provide innovative solutions.
    ### How to use this web?
    """)
    st.markdown("""<iframe width="800" height="450" src="https://cdn.pixabay.com/video/2016/12/31/6962-197634410_large.mp4" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
                """, unsafe_allow_html=True)
    st.title('About Us')
    team_members = [
        {"name": "Yanfeng Xu", "role": "JIRA", "linkedin": "https://www.linkedin.com/in/yanfeng-xu-734698239/", "email": "yx3104@nyu.edu", "image_path": "path_to_xu.jpg"},
        {"name": "Tianyi Wu", "role": "Email Communication", "linkedin": "https://www.linkedin.com/in/tianyi-wu-b558a51a3/", "email": "tw2709@nyu.edu", "image_path": "path_to_yi.jpg"},
        {"name": "Ruoan Ni", "role": "Meeting Notes", "linkedin": "https://www.linkedin.com/in/ruoan-ni-97815424b/", "email": "rn2429@nyu.edu", "image_path": "path_to_mao.jpg"},
        {"name": "Rui Xue", "role": "Meeting Moderator", "linkedin": "https://www.linkedin.com/in/rui-xue-b854731a4/", "email": "rx2161@nyu.edu", "image_path": "path_to_rui.jpg"}
    ]

    cols = st.columns(4)
    for i, member in enumerate(team_members):
        with cols[i]:
            st.image(member["image_path"], use_column_width=True)
            st.write(member["name"])
            st.write(member["role"])

    df = pd.DataFrame(team_members)
    def make_clickable(link, text):
        return f'<a target="_blank" href="{link}">{text}</a>'

    df['linkedin'] = df.apply(lambda x: make_clickable(x['linkedin'], 'LinkedIn'), axis=1)
    df['email'] = df.apply(lambda x: make_clickable(f"mailto:{x['email']}", x['email']), axis=1)
    df = df[['name', 'role', 'email', 'linkedin']]
    st.title("Connect with us")
    st.write("If you have any problems, please connect with us!")
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

    st.markIt appears that the paths to the images you're trying to load into your Streamlit application are incorrect, or the files are not accessible from the specified paths. You need to ensure that the paths you've specified for your image files are correct and accessible by the Streamlit server. Here's how you can correct the paths in your code:

1. Verify the correct paths to your images. Make sure they exist in the specified location.
2. If you're running the app locally, ensure that the paths are relative to the script or use absolute paths.
3. If the app is hosted, ensure that the server has access to the file paths and that they are included in your deployment.

Here is an example of how you might specify a path to an image if the images are stored in a directory called `images` in the same directory as your script:

```python
    team_members = [
        {"name": "Yanfeng Xu", "role": "JIRA", "linkedin": "https://www.linkedin.com/in/yanfeng-xu-734698239/", "email": "yx3104@nyu.edu", "image_path": "./images/xu.jpg"},
        {"name": "Tianyi Wu", "role": "Email Communication", "linkedin": "https://www.linkedin.com/in/tianyi-wu-b558a51a3/", "email": "tw2709@nyu.edu", "image_path": "./images/yi.jpg"},
        {"name": "Ruoan Ni", "role": "Meeting Notes", "linkedin": "https://www.linkedin.com/in/ruoan-ni-97815424b/", "email": "rn2429@nyu.edu", "image_path": "./images/mao.jpg"},
        {"name": "Rui Xue", "role": "Meeting Moderator", "linkedin": "https://www.linkedin.com/in/rui-xue-b854731a4/", "email": "rx2161@nyu.edu", "image_path": "./images/rui.jpg"}
    ]


