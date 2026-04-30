
def get_score():
     return float(input("please enter score:"))
     


def check_score(score):
    while  (score < 0.0)  or  (score > 1.0):
        print('out of range')
        score = get_score()
    return score

def check_grade(score):
    
    if score >= 0.9:
          print('GRADE A')

    elif score >= 0.8:
         print("GRADE B")
    
    elif score >= 0.7:
         print("GRADE C")

    elif score >= 0.6:
         print("GRADE D")

    else:
         print('GRADE F')



def main():
    score = get_score()
    score = check_score(score)
    check_grade(score)
         
    
if __name__ == '__main__':
     
     main()
     