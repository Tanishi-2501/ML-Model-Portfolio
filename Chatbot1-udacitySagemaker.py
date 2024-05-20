#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define a dictionary with predefined responses
responses = {
    "hi": "Hello there! How can I assist you today?",
    "how are you": "I'm a bot, so I don't have feelings, but I'm functioning properly!",
    "i am happy": "That's so great to hear.! What is the reason for this happiness?",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure, I can help you. What do you need assistance with?",
}


# In[ ]:


# Function to get the bot response
def get_bot_response(user_input):
    # Make the input lowercase to match the dictionary keys
    user_input = user_input.lower()

    # Return the matching response if it exists, otherwise return a default response
    return responses.get(user_input, "I'm not sure how to respond to that. Can you try asking something else?")


# In[ ]:


# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = get_bot_response(user_input)
    print(f"Bot: {response}")







