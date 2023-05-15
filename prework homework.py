#Question 1: hello_USERNAME
def hello_name(user_name):
    print("hello_"+str(user_name))

user_name = input('Enter a username: ')
hello_name(user_name)
print("\n")

#Question 2: All odd numbers between 0-100
def first_odds():
    for n in range(100):
        if n % 2 != 0 and n != 99:
            print(n, end=", ")
        elif n == 99:
            print(n, end=".\n")

first_odds()
print("\n")

#Question 3: Max # in the list
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

mylist = input("Please enter a list of numbers (separated by spaces): ")
mylist = mylist.split()
a_list = []
for i in mylist:
    num = int(i)
    a_list.append(num)

print("The maximum # in your list is: "+str(max_num_in_list(a_list)))
print("\n")

#Question 4: Is it a leap year?
def is_leap_year(a_year):
    y = int(a_year)
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 4 and y % 400 == 0:
        return True
    else:
        return False
    
a_year = input("Enter a year: ")
print(f'Was {a_year} a leap year?: '+str(is_leap_year(a_year)))
print("\n")

#Question 5: Is the list consecutive?
def is_consecutive(a_list):
    li = [0]
    for n in a_list:
        if n >= max(li):
            li.append(n)
        else:
            return False
    return True
        
str_list = input('Enter a list of numbers (separated by spaces): ')
str_list = str_list.split()
a_list = []
for i in str_list:
    num = int(i)
    a_list.append(num)

if is_consecutive(a_list) == True:
    print('The list is in order')
else:
    print('This list is not in order')
