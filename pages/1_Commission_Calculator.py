import streamlit as st
from modules.calculator import CommissionCalculator
from config.config_loader import load_config
from dotenv import load_dotenv
import pandas as pd

load_dotenv(".env.dev")

if "reset" not in st.session_state:
    st.session_state.reset = False

st.set_page_config(page_title="Commission Calculator", page_icon=":moneybag:")


config = load_config("COMMISSION_CONFIG")["commission_rates"]

# Create show/hide instructions
with st.expander("Show Instructions", expanded=False):
    st.markdown(
        """
                ### Instructions ###
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

sales_amount = st.sidebar.number_input(
    "Enter the **sales** amount (USD)", min_value=0.0, step=100.0
)
n_salespeople = st.sidebar.radio(
    "Select the **number of salespeople**", options=list(config.keys())
)
location = st.sidebar.selectbox(
    "Select the location", options=list(config[n_salespeople].keys())
)

if st.sidebar.button("Calculate Commission"):
    calculator = CommissionCalculator(sales_amount, int(n_salespeople), location)
    commission = calculator.calculate_commission()

    # Create a Dataframe with the results
    results = pd.DataFrame(
        {
            "Sales amount": [f"${sales_amount:.2f}"],
            "Number of salespeople": [n_salespeople],
            "Location": [location],
            "Commission rate": [f"{calculator.get_commission_rate() * 100:.2f}%"],
            "Estimated commission": [f"${commission:.2f}"],
        }
    )
    # Transpose the results
    results = results.T

    # Rename the column
    results = results.rename(columns={0: "Results"})

    results = results.style.apply(
        lambda x: [
            "background: blue" if x.name == "Estimated commission" else "" for i in x
        ],
        axis=1,
    )
    if results is not None:
        st.sidebar.success("The commission was calculated successfully!")
    st.table(results)

    # st.write(
    #     f"""
    #     ## Results: ##
    #     - Sales amount:
    #         ${sales_amount:.2f}
    #     - Number of salespeople:
    #         {n_salespeople}
    #     - Location: {location}
    #     - Commission rate: {calculator.get_commission_rate() * 100:.2f}%
    #     - Estimated commission:
    #         ## ${commission:.2f} ##
    #     """
    # )


if st.sidebar.button("Reset"):
    st.session_state.reset = True
    st.rerun()
else:
    st.session_state.reset = False
