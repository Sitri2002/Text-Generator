import random
import re
import string
punc = string.punctuation
def convert_text(file):
    text = []
    inp = open(file)
    #text = [[j for j in line.split()] for line in inp]
    text = [re.findall(r"[\w']+|[.,!?;]",line) for line in inp]
    return [word for line in text for word in line]

def state_transition(data, size):
    m_dict = {}
    temp = [' ']*size
    for i in range(len(data)):
        key = tuple(temp)
        if key not in m_dict.keys():
            m_dict[key] = []
            m_dict[key].append(data[i])
        else:
            m_dict[key].append(data[i])
        temp[0:-1] = temp[1:]
        temp[len(temp)-1] = data[i]
    return m_dict

def text_generator(m_chain, w_count, start = None):
    generated_text =[]
    keylist = [x for x in m_chain.keys()]
    width = len(keylist[0])
    if start:
        start_list = start.split()
        for x in start_list:
            generated_text.append(x)
    else:
        for x in keylist[width]:
            generated_text.append(x)
    while len(generated_text) <= w_count:
        l = len(generated_text)
        key = tuple(generated_text[l-width:l])
        if key not in m_chain.keys():
            break
        if len(m_chain[key][0]) > 1:
            generated_text.append(m_chain[key][random.randint(0,len(m_chain[key])-1)])
        else:
            generated_text.append(m_chain[key][0])
    return generated_text

def nice_print(text, word_per_line):
    s = ''
    count = word_per_line
    for i in range(len(text)):
        if count == 0:
            count = word_per_line
            s+='\n'
        count -= 1
        s+=text[i] + ' '
        
    return s

def standard_print(text):
    s = ''
    for i in range(len(text)-1):
        if text[i+1] in punc:
            s+= text[i]
        else: s += text[i]+ ' '
    return s

d = state_transition(convert_text('sunalsorises.txt')+convert_text("stud.txt")+convert_text('vall.txt')+convert_text('sign.txt')+convert_text('houn.txt'),3) 
print(standard_print(text_generator(d,90)))  