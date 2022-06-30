# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 17:06:46 2022

@author: Anujan
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(name='trivially egor', read_only=False, 
              logic_adapters=['chatterbot.logic.MathematicalEvaluation', 
                              'chatterbot.logic.BestMatch'])

trivial = ["Hi, can I be of assistance?",
           "I need some maths help",
           "That is trivial",
           "What is your name?",
           "Trivially Egor",
           "What's your favourite drink?",
           "Vodka"]

list_trainer = ListTrainer(bot)
list_trainer.train(trivial)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english", 
              "chatterbot.corpus.english.conversations")

# while True:
#     inp = input()
#     print(bot.get_response(inp))
#     if (inp=="bye"):
#        break

while True:
    inp = input()
    print(bot.get_response(inp))
    if KeyboardInterrupt==True:
       break
