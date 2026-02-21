import random
import time
import matplotlib.pyplot as plt

# STEPS 1 & 2

def bubble_sort(my_list):
    steps=0 #Counting interation OR steps
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1-i):
            steps = steps + 1
            if my_list[j]>my_list[j+1]:
                temp = my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
                steps = steps + 3 #Adding 3 steps because it took 3 operations to do the swap
    print(my_list)
    return steps

li=[7,3,8,10,5]

# print(bubble_sort(li))

def selection_sort(my_list):
    steps = 0
    for i in range(len(my_list)):
        min_index = i
        for j in range(i+1, len(my_list)):
            steps = steps +1
            if my_list[j]<my_list[min_index]:
                min_index=j
            if min_index != i:
                temp = my_list[i]
                my_list[i]=my_list[min_index]
                my_list[min_index]=temp
                steps = steps + 3
    print(my_list)
    return steps

print(selection_sort(li))


def insertion_sort(my_list):
    steps = 0
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        steps = steps + 1
        while j>=0 and my_list[j]>key:
            steps = steps + 1
            my_list[j+1]=my_list[j]
            steps = steps + 1
            j = j -1
        my_list[j+1] = key
        steps = steps + 1
    return steps


def quick_sort(my_list, low=0, high=None):
    if high is None:
        high = len(my_list)-1

    steps = 0
    if low<high:
        piv=my_list[high]
        steps = steps + 1
        i = low - 1

        for j in range(low,high):
            steps = steps +1
            if my_list[j]<=piv:
                i = i + 1
                temp = my_list[i]
                my_list[i]=my_list[j]
                my_list[j]=temp
                step = step + 3

            tem = my_list[i+1]
            my_list[i+1]=my_list[high]
            my_list[high]=tem
            steps = steps+3
            piv_index = i + 1

            steps = steps + quick_sort(my_list, low, piv_index - 1)
            steps = steps + quick_sort(my_list, piv_index + 1, high)

    return steps

def insertion_sort_range(my_list, left, right):
    steps=0
    for i in range(left+1, right+1):
        key = my_list[i]
        j = i - 1
        steps = steps + 1
        while j>=left and my_list[j]>key:
            steps = steps + 1
            my_list[j+1]=my_list[j]
            steps = steps + 1
            j = j -1
        my_list[j+1] = key
        steps = steps + 1
    return steps


# VERIFICATION

test_list = [random.randint(0,1000) for m in range(100)]
print("Bubble sort: ", bubble_sort(test_list.copy()))
print("Selection sort: ", selection_sort(test_list.copy()))
print("Insertion sort: ", insertion_sort(test_list.copy()))
print("Quick sort: ", quick_sort(test_list.copy()))
print("Insertion range: ", insertion_sort_range(test_list.copy(),0,99))



# STEP 3

sizes=[10,50,100,500,1000,2000]

bubble_steps, selection_steps, insertion_steps, quick_steps = []

for n in sizes:
    worst_case = list (range(n,0,-1))

    bubble_steps.append(bubble_sort(worst_case.copy()))
    selection_steps.append(selection_sort(worst_case.copy()))
    insertion_steps.append(insertion_sort(worst_case.copy()))
    quick_steps.append(quick_sort(worst_case.copy()))

plt.figure()
plt.plot(sizes, bubble_steps, label="Bubble sort")
plt.plot(sizes, selection_steps, label="Selection sort")
plt.plot(sizes, insertion_steps, label="Insertion sort")
plt.plot(sizes, quick_steps, label="Quick sort")
plt.xlabel("n")
plt.ylabel("T(n)")
plt.title("Worst-case T(n) vs n")
plt.legend()
plt.show()
