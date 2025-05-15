import streamlit as st
import re

# Set page config
st.set_page_config(page_title="Loan Chatbot", page_icon="🤖")

# Title and subtitle
st.markdown("""
    <h1 style='text-align: center;'>🤖 Loan Assistant Chatbot</h1>
    <p style='text-align: center;'>Ask me anything about loans terms</p>
""", unsafe_allow_html=True)

# Predefined chatbot responses
responses = {
    "what is emi": "EMI stands for Equated Monthly Installment — the fixed payment made by a borrower every month.",
    "how is emi calculated": "EMI = [P x R x (1+R)^N]/[(1+R)^N - 1], where P = loan amount, R = monthly interest rate, N = number of months.",
    "what is tenure": "Tenure refers to the total duration (in months or years) of the loan.",
    "what is interest rate": "It is the percentage of loan amount charged by the lender for borrowing money.",
    "what is collateral": "Collateral is an asset pledged by the borrower to secure the loan.",
    "what is a secured loan": "A secured loan is backed by collateral, such as property or assets, which the lender can claim if you default.",
    "what is an unsecured loan": "An unsecured loan does not require any collateral and is given based on creditworthiness.",
    "what is a credit score": "A credit score is a number that represents your creditworthiness. Higher scores improve your chances of loan approval.",
    "what is loan default": "Loan default occurs when a borrower fails to repay the loan as agreed.",
    "what is prepayment": "Prepayment means paying off your loan before the scheduled tenure, either partially or fully.",
    "what is processing fee": "Processing fee is a one-time charge by the lender to process your loan application.",
    "what is foreclosure": "Foreclosure is the full repayment of the outstanding loan before the end of the tenure, closing the loan.",
    "what is a fixed interest loan": "A fixed interest loan has an interest rate that remains constant throughout the loan tenure.",
    "what is a floating interest loan": "A floating interest loan has an interest rate that varies with market conditions.",
    "what is a moratorium period": "The moratorium period is a break period where you don't have to make EMI payments, usually offered at the beginning of the loan.",
    "what is loan disbursement": "Loan disbursement is the process by which the lender releases the loan amount to the borrower.",
    "what is a loan sanction letter": "A loan sanction letter is a document issued by the bank confirming the approval of your loan and terms.",
    "what is a loan agreement": "A loan agreement is a legally binding document that outlines terms and conditions of the loan.",
    "what is creditworthiness": "Creditworthiness is an assessment of your ability to repay a loan, based on credit score, income, and history.",
    "what is a co-applicant": "A co-applicant is another person who applies for the loan with you and shares responsibility for repayment.",
    "what is a guarantor": "A guarantor is someone who guarantees loan repayment if the primary borrower fails to pay.",
    "what is loan refinancing": "Loan refinancing means replacing your existing loan with a new one, usually to get a better interest rate.",
    "what is top-up loan": "A top-up loan is an additional loan amount given on your existing loan.",
    "what is loan to value ratio": "Loan to Value (LTV) ratio is the percentage of the asset value that the lender is willing to finance.",
    "what is loan principal": "Loan principal is the original amount borrowed before adding interest or fees.",
    "what is overdue amount": "The overdue amount is the EMI that was not paid by the due date.",
    "what is bounce charge": "A bounce charge is a penalty for failed EMI payment due to insufficient funds.",
    "what is pre-closure charge": "A pre-closure charge is a fee charged if you pay off your loan earlier than scheduled.",
    "what is dti ratio": "Debt-to-Income (DTI) ratio compares your monthly debt payments to your monthly income.",
    "what is repo rate": "Repo rate is the rate at which RBI lends money to banks, affecting interest rates.",
    "what is cibil score": "CIBIL score is a credit score provided by TransUnion CIBIL that ranges from 300 to 900.",
    "what is personal loan": "A personal loan is an unsecured loan taken for personal use, like medical or travel expenses.",
    "what is home loan": "A home loan is a secured loan used to purchase residential property.",
    "what is car loan": "A car loan is a secured loan taken to finance the purchase of a car.",
    "what is education loan": "An education loan helps students fund tuition, living expenses, and education-related costs.",
    "what is business loan": "A business loan is offered to companies or individuals to support business operations or growth.",
    "what is gold loan": "A gold loan is a secured loan taken by pledging gold as collateral.",
    "what is balance transfer": "Balance transfer is moving your loan from one lender to another for better interest rates.",
    "what is npa": "NPA (Non-Performing Asset) is a loan where the borrower has stopped making repayments for 90+ days.",
    "what is emi bounce": "An EMI bounce occurs when your bank account doesn't have enough funds to cover the EMI.",
    "what is part payment": "Part payment is a lump sum payment made to reduce the loan principal during the loan tenure.",
    "what is emi due date": "EMI due date is the date by which your monthly installment must be paid.",
    "what is standing instruction": "Standing instruction is an automated payment setup where EMI is debited monthly from your account.",
    "what is disbursal date": "Disbursal date is the date on which the loan amount is credited to your account.",
    "what is default date": "Default date is when the borrower officially fails to make the scheduled loan payments.",
    "what is loan tenure extension": "Loan tenure extension is an agreement to extend the duration of your loan repayment period.",
    "what is rescheduling of loan": "Loan rescheduling is a change in the loan’s EMI amount or repayment duration due to financial hardship.",
    "what is underwriter": "An underwriter is a professional who evaluates your loan application and assesses the risk for the lender.",
    "what is sanction amount": "Sanction amount is the approved amount of loan you are eligible to receive after evaluation.",
    "what is emi calendar": "EMI calendar is a schedule showing the due dates and amounts for your upcoming loan installments."
}


# Function to clean user input
def clean_input(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)     # Normalize spaces
    return text

# Initialize message history with greeting
if "messages" not in st.session_state:
    st.session_state.messages = [
        ("bot", "Hello! I’m your Loan Assistant. You can ask me anything about loans terms")
    ]

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="Ask a loan question...", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

# Handle message logic
if submitted and user_input:
    user_msg = user_input.strip()
    cleaned_input = clean_input(user_msg)

    response = responses.get(cleaned_input, "I'm sorry, I can only answer predefined questions about loan terms right now.")
    
    st.session_state.messages.append(("user", user_msg))
    st.session_state.messages.append(("bot", response))

# Message bubble display (chat-like)
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.markdown(
            f"<div style='background-color:#d1f7c4;padding:10px 15px;border-radius:12px;margin:5px 0;text-align:right;color:#000'><b>You:</b> {msg}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#e4e4ff;padding:10px 15px;border-radius:12px;margin:5px 0;text-align:left;color:#000'><b>Bot:</b> {msg}</div>",
            unsafe_allow_html=True
        )

