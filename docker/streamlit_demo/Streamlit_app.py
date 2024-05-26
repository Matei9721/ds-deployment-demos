import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Main Streamlit Demo page",
    layout="wide"
)

st.title("Main Streamlit Demo Page")


# Initialize session state variable if it doesn't exist
if "button_clicks" not in st.session_state:
    st.session_state["button_clicks"] = 0


# Define the callback function
def increment_counter():
    st.session_state["button_clicks"] += 1


# Define the callback function
def reset_counter():
    st.session_state["button_clicks"] = 0


# Add sidebar to the app
with st.sidebar:
    st.markdown("You can use this **sidebar** to **navigate** between your application's **pages** or to **add "
                "buttons** and **configuration menus**.")
    st.divider()

    # Create columns
    col1, col2 = st.columns(2)
    with col1:
        st.button("Click me!", on_click=increment_counter, help="Click this button for the counter to update")

    with col2:
        st.button("Reset!", on_click=reset_counter, help="Click this button to reset the counter")
    st.markdown(f"**The button was clicked {st.session_state['button_clicks']} times!**")

    st.divider()

st.markdown("""
### Welcome to Streamlit!

Streamlit is an open-source Python library that makes it easy to create web apps for machine learning, data science, and more. With Streamlit, you can build interactive and customizable apps using simple Python scripts.

#####  How to use Streamlit:

1. **Install Streamlit**: First, install Streamlit using pip:

``pip install streamlit``

##### Key Features of Streamlit:

- **Easy-to-Use**: Streamlit's simple API allows you to create powerful apps with just a few lines of code.
- **Fast Prototyping**: Iterate quickly on your ideas and instantly see the results as you code.
- **Interactive Widgets**: Build interactive user interfaces with a wide range of widgets for user input and data exploration.
- **Customizable**: Customize the appearance of your app with themes, layout options, and CSS styling.
    - There are some limits to customizing your application with Streamlit which is why it should be used only for simple POCs.
- **Scalable**: Streamlit apps can be deployed on a variety of platforms and can handle large datasets and complex computations.
    - Streamlit can optimize the apps using internal caching mechanisms.

""")

st.subheader("Examples of showing data using Streamlit")

# Define data for the DataFrame
data = {
    'Numbers': [10, 20, 30, 40, 50],
    'Bigger numbers': [100, 200, 300, 400, 500],
    'Fruits': ['apple', 'banana', 'orange', 'grape', 'pineapple'],
    'Animals': ['cat', 'dog', 'rabbit', 'hamster', 'bird'],
    'List column': [['a', 'b', 'c'], ['d', 'e'], ['f'], ['g', 'h', 'i', 'j'], ['k']],
    'Flag': [True, False, True, True, False]
}

st.markdown("##### Displaying a dataframe")
st.dataframe(pd.DataFrame(data), use_container_width=True)

st.markdown("##### Editing a dataframe")
st.data_editor(pd.DataFrame(data), use_container_width=True)

st.markdown("##### Visualize line charts")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

st.markdown("##### Visualize points on a map")
df = pd.DataFrame(
    [[52.3676, 4.9041]],
    columns=['lat', 'lon'])

st.map(df)


