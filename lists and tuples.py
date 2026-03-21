#lists
marks=[1,2,3,4,5,6,7]
print(marks)
print(type(marks))

print(marks[0])

print(len(marks))

student = ["niharika", 23, "delhi"]
print(student)

#immutable string
#str ="hello"
#print(str[0])
#str[0]="y"

#mutable lists
hello = ["aman", 23, "udpr"]
print(hello[0])
hello[0]="arjun"

marks=[30,34,56,78,89]

print(marks[1:5]) #last element not included

#list methods
#append

list=[1,2,3,4,5,6,7]
list.append(8)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(4,12)
print(list)

print(list.remove(12))
print(list)

list.insert(4,12)
list.pop(4)
print(list)

#tuple
tup = (1,2,3,4,5,6,7,7)
print(type(tup))
print(tup)

print(tup.index(5))

print(tup.count(7))

#practice questions


#Movies=[]
#Mov1=input("Enter 1st movie:")
#Mov2=input("Enter 2nd movie:")
#Mov3=input("Enter 3rd movie:")

#Movies.insert(0,Mov1)
#Movies.insert(1,Mov2)
#Movies.insert(2,Mov3)

#Movies.sort()
#print(Movies)

#question2
#palindrome concept

list1=["m","o","m"]


copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")

else:
    print("not palindrome")



#question3
grade = ("a","b","c","a","a")

print(grade.count("a"))

#question4

alphabets = ["A","B","C","D","C","D"]

print(alphabets.sort())
print(alphabets)



