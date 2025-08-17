#a loop is basically a way to repeat a block of code multiple times until a certain condition is met
# in python there are 2 types of loops
#for loop

'''list1 = ['S', 'R', 'M', 'C', 'E', 'M']

for i in list1:
    print(i)

#for loop in tuple

list2 = ('S', 'R', 'M', 'C', 'E', 'M')
for i in list2:
    print(i, end=" ")

for i in list1:
    print(i)

#for loop in tuple

list2 = ('S', 'R', 'M', 'C', 'E', 'M')
for i in list2:
    print(i, end=" ")


list3 = [100, 90, 30, 40, 50, 60, 70, 20, 10, 80]
for i in range(10):
    print(i, end=" ")'''

#for i in range(1, 4):
    #print("Table of",i)
    #for j in range(1, 4):
        #print(i,"x", j, "=", i*j)

#fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
#for i in fruit:
   # if i == "banana":
       # print(i)

# write a function sum_number(n) that use for loop to calculate the sum of numbers from 1 to n

''''def sum_number(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print(sum)

sum_number(3)'''

# write a function to calculate the sum of even numbers from 1 to n

''''def sum_even_numbers(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum = sum + i
    print(sum)
sum_even_numbers(9)'''

'''def print_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)

print_table(5)'''

# write a function to print the vowels and count the vowels

'''def print_vowels(s):
    vowels = "aeiouAEIOU"
    sum = 0
    for char in s:
        if char in vowels:
            print(char, end=" ")
            sum = sum + 1
    print("Total vowels:", sum)

print_vowels("Gaurav")'''

#write a function that takes a list of numbers and returns a list of the square of those numbers

''''def list_squares(list1):
    list2 = []
    for i in list1:
        list2.append(i**i)
    print(list2)
list_squares([1, 2, 3, 4, 5])'''

#reverse string
'''def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    print(reversed_s)
reverse_string("Gaurav")'''

# words length (["apple", "banana", "cherry"])--> apple : 5, banana : 6, cherry : 6
''''def word_length(words):
    for word in words:
        print(word, ":", len(word))

word_length(["apple", "banana", "cherry"])'''

#loops conditional statement

#break
'''for i in range(10):
    if i == 6:
        break
    print(i)'''

#continue
'''for i in range(10):
    if i == 6:
        continue
    print(i)'''

#pass
'''for i in range(10):
    if i == 6:
        pass
    print(i)'''

#basic loop example
''''count = 1
while count <= 5:
    print("Count is:", count)
    count += 1'''

#else clause in loops 
#python allows an else with loops

'''for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished successfully")'''

#factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

factorial(5)
