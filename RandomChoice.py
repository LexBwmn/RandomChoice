# program that will randomly generate starter coding project ideas 

## BASE PROJECT PROTOTYPE##

#from random import choice

# prototype projects
    # projects = ['Calculator', 'Scheduling Application', 'Cafe Shoppe']
    # print(choice(projects))

import openai
import os

def response_gpt(user_input):
    message = {
        "role": "user",
        "content": user_input
    }

    response = openai.chat.completions.create(
        messages = [message], 
        #model that my chatbot is based off of 
        model = "gpt-4o-mini" 
    )
    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input == ('exit', 'Goodbye', 'Close'):
            print('Chatbot: Goodbye')
        break
    response = response_gpt(user_input)
    print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()

