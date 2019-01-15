#!/usr/bin/env python3
# coding: utf-8
import sys, json
import random
from sandboxio import output, get_context, get_answers


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
    with open(sys.argv[1]) as f:
        context = json.load(f)
    f.close()
    
    with open(sys.argv[2]) as f:
        answers = json.load(f)
    f.close()
    
    # time to correct the last question if relevant
    if context['clic'] > 0:
        grade = 0
        
        ok = 0
        not_ok = 0
        for good in context['goods']:
            if good in answers:
                ok += 1
            else:
                not_ok += 1
        for bad in context['bads']:
            if bad in answers:
                not_ok += 1
            else:
                ok += 1
        
        grade = 100*ok // (ok+not_ok)
        context['grade_questions'].append(grade)
    
    
    context['text'] = ""
    context['form'] = ""
    
    # time to prepare the next question
    if len(context['grade_questions']) < len(context['indices_questions']):
        context['clic'] += 1
        question = context['mcq'][context['indices_questions'][len(context['grade_questions'])]]
        
        context['goods'] = []
        context['bads'] = []
        
        context['text'] += question[0]+"\n\n"
        
        # Total possible option and random combination
        if 'min_option' in context:
            min_answer = int(context['min_option'])
        else:
            min_answer = 4 # This minimizes the number of option  
        if 'max_option' in context:
            max_answer = int(context['max_option'])
        else:
            max_answer = 8 # This bounds the number of option if there are more
        
        total = len(question[1]) + len(question[2])
        max_option = min(max_answer, total)
        min_option = min(min_answer, total)
        nb_option = random.randint(min_option, max_option)
        indices = knuth_mixing(subset_index(total, nb_option))
    
        # generation of the form
        for index in indices:
            if index < len(question[1]):
                context['goods'].append(str(index))
                context['form'] +='<input type="checkbox" name="c_' + \
                str(index) + '" value="' + str(index) + '" id="form_' + \
                str(index) + '">' + question[1][index] + "<br />"
            else:
                context['bads'].append(str(index))
                context['form'] +='<input type="checkbox" name="c_' + \
                str(index) + '" value="' + str(index) + '" id="form_' + \
                str(index) + '">' + \
                question[2][index - len(question[1])] + "<br />"
        
        output(-1, str(context['clic'])+" CLIC<br />"+context['text']+context['form'], context)
    
    if len(context['grade_questions']) == len(context['indices_questions']):
        grade = 0
        for g in context['grade_questions']:
            grade += g
        grade = grade // len(context['grade_questions'])
        
        feedback = "Vous avez obtenu *" + str(grade) + "%* de réussite à votre QCM."
        
        output(grade, feedback, context)
    
    output(-1, "", context)

