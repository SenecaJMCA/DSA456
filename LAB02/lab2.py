
# FUNCTION 1

# def function1(number):
# 	total = 0
# 	for i in range(number):
# 		x = i + 1
# 		total += x * x
 
# 	return total

# Let n represent the value we are finding factorial for
# Let T(n) be the number of operations to find n! 

# Now lets count the operatiosn for each line of code. The loop runs n times
def function1(number):
	total = 0                   # 1 op     
	for i in range(number):     # n + 1 ops 
		x = i + 1               # n (1 op + 1 op)
		total += x * x          # n (1 op + 1 op + 1op)
	return total                # 1 op


# T(n) = 1 + n + 1 + n(1+1) + n(1+1+1)
# T(n) = 2 + n + 2n + 3n
# T(n) = 6n + 2

# Theferore T(n) is O(n) since the denominating term is n



# FUNCTION 2

# def function2(number):
# 	return (number * (number + 1) * (2 * number + 1)) // 6

# Let n represent the value we are finding factorial for
# Let T(n) be the number of operations to find n! 

# Now lets count the operatiosn for each line of code. Wil add a single value for each operator
def function2(number):
	return (number * (number + 1) * (2 * number + 1)) // 6 # 1 + (1 + (1) + 1 + (1 + 1) + 1)
        
# T(n) = 1 + (1 + (1) + 1 + (1 + 1) + 1)
# T(n) = 7

# The function growth rate is a constant. Therfore T(n) = c


# FUNCTION 3

# def function3(list):
# 	n = len(list)
# 	for i in range(n - 1):
# 		for j in range(n - 1 - i):
# 			if list[j] > list[j+1]:
# 				tmp = list[j]
# 				list[j] = list[j+1]
# 				list[j + 1] = tmp
				
# Let n represent the length of the list
# Let T(n) be the number of operations to find n

#  Now lets count the operatiosn for each line of code. 

	# n = len(list)    # len() is a constant so it is performed once plus a assinging op = 1 + 1

# The first loop runs (n-1) times. 
    # for i in range(n-1)     # (n-1) + 1 + 1
	
#The second loop for j:
# since i runs (n-1) times, this means that i assumes  i = 0, 1, 2, 3, ... (n-2)
# j assumes the valeu from 0 to (n-1-i), having i assum i = 0, 1, 2, 3, ... (n-2), the values for j will be j = (n-1), (n-2), (n-3), ... 1
# therefore the inner loop j will occurs (n-1) + (n-2) + (n-3) + ... + 1
# which is the same as (n-1)n/2

# For the If statement we count on comparison.
    # if list[j] > list[j+1]:     #  1

# Counting the operations in the inner loops.
    # tmp = list[j]           # 1
 	# list[j] = list[j+1]     # 1 
 	# list[j + 1] = tmp       # 1 
	
# def function3(list):
# 	n = len(list)                       # 1 + 1
# 	for i in range(n - 1):              # (n-1) + 1 
# 		for j in range(n - 1 - i):      # (n-1)n/2
# 			if list[j] > list[j+1]:     # (n-1)n/2 + 1
# 				tmp = list[j]           # 1 * [(n-1)n/2]
# 				list[j] = list[j+1]     # 1 * [(n-1)n/2]
# 				list[j + 1] = tmp       # 1 * [(n-1)n/2]

# T(n) = 1 + 1 + (n-1) + 1 + (n-1)n/2 + (n-1)n/2 + 1 + (n-1)n/2 + (n-1)n/2 + (n-1)n/2
# T(n) = 4 + (n-1) + 5[(n-1)n/2]
# T(n) = 5[(n2 - 2n(1) + 1)/2] + (n-1) + 4
# T(n) = (5n2 - 10n + 5)/2 + (n-1) + 4
# T(n) = (5n2)/2 - 5n + 5/2 + n - 1 + 4
# T(n) = (5n2)/2 - 4n + 13/2

# Theferore T(n) is O(n) since the denominating term is n2



# FUNCTION 4

# def function4(number):
# 	total = 1
# 	for i in range(1, number):
# 		total *= i + 1
# 	return total

# Let n represent the number
# Let T(n) be the number of operations to find n

# Now lets count the operatiosn for each line of code. Wil add a single value for each operator
def function4(number):
	total = 1                       # 1
	for i in range(1, number):      # (n-1) + 1
		total *= i + 1              # (n-1)(1+1+1)
	return total                    # 1

# T(n) = 1 + (n-1) + 1 + (n-1)(1+1+1) + 1
# T(n) = 1 + n - 1 + 1 + 3n - 3 + 1
# T(n) = 4n - 1

# Theferore T(n) is O(n) since the denominating term is n