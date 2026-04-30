#Game of find the ball in 3 jugglers
from random import shuffle

def shuffled_list(list):

     shuffle(list)

     return list


def user_guess():
     
     guess = ''
     
     while guess not in ['0', '1', '2']:

        guess = input("please Provide number between 0 to 2:") 

     return int(guess)


def final_result(list, guess):

    if list[guess] == 'O':

        print('U won!!')

    else:
        print("wrong guess")
        print(list)


#main call
main_list = ['', 'O', '']

result = shuffled_list(main_list)

input_index = user_guess()
print(input_index)

final_result(result,input_index)

