#!/usr/bin/env python3
# coding: utf-8

import sys
import json
import random


def ParseQuestion(open_file):
    """
    Parse a Python open file of formated questions in AMC style and return a 
    list of instance of class Question.
    """
    text = None
    goods = []
    bads = []
    current = None
    MCQ_lst = []
    # We manually add a last "*" in the parsing to register the last question 
    for line in open_file.readlines()+["*"]:
        if line[0] in "*+-":
            # We did read a new item
            # First, we register the last item
            if current is not None:
                if current[0] == "*":
                    text = current[1:]
                elif current[0] == "+":
                    goods.append(current[1:])
                elif current[0] == "-":
                    bads.append(current[1:])
                else:
                    raise ValueError("Error during parsing the questions file.")
            
            if line[0] == "*":
                # In this case, the new item is a new question
                # It is time to insert a potential question
                if text is not None:
                    MCQ_lst.append([text, goods, bads])
                    text = None
                    goods = []
                    bads = []
            
            # the new item overwrite the current one
            current = line 
        else:
            # If this is not a new item, we concat to the previous item.
            current = current.replace("\n", " ")
            current += line
    return MCQ_lst


def subset_index(n, p):
    """
    Returns a random subset of {0, ..., `n-1`} of size `p`
    """
    lst = []
    while (n >= p and p > 0):
        if random.randint(1, n) <= p:
            lst.append(n-1)
            p = p-1
        n = n-1
    return lst


def knuth_mixing(lst):
    """
    Mix in place element of the list `lst` in argument.
    """
    for i in range(len(lst)-1, 0, -1):
        j = random.randint(0, i)
        if j != i:
            lst[i], lst[j] = lst[j], lst[i]
    return lst


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
        sys.exit(1)
    
    # The parsing is done here
    file_question = open(file_question_name, "r")
    question_lst = ParseQuestion(file_question)
    context['mcq'] = question_lst
    
    # Set the number of questions in this MCQ
    if 'number_question' in context:
        number_of_mcq = int(context['number_question'])
        # By security, one can not have more questions than availlable.
        number_of_mcq = min(number_of_mcq, len(context['mcq']))
    else:
        number_of_mcq = len(context['mcq']) // 2
    
    # Set the text at begining of MCQ
    if number_of_mcq > 1:
        context['text'] = "Cliquez pour entammer une série de " + str(number_of_mcq) + " questions !"
    elif number_of_mcq == 1:
        context['text'] = "Cliquez pour accèder à la question !"
    else:
        context['text'] = "Aucune question n'a pu être préparée ou selectionnée : veuillez vérifier votre fichier de questions !"
    
    # Selection of the indices of the questions
    context['indices_questions'] = knuth_mixing(subset_index(len(context['mcq']), number_of_mcq))
    
    context['grade_questions'] = []
    context['form'] = " "
    context['clic'] = 0
    
    with open(sys.argv[2], 'w+') as f:
        json.dump(context, f)
        
    sys.exit(0)

sys.exit(0)

