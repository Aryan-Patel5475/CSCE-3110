from stack import Stack

import re

PRECEDENCE = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}

def infix_postfix(exp):
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", exp)

    myStack = Stack()
    postfix = []

    for token in tokens:

        if token.isalnum():
            postfix.append(token)

        elif token == '(':
            myStack.push(token)
        elif token == ')':
            top = myStack.pop()
            while top != '(':
                postfix.append(top)
                top = myStack.pop()

        else:
            while myStack.items and (PRECEDENCE[myStack.items[-1]] >= PRECEDENCE[token]):
                postfix.append(myStack.pop())
            myStack.push(token)

    while myStack.items:
        postfix.append(myStack.pop())
    return ''.join(postfix)

def reading_file():
    file1 = open('input_infix2postfix.txt', 'r')

    list = []

    for line in file1:
        list.append(line)

    return list

def inserting():
    list = reading_file()
    final_list = []

    i = 0
    while i < len(list):
        str = list[i]
        list2 = ''
        j = 0
        while j < len(str):
            if str[j] == '\t':
                j += 1
                if str[-1] == '\n':
                    list2 = str[j:-1]
                else:
                    list2 = str[j:]
            j += 1
        final_list.append(list2)
        i += 1

    return final_list

expressions = inserting()

for exp in expressions:
    print(infix_postfix(exp))