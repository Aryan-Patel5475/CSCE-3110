from stack import Stack

def postfic_eval(exp):

    myStack = Stack()

    for ch in exp:

        if ch.isdigit():
            myStack.push(int(ch))

        else:
            x = myStack.pop()
            y = myStack.pop()

            if ch == '+':
                myStack.push(y + x)
            elif ch == '-':
                myStack.push(y - x)
            elif ch == '*':
                myStack.push(y * x)
            elif ch == '/':
                myStack.push(y // x)

    return myStack.pop()


def reading_file():
    file1 = open('input_postfixeval.txt', 'r')

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

expression = inserting()
for exp in expression:
    print(postfic_eval(exp))