import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(
    page_title="Talking Rabbitt",
    page_icon="🐰",
    layout="wide"
)

px.defaults.template = "plotly_white"

st.title("🐰 Talking Rabbitt")
st.markdown("Ask questions about your sales data in natural language.")

# st.markdown("### Example Questions")
# st.markdown("""
# - Which region generated the highest revenue?
# - Show revenue trend over time
# - Show revenue distribution by region
# - Compare revenue by region
# """)

# Sidebar
st.sidebar.header("Upload Data")

file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def detect_chart(question):

    q = question.lower()

    if "trend" in q or "over time" in q or "date" in q:
        return "line"

    if "distribution" in q or "percentage" in q:
        return "pie"

    if "compare" in q or "highest" in q or "by region" in q or "by product" in q:
        return "bar"

    return "bar"


if file:

    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.divider()

    # Show chat history
    for chat in st.session_state.chat_history:

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):

            st.write(chat["answer"])

            chart_type = chat["chart_type"]

            if chart_type == "bar":

                if "region" in df.columns and "revenue" in df.columns:

                    data = df.groupby("region")["revenue"].sum().reset_index()

                    fig = px.bar(
                        data,
                        x="region",
                        y="revenue",
                        color="region",
                        title="Revenue by Region"
                    )

                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "line":

                if "date" in df.columns and "revenue" in df.columns:

                    df["date"] = pd.to_datetime(df["date"])

                    data = df.groupby("date")["revenue"].sum().reset_index()

                    fig = px.line(
                        data,
                        x="date",
                        y="revenue",
                        markers=True,
                        title="Revenue Trend Over Time"
                    )

                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "pie":

                if "region" in df.columns and "revenue" in df.columns:

                    data = df.groupby("region")["revenue"].sum().reset_index()

                    fig = px.pie(
                        data,
                        values="revenue",
                        names="region",
                        title="Revenue Distribution"
                    )

                    st.plotly_chart(fig, use_container_width=True)

    # User input
    question = st.chat_input("Ask a question about your data")

    if question:

        with st.chat_message("user"):
            st.write(question)

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={
                "question": question,
                "data": df.to_dict(orient="records")
            }
        )

        answer = response.json()["answer"]

        chart_type = detect_chart(question)

        with st.chat_message("assistant"):

            st.write(answer)

            if chart_type == "bar":

                if "region" in df.columns and "revenue" in df.columns:

                    data = df.groupby("region")["revenue"].sum().reset_index()

                    fig = px.bar(
                        data,
                        x="region",
                        y="revenue",
                        color="region",
                        title="Revenue by Region"
                    )

                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "line":

                if "date" in df.columns and "revenue" in df.columns:

                    df["date"] = pd.to_datetime(df["date"])

                    data = df.groupby("date")["revenue"].sum().reset_index()

                    fig = px.line(
                        data,
                        x="date",
                        y="revenue",
                        markers=True,
                        title="Revenue Trend Over Time"
                    )

                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "pie":

                if "region" in df.columns and "revenue" in df.columns:

                    data = df.groupby("region")["revenue"].sum().reset_index()

                    fig = px.pie(
                        data,
                        values="revenue",
                        names="region",
                        title="Revenue Distribution"
                    )

                    st.plotly_chart(fig, use_container_width=True)

        # Save conversation with chart type
        st.session_state.chat_history.append({
            "question": question,
            "answer": answer,
            "chart_type": chart_type
        })

else:

    st.info("Upload a CSV file from the sidebar to begin.")