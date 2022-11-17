from stack import Stack

def balancing(exp):

    myStack = Stack()
    len_exp = len(exp)

    if len_exp % 2 != 0:
        return 'Brackets are not balanced'

    for i in exp:

        if i == '(' or i == '[' or i == '{':
            myStack.push(i)

        elif i == ')' and myStack.items[-1] != '(':
            return 'Brackets are not balanced'
        elif i == ')' and myStack.items[-1] == '(':
            myStack.pop()

        elif i == ']' and myStack.items[-1] != '[':
            return 'Brackets are not balanced'
        elif i == ']' and myStack.items[-1] == '[':
            myStack.pop()

        elif i == '}' and myStack.items[-1] != '{':
            return 'Brackets are not balanced'
        elif i == '}' and myStack.items[-1] == '{':
            myStack.pop()

    return 'Brackets are balanced'


def reading_file():
    file1 = open('input_balancing.txt', 'r')

    list = []
    list2 = []
    list3 = []

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
            if str[j] == '(' or str[j] == ')' or str[j] == '[' or str[j] == ']' or str[j] == '{' or str[j] == '}':
                list2 = list2 + str[j]
            j += 1
        final_list.append(list2)
        i += 1
    
    return final_list

list = inserting()

for str in list:
    print(str, balancing(str))