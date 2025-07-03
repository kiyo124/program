#task 1
print("Task 1")
try:
    dict={'Aashish':95 , 'Himanshu':97 , 'Alice':85 ,'Ankit':99}
    a=input("Enter the student's name: ")
    print("{}'s marks: {}".format(a,dict[a]))
except KeyError:
    print("Student not Found")
print("Task 2")
#task2
lst=[i for i in range(1,12)]
print(lst)
print('Extracted first five elements: ',lst[:5])
print('Reversed Extracted elements: ',lst[4::-1])

