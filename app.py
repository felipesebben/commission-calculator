import streamlit as st


def main():
    """Run this function to display the Streamlit app."""
    st.set_page_config(page_title="Main Page", page_icon=":house:")
    st.write("This app calculates the commission for a given sales amount.")

    st.sidebar.subheader("User Input")


if __name__ == "__main__":
    main()
