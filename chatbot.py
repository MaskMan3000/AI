"""
pip install chatterbot
pip install chatterbot_corpus
python -m spacy download en_core_web_sm

"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Step A: Create chatbot instance
chatbot = ChatBot('SupportBot')

# Step B: Train with corpus data
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

# Step C: Train with custom FAQ list for customer support
faq = [
    "Hi",
    "Hello! Welcome to Customer Support.",
    "What services do you offer?",
    "We offer product support, order tracking, and return assistance.",
    "How can I track my order?",
    "You can track your order using the tracking number sent to your email.",
    "What is your return policy?",
    "We accept returns within 30 days of delivery.",
    "Can I speak to a human?",
    "Our support staff is available from 9 AM to 5 PM, Monday to Friday.",
    "Thank you",
    "You're welcome!",
    "Bye",
    "Have a great day!"
]

list_trainer = ListTrainer(chatbot)
list_trainer.train(faq)

# Step D: User interaction
print("SupportBot: Hello! I'm your virtual assistant. Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "stop", "bye"]:
        print("SupportBot: Thank you for chatting with us. Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("SupportBot:", response)





















"""
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer 
from chatterbot.trainers import ListTrainer 

bot = ChatBot('Bot') 

trainer = ListTrainer(bot) 

trainer.train([ 
	'Hi', 
	'Hello', 
	'I need roadmap for Competitive Programming', 
	'Just create an account on GFG and start', 
	'I have a query.', 
	'Please elaborate, your concern', 
	'How long it will take to become expert in Coding ?', 
	'It usually depends on the amount of practice.', 
	'Ok Thanks', 
	'No Problem! Have a Good Day!'
]) 

while True: 
	request=input('you :') 
	if request == 'OK' or request == 'ok': 
		print('Bot: bye') 
		break
	else: 
		response=bot.get_response(request) 
		print('Bot:', response) 
 
"""
