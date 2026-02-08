# -----------------------------------------------------------------------------
# ----------------------------   PART A  --------------------------------------
# -----------------------------------------------------------------------------

# FUNCTION 1
def factorial(number):
    res = 1
    if number<=1:
        return res
    elif number>1:
        res = number * factorial(number-1)

    return res


# FUNCTION 2
def linear_search(list,key, i=0):
    if i == len(list):
        return -1
    
    if key == list[i]:
        return i
    
    return linear_search(list,key, i=i+1)


# FUNCTION 3
def binary_search(list,key,i=0):

    if i == len(list):
        return -1
    
    if list[i]== key:
        return i
    
    return binary_search(list,key,i=i+1)



# -----------------------------------------------------------------------------
# ----------------------------   PART B  --------------------------------------
# -----------------------------------------------------------------------------

# FUNCTION 1

def function1(value, number):
	if (number == 0):                                   # 1op
		return 1        
	elif (number == 1):                                 # 1op
		return value
	else:                                               
		return value * function1(value, number-1)       #  1op * (number-1)
     
# In the best case scenario the number will be either 0 or 1. Then the iteraction to the function would be limited to 2op, T(0) = O(1), the growth rate is in a constante magnitude.
# Now assuming number is greater than 1 and assuming n as the number of operations to find the factorial. As T(n) being the running time fot function1(valeu, n)
# T(n) = T(n-1) + c
# The grwoth rate magnitude of n, therefore T(n) = O(n)

# FUNCTION 2

def recursive_function2(mystring,a, b):
	if(a >= b ):                                                # 1op
		return True
	else:
		if(mystring[a] != mystring[b]):                         # 1op
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)        # 1op + 1op + 1op
 
def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

# Analysing the function2 first, we noticed that there are 3 operations, calling recursive_function2, subtraction and lastly the len(). Assuming that n is len(my_string) 
# and T(n) as the running time for function2, we ende up: 

# T(n) = 1op + 1op + 1op => T(n) = 3 => T(n) = c => O(1) = c

# T(n) = O(1), in other words a constante growth rate magnitude for function2.

# Now analyzing recursion_function2, assuming n as the length of mystring, we see that there is 5 operations and a recursion that happens n/2 since everytime we call the recursion function
# eliminates the first and last character to be analyzed.
# So T(n) = 5 + n/2 => c + n/2 => O(n)

# Lastly if we add up the T(n) for both functions we have:
# T(n) = O(1) + O(n) => T(n) = O(n). The growth rate is linear as having T(n) = O(n)


# -----------------------------------------------------------------------------
# ----------------------------   PART C  --------------------------------------
# -----------------------------------------------------------------------------

# 1) My approach for every recursive function was to initially come up with a function that will achieve the same result but not recursive. Basically I would create a normal fucntion.
# Once I understood what and how the function woudl work then I started working on the most basic case of the recursive function, let's say when the number was at the start of the list or when the numebr was just not in the list.
# That gave the basic case where a following case N+1 would eventually run back to it. And then at the end my most concern what how to call the same fucntion and make the function remember what
# was the result for the last interation

# 2) For me the recursive functions are always based on the basic case. For every fucntion to be rewritten in a recursive way the way to go is trying to break into small problems the same function.
# This way it allows me to target the specific part of the code that need changes. For example there are part of the code that we need to considerer the "loop" and if there is a variable that would track the "loop".
# But basically what differs the most from a normal function to a recursive function is the fact that in a recursive function we have always to consider first the most basic case for that function, the case where the lower value would be assign to.