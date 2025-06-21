# main.py

import streamlit as st
from agents.coordinator_agent import CoordinatorAgent
import os

st.set_page_config(page_title="AutoGen Studio", layout="wide")
st.title("🧠 AutoGen Studio – AI Blog Generator")

# User input
topic = st.text_input("🎯 Enter a blog topic:", placeholder="e.g. Decision Tree in ML")

if st.button("🚀 Generate Content"):
    if topic.strip() == "":
        st.warning("Please enter a valid topic!")
    else:
        with st.spinner("Generating blog, image, SEO and package..."):
            agent = CoordinatorAgent()
            result = agent.run(topic)

        st.subheader("📄 Blog Title Plan")
        st.write(f"**{result['idea']['title']}**")

        st.subheader("📝 Blog Content")
        st.markdown(result['blog'])

        st.subheader("🖼️ AI-Generated Image")
        if os.path.exists(result['image']):
            st.image(result['image'])
        else:
            st.error("Image file not found!")

        st.subheader("📈 SEO Data")
        st.json(result['seo'])

        st.subheader("🧐 Review Summary")
        st.markdown(result['review'])

        st.subheader("📦 Download Package")
        if os.path.exists(result['package']):
            with open(result['package'], "rb") as f:
                st.download_button(
                    label="📥 Download ZIP",
                    data=f,
                    file_name=os.path.basename(result['package']),
                    mime="application/zip"
                )
        else:
            st.error("Package not found!")
