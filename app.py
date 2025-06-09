import streamlit as st
# from src.models.predict import load_model, predict_and_explain
# from chatbot import get_chat_response

st.set_page_config(page_title="AI Loan Assistant", layout="centered")

# Load model once
# @st.cache_resource
# def get_model():
#     return load_model("best_model.pkl")

# model = get_model()

st.title("💸 AI Loan & Investment Assistant")

# Create 4 tabs
loan_tab, invest_tab, emi_tab, chatbot_tab = st.tabs([
    "🏦 Loan Approval Predictor", 
    "📈 Investment Calculator", 
    "📊 EMI Calculator",
    "🤖 Chat with BankBot"
])

# ------------------- TAB 1: Loan Prediction -------------------
# with loan_tab:
#     st.header("🏦 Loan Approval Predictor")

#     with st.form("loan_form"):
#         col1, col2 = st.columns(2)

#         with col1:
#             income_annum = st.number_input("Annual Income (₹)", value=500000, step=10000, key="income")
#             loan_amount = st.number_input("Loan Amount (₹)", value=1000000, step=10000, key="loan_amt")
#             loan_term = st.number_input("Loan Term (in months)", value=120, step=12, key="term")
#             cibil_score = st.number_input("CIBIL Score", value=700, step=10, key="cibil")

#         with col2:
#             no_of_dependents = st.number_input("Number of Dependents", value=0, step=1, key="deps")
#             residential_assets_value = st.number_input("Residential Asset Value (₹)", value=500000, step=10000, key="res")
#             commercial_assets_value = st.number_input("Commercial Asset Value (₹)", value=0, step=10000, key="com")
#             luxury_assets_value = st.number_input("Luxury Asset Value (₹)", value=0, step=10000, key="lux")
#             bank_asset_value = st.number_input("Bank Balance (₹)", value=100000, step=10000, key="bank")

#         col3, col4 = st.columns(2)
#         with col3:
#             education = st.selectbox("Education", ["Graduate", "Not Graduate"])
#         with col4:
#             self_employed = st.selectbox("Self Employed?", ["No", "Yes"])

#         submitted = st.form_submit_button("🔍 Predict Loan Approval")

#         if submitted:
#             input_data = {
#                 "no_of_dependents": no_of_dependents,
#                 "income_annum": income_annum,
#                 "loan_amount": loan_amount,
#                 "loan_term": loan_term,
#                 "cibil_score": cibil_score,
#                 "residential_assets_value": residential_assets_value,
#                 "commercial_assets_value": commercial_assets_value,
#                 "luxury_assets_value": luxury_assets_value,
#                 "bank_asset_value": bank_asset_value,
#                 "education_ Not Graduate": 1 if education == "Not Graduate" else 0,
#                 "self_employed_ Yes": 1 if self_employed == "Yes" else 0
#             }

#             result = predict_and_explain(model, input_data)

#             if result["prediction"] == 1:
#                 st.success("✅ Loan Approved!")
#             else:
#                 st.error("❌ Loan Rejected.")

#             st.info(f"📊 Risk Level: **{result['risk']}**")

# ------------------- TAB 2: Investment Calculator -------------------
with invest_tab:
    st.header("📈 Investment Calculator")

    principal = st.number_input("Initial Investment (₹)", value=100000, step=1000, key="inv_principal")
    rate = st.number_input("Annual Interest Rate (%)", value=7.0, step=0.1, key="inv_rate")
    years = st.number_input("Investment Duration (Years)", value=10, step=1, key="inv_years")

    if st.button("💹 Calculate Future Value"):
        future_value = principal * (1 + rate/100) ** years
        st.success(f"📌 Future Value: ₹{future_value:,.2f}")

# ------------------- TAB 3: Loan EMI Calculator -------------------
with emi_tab:
    st.header("📊 EMI Calculator")

    loan_amt = st.number_input("Loan Amount (₹)", value=1000000, step=10000, key="emi_loan_amt")
    annual_rate = st.number_input("Annual Interest Rate (%)", value=8.0, step=0.1, key="emi_rate")
    tenure_months = st.number_input("Loan Tenure (in months)", value=120, step=12, key="emi_tenure")

    if st.button("📅 Calculate EMI"):
        r = annual_rate / 12 / 100
        t = tenure_months
        emi = (loan_amt * r * (1 + r) ** t) / ((1 + r) ** t - 1)
        st.success(f"📌 Monthly EMI: ₹{emi:,.2f}")

# ------------------- TAB 4: Chatbot -------------------
# with chatbot_tab:
#     st.header("🤖 Chat with BankBot")
#     user_input = st.text_input("You:")
#     if user_input:
#         response = get_chat_response(user_input)
#         st.markdown(f"**BankBot:** {response}")
