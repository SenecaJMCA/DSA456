# print("Hello word")

# function 1:
def wins_rock_scissors_paper(player1_opt, player2_opt):
    lower_player1_opt = player1_opt.lower()
    lower_player2_opt = player2_opt.lower()

    if lower_player1_opt == "rock":
        if lower_player2_opt == "rock":
            print("It's a tie!")
        elif lower_player2_opt == "scissors":
            print("Rock beats scissors, Player One wins!")
        elif lower_player2_opt == "paper":
            print("Paper beats rock, Player Two wins!")
        else:
            print("Invalid input, please choose one of the three options (rock, paper, scissors)")
    elif lower_player1_opt == "paper":
        if lower_player2_opt == "paper":
            print("It's a tie!")
        elif lower_player2_opt == "scissors":
            print("Scissors beats paper, Player Two wins!")
        elif lower_player2_opt == "rock":
            print("Paper beats rock, Player One wins!")
        else:
            print("Invalid input, please choose one of the three options (rock, paper, scissors)")
    elif lower_player1_opt == "scissors":
        if lower_player2_opt == "scissors":
            print("It's a tie!")
        elif lower_player2_opt == "paper":
            print("Scissors beats paper, Player One wins!")
        elif lower_player2_opt == "rock":
            print("Rock beats scissors, Player Two wins!")
        else:
            print("Invalid input, please choose one of the three options (rock, paper, scissors)")
    else:
        print("Invalid input, please choose one of the three options (rock, paper, scissors)")

# function 2:
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return -1
    else:
        i = 0
        result = 1
        while i != n:
            result = result * (n - i)
            i = i + 1

        return result
    

# function 3:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 

# function 4:
def sum_to_goal(arr, n):
    i=0
    j=0
    for i in arr:
        num1 = i
        for j in arr:
            num2 = j
            total_sum = num1 + num2
            if total_sum == n:
                return num1 * num2
    
    if i + j != n:
        return 0
        
            

