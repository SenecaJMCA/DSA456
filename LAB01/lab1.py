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
        
            

class UpCounter:
    def __init__(self, stepSize = 1):
        self.counter = 0
        self.stepSize = stepSize
    
    def count(self):
        return self.counter
    def update(self):
        self.counter = self.counter + self.stepSize


class DownCounter(UpCounter):
    def __init__(self, stepSize=1):
        super().__init__(stepSize)
        
    def update(self):
        self.counter = self.counter - self.stepSize


    


# Part B
# 1 - What I like the most about Python is the fewer lines of code required to accomplish a result when compared with other programming languages, it seems simplier
# 2 - Yes, the indentation and the fact we don't need braces to delimited code blocks. Since I'm not used to that I felt a bit strange
# 3 - Well in terms of difference, the fact that Python is not a low level code programming language type as C++ allow us to forget about memory leak as it happens in C++. Having the machine to take care of how much 
# memory I will need to write a new variable without specifing the type of data the variable will receive make our life easier, and also I believe that makes the code less error prone.
# In term of similiarities most of the control flow statements (fi, for loops, while loop) work quite similar. Also for classes the destructor in C++ and the def __init__ in Python have the same functionality
# it's like a blueprint of the class and what it needs to be isntantiated.