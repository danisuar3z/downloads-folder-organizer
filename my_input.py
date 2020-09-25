# -*- coding: utf-8 -*-

# my_input.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Input function


def my_input(question, answers):
    correct_answer = False
    while not correct_answer:
        answer_given = input(question)
        if answer_given in answers:
            correct_answer = True
    return answer_given