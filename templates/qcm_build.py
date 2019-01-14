#!/usr/bin/env python3
# coding: utf-8

import sys
import json

class Question():
    """
    A class to model the notion of questions with multiple choice.
    """
    def __init__(self, text, goods, bads):
        """
        Initialize a question with its `text` : the question, with a list of 
        good answers `goods` together with a list of bad answers `bads`.
        
        `text` is supposed to be a Python string.
        `goods` is supposed to be a list of Python strings.
        `bads` is supposed to be a list of Python strings.
        """
        self._text = text
        self._goods = goods
        self._bads = bads
        
    def __str__(self):
        """
        Returns a string describing `self` : i.e. a question.
        """
        return "A question with mutiple possible choice"


def ParseQuestion(brut_str_question):
    """
    Parse a brut Python string of formated questions in AMC style and return a 
    list of instance of class Question.
    """
    i = 0
    prev = "\n"
    current = None
    nb_total_char = len(brut_str_question)
    lst_goods = []
    lst_bads = []
    current_text = ""
    is_question = False
    is_good = False
    is_bad = False
    
    # This is a brutal char by char parsing
    while i < nb_total_char:
        current = brut_str_question[i]
        if prev == "\n" and current in "*+-":
            is_question = False
            is_good = False
            is_bad = False
            if current == "*":
                is_question = True
                is_good = False
                is_bad = False
        prev = current
        i = i+1
    

if __name__ == "__main__":
    """
    This programm generate a nice Multiple Choice formulary from the context 
    exercice. The MCQ is mainly build from a file specified by key 
    `data_from_file` inside the exercise.
    """
    with open(sys.argv[1],'r') as f:
        context = json.load(f)
       
    # Here is the name of the file containing all available questions
    file_question_name = context['data_from_file']
        
    if file_question_name == "None":
        context['text'] = ("Cet exercise n'utilise pas le template qcm "
        "correctement. L'entrée 'data_from_file' de l'exercice doit spécifier "
        "le chemin d'un fichier accessible contenant les questions.")
    else:
        file_question = open(file_question_name, "r")
        context['text'] = file_question.readlines()
        
    with open(sys.argv[2], 'w+') as f:
        json.dump(context, f)

sys.exit(0)

