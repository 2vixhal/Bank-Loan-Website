from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
chatbot = ChatBot('BankBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Bank-related questions and answers for training
bank_qa = [
    "What is a savings account?",
    "A savings account is a deposit account that earns interest over time.",
    
    "How can I apply for a loan?",
    "You can apply for a loan by visiting our branch or applying online on our website.",
    
    "What documents do I need to apply for a loan?",
    "You need your ID proof, income proof, and address proof to apply for a loan.",
    
    "What is the interest rate on home loans?",
    "The current interest rate on home loans is 7.5% per annum.",
    
    "What are your working hours?",
    "Our working hours are from 9 AM to 5 PM, Monday to Friday.",
    
    "How do I check my account balance?",
    "You can check your account balance using our mobile app, online banking, or by visiting the branch.",
    
    "Can I open a fixed deposit account?",
    "Yes, you can open a fixed deposit account with us with attractive interest rates.",
    
    "What is the minimum balance required for a savings account?",
    "The minimum balance required is Rs. 1000 in a savings account."
]

# Train the chatbot with the bank Q&A
trainer.train(bank_qa)

print("BankBot is ready to chat! Type 'exit' to quit.")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("BankBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("BankBot:", response)
