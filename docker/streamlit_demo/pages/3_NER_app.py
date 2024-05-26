import streamlit as st
from annotated_text import annotated_text

st.set_page_config(
    page_title="NER Visualisation Streamlit App",
    layout="wide"
)

st.title("NER Vizualization Streamlit App")

st.divider()

annotated_text(
    "This ",
    ("is", "Verb"),
    " some ",
    ("annotated", "Adj"),
    ("text", "Noun"),
    " for those of ",
    ("you", "Pronoun"),
    " who ",
    ("like", "Verb"),
    " this sort of ",
    ("thing", "Noun"),
    ". ",
    "And here's a ",
    ("word", ""),
    " with a fancy background but no label.",
)
