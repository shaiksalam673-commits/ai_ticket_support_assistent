import streamlit as st

from src.data_loader import load_data
from src.query_engine import run_query
from src.anomaly_detector import detect_anomalies

st.set_page_config(
    page_title="AI Support Ticket Assistant",
    layout="wide"
)

df = load_data()

st.title("AI Support Ticket Assistant")

tab1, tab2, tab3 = st.tabs(
    ["Dataset", "Ask Questions", "Anomalies"]
)


with tab1:

    st.subheader("Dataset Preview")

    st.dataframe(df.head(20))


with tab2:

    question = st.text_input(
        "Ask a question"
    )

    if st.button("Submit"):

        result = run_query(
            question,
            df
        )

        st.write(result)

with tab3:

    anomalies = detect_anomalies(df)

    st.subheader(
        "Critical Unresolved Tickets"
    )

    st.dataframe(
        anomalies["critical_unresolved"]
    )

    st.subheader(
        "Long Resolution Times"
    )

    st.dataframe(
        anomalies["long_resolution"]
    )

    st.subheader(
        "Low Customer Ratings"
    )

    st.dataframe(
        anomalies["low_ratings"]
    )