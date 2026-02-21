import random

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

def insertion_sor_range(my_list, left, right):
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


test_list = [random.randint(0,1000) for m in range(100)]

