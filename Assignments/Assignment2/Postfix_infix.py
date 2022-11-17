from stack import Stack

def postfix_infix(exp):

    myStack = Stack()

    i = 0
    while i < len(exp):
        char = exp[i]
        if char.isalpha() or char.isupper() or char.isnumeric():
            myStack.push(char)
        else:
            operator1 = myStack.pop()
            operator2 = myStack.pop()

            myStack.push('(' + operator2 + exp[i] + operator1 + ')')

        i += 1

    return myStack.pop()

expression = ['1b*c+d*e/']
print(postfix_infix(expression[0]))