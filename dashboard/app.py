
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Byte Bankers | Loan Analysis",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Loan Approval Data Exploration")
st.subheader("Byte Bankers | Interactive Analytics Dashboard")

DATA_PATH = Path(__file__).parent.parent / "data" / "india" / "cleaned_loan_dataset.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean loan status values
    df["loan_status"] = (
        df["loan_status"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Clean other text columns
    df["education"] = df["education"].astype(str).str.strip()
    df["self_employed"] = df["self_employed"].astype(str).str.strip()

    return df

df = load_data()

st.sidebar.header("Dashboard Filters")

education = st.sidebar.multiselect(
    "Education",
    options=df["education"].dropna().unique(),
    default=list(df["education"].dropna().unique())
)

employment = st.sidebar.multiselect(
    "Self Employed",
    options=df["self_employed"].dropna().unique(),
    default=list(df["self_employed"].dropna().unique())
)

filtered = df[
    df["education"].isin(education) &
    df["self_employed"].isin(employment)
]

total = len(filtered)
approved = (filtered["loan_status"] == "Approved").sum()
rejected = (filtered["loan_status"] == "Rejected").sum()
rate = approved / total * 100 if total else 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Applicants", f"{total:,}")
c2.metric("Approved", f"{approved:,}")
c3.metric("Rejected", f"{rejected:,}")
c4.metric("Approval Rate", f"{rate:.2f}%")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Loan Approval Distribution")
    fig = px.pie(
        filtered,
        names="loan_status",
        hole=0.45,
        title="Approved vs Rejected"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("CIBIL Score Analysis")
    fig = px.box(
        filtered,
        x="loan_status",
        y="cibil_score",
        color="loan_status",
        title="CIBIL Score by Loan Status"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Annual Income vs Loan Amount")

fig = px.scatter(
    filtered,
    x="income_annum",
    y="loan_amount",
    color="loan_status",
    hover_data=["cibil_score", "education"],
    title="Income and Loan Amount Relationship"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Education-wise Loan Status")

education_data = (
    filtered.groupby(["education", "loan_status"])
    .size()
    .reset_index(name="Applicants")
)

fig = px.bar(
    education_data,
    x="education",
    y="Applicants",
    color="loan_status",
    barmode="group"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Applicant Data")
st.dataframe(filtered, use_container_width=True)

st.caption(
    "Byte Bankers | Academic sample-data analysis. "
    "This dataset is not verified as official RBI data."
)
