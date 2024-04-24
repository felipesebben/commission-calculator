import streamlit as st

st.set_page_config(page_title="Commission Calculator", page_icon=":moneybag:")
st.markdown(
    """
            ## Instructions
            + This app calculates the commission for a given sales amount.
            + Use the sidebar to enter the sales amount.
            + Inform the number of salespeople to calculate the total commission.
                - Possible values are 1 (one people) or 2 (two people).
            + Inform where the commission will be paid.
                - Possible values are 'Brazil' or 'Abroad'.
            + Click on the 'Calculate Commission' button to calculate the commission.
            + The commission will be displayed on the main page.
            """
)
