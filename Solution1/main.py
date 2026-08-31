import random


print("="*20)
print("Welcome to My game")
print("="*20)


random_number = random.randint(1,100)

score = 100
EXIT_COMMONDS = ('Q','q','ex','exit','quit')

def evaluate_input(user_input,random_number,score):
    if not user_input.isdigit():
        return "invalid input please try again"
    
    user_input = int(user_input)
    if user_input > 100 or user_input < 1:
        return "invalid range! plaese Enter between 1 to 100"
    
    if score == 0 :
        return "you lose"
    
    if user_input < random_number:
        score-=10
        return f"your input is too low ==== remaining score : {score}"
            
            
    elif user_input > random_number:
        score-=10
        return f"your input is too high ==== remaining score : {score}"

    else:
        return f"You win!!! with score : {score}"
            
def main():
    while True:
        user_input = input(">>> ")
        
        if user_input in EXIT_COMMONDS:
            print("Thanks for playing")
            break
        
        print(evaluate_input(user_input,random_number,score))
        
        


if __name__ == '__main__':
    main()