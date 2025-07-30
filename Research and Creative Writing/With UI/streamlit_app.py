# streamlit_app.py
import streamlit as st
from crew_pipeline import run_crew
import json
import time

st.set_page_config(page_title="Blog Wizard", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .title-text {
        font-size: 36px;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .sub-text {
        font-size: 18px;
        color: #7f8c8d;
    }
    .result-box {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">🚀 Blog Wizard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Enter a topic to generate a short, engaging blog post using AI agents.</div>', unsafe_allow_html=True)

topic = st.text_input("Enter a topic:", placeholder="e.g., Electric Vehicles in 2025")

if st.button("Generate Blog Summary"):
    if topic.strip() == "":
        st.warning("Please enter a valid topic.")
    else:
        with st.spinner("Running AI agents and writing your blog... ⏳"):
            retries = 3
            for attempt in range(retries):
                try:
                    result = run_crew(topic)
                    break
                except Exception as e:
                    st.error(f"Attempt {attempt + 1} failed with error: {e}")
                    if attempt < retries - 1:
                        time.sleep(5)
                    else:
                        st.error("All attempts failed. Please try again later.")
                        result = None

        if result:
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("✍️ Blog Summary")
            # If result is a dict with "raw" key or similar
            if isinstance(result, dict) and "raw" in result:
                blog_text = result["raw"]
            else:
                blog_text = str(result)

            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("✍️ Blog Summary")
            st.markdown(blog_text)  # Renders markdown correctly
            st.markdown("</div>", unsafe_allow_html=True)
            st.download_button("📥 Download Blog Summary", blog_text, file_name="blog_summary.md")
            st.markdown("</div>", unsafe_allow_html=True)

