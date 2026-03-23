# Example idea - what could this be useful for?
from symbol import return_stmt

pairs = {')': '(', ']': '[', '}': '{'}

s = "{[}]"


list1 = []

for i in s:

    if i == '(' or i == '[' or i == '{' :

        list1.append(i)

    elif i == ')' or i == ']' or i == '}':

        if list1[-1] == pairs[i]:
            print(list1[-1])
            print(pairs[i])

            list1.pop(-1)

if len(list1) == 0:
    print('True')
else:
    print('False')













