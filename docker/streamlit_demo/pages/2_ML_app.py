import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="ML Streamlit App",
    layout="wide"
)

st.title("ML Streamlit App")


# Create pipeline and cache it so it doesn't load every page reload
@st.cache_resource()
def get_sentiment_analysis_pipeline(model_name: str = "bhadresh-savani/electra-base-emotion"):
    pipe = pipeline(task="text-classification", model=model_name, return_all_scores=True)

    return pipe


with st.spinner("Downloading Model from HuggingFace Repository"):
    ml_pipeline = get_sentiment_analysis_pipeline()

user_input = st.text_input("Enter a sentence", help="Write any sentence to be inferenced using"
                                                    " bhadresh-savani/electra-base-emotion model from HF.")

if user_input:
    with st.status("Processing sentence using Transformer model", expanded=True) as status:
        st.markdown("Running Transformer pipeline!")
        pipeline_output = ml_pipeline(user_input)
        status.update(label="Inference complete!", state="complete")

    st.write(pipeline_output)
