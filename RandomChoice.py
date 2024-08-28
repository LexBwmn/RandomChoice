# program that will randomly generate starter coding project ideas 

## BASE PROJECT PROTOTYPE##

#from random import choice

# prototype projects
    # projects = ['Calculator', 'Scheduling Application', 'Cafe Shoppe']
    # print(choice(projects))

import openai
import os

#model that my chatbot is based off of 
model = "gpt-4o-mini"


def cont(messages, projects=0):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        projects=projects,
    )
    return response.choices[0].message.content

