# chatbot.py

# Predefined Q&A pairs
bank_qa = {
    "what is a savings account": "A savings account is a deposit account that earns interest over time.",
    "how can i apply for a loan": "You can apply for a loan by visiting our branch or applying online on our website.",
    "what documents do i need to apply for a loan": "You need your ID proof, income proof, and address proof to apply for a loan.",
    "what is the interest rate on home loans": "The current interest rate on home loans is 7.5% per annum.",
    "what are your working hours": "Our working hours are from 9 AM to 5 PM, Monday to Friday.",
    "how do i check my account balance": "You can check your account balance using our mobile app, online banking, or by visiting the branch.",
    "can i open a fixed deposit account": "Yes, you can open a fixed deposit account with us with attractive interest rates.",
    "what is the minimum balance required for a savings account": "The minimum balance required is Rs. 1000 in a savings account."
}


def get_chat_response(user_input):
    query = user_input.strip().lower()
    for question in bank_qa:
        if question in query:
            return bank_qa[question]
    return "I'm sorry, I don't have an answer for that. Please contact customer support."


# Chat loop (for testing)
if __name__ == "__main__":
    print("BankBot is ready to chat! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("BankBot: Goodbye!")
            break
        response = get_chat_response(user_input)
        print("BankBot:", response)
