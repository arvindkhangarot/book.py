# print lower and upper case
name = "Ada Lovelace"
print(name.lower())
print(name.upper())

# f string
# combine those values to display someone’s full name:
first_name = "ada"
last_name = "lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
fulname=f"{first_name} {last_name}"
print(f"hello ,{fulname.title()}")

first_name = "ada"
last_name = "lovelace"
fullname=f"{first_name} {last_name}"
message= f"hello ,{fullname.title()}"
print(message)

'''Adding Whitespace to Strings with Tabs or Newlines
To add a tab to your text, use the character combination \t:'''
print("python")
print("\tpython")#for add white space

# To add a newline in a string, use the character combination \n
print("hello\nram \nshyam")#add new line

print("name:\n\tram\n\tshyam")

#remove white space
favorite_language = ' python '
print(favorite_language.rstrip())#remove right white space

favorite_language = ' python'
print(favorite_language.lstrip())#remove left white space

#Removing Prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

# Underscores in Numbers
universe_age = 14_000_000_000
print(universe_age)

#list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())#op is Trek(in trek t change in to capital T)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

# Using Individual Values from a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message=f"my firsy bicyles is {bicycles[0].title()}"
print(message)

#Modifying, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]='tvs'
print(motorcycles)

#append
motorcycles.append('tvs')
print(motorcycles)

motorcycles = []
motorcycles.append('tvs')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#remove
Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# pop
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle=motorcycles.pop()
print(popped_motorcycle)
print(motorcycles.pop(0))

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.pop(0)#remove item at tndex 0 and give op is['yamaha', 'suzuki']
print(motorcycles)
print(motorcycles.pop(0))#give pop vale
print(f'my first bike is{motorcycles}')

motorcycles = ['honda', 'yamaha', 'suzuki']
myfirst_bike=motorcycles.pop(0)
print(f'my first bike is {myfirst_bike.title()}')#op-my first bike is Honda(h is capital)

'''If you’re unsure whether to use the del statement or the pop() method,
here’s a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method.'''

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

#Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#loop
magicians = ['alice', 'david', 'carolina']
for i in magicians:
    print([i])
    print(i)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"that was a great trick!{magician.title()}, ")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

car=['maruti','honda','suzuki','kia']
for cars in car:
    print(f'my fav car is {cars.title()}')
    print(f'i cant wait for {cars.title()}\n')

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

Using the range() Function
for value in range(1,5):
    print(value)


# even numbers between 1 and 10:
for evenno in range(2,11,2):
    print(evenno)

#for odd no from 1,10
for oddno in range(1,11,2):
    print(oddno)

#find squre of number from 1 to 10
squre=[]
for i in range(1,11):
    i=i**2
    squre.append(i)
print(squre)

#min and max
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

List Comprehensions
find squre
squre=[i**2 for i in range(1,11)]
print(squre)

# Make a list of the numbers from one to one million
a=[1,2,5,88]
min1=[]
max1=[]
sum1=[]
for i in range(1, 1000001):
    count=i+1
    sum1.append(count)
    print(sum1)
#sum
sum1 = [1,2,4]
su=0
for i in sum1:
    su+=i
print(su)

#max
number = [1,2,4]
big=0
for i in number:
    if i >big:
        big=i
print(big)

number = [1,2,4]
small=10
for i in number:
    if i<small:
        small=i
print(small)

l = [1,2,4,55,66,5,5,84]
mx=l[0]
mi=l[0]
sum1=0
for i in l:
    if i>mx:
        mx=i
    if i <mi:
        mi=i
print(mx)
print(mi)
print(sum1)

#sum
l = [1,2,4,55,66,5,5,84]
so=l[0]
for i in l:
    so+=i
print(so)

#slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:2])
print(players[1:4])

# Without a starting index, Python starts at the beginning of the list:
name=['charles', 'martina', 'michael', 'florence']
print(name[:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3])
print(players[:-3])
print(players[-3:-1])

#print first three players on my team.using loop
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("first three player are")
for i in players[0:3]:

    print(i)
    print(i.title())

#copy list
my_foods = ['pizza', 'falafel', 'carrot cake']
food=my_foods
print(food)

#append

my_foods = ['pizza', 'falafel', 'carrot cake']
my_foods.append('ice')
print(my_foods)


car = 'Audi'
print(car.lower())


#if

requested_topping = ['mushrooms']
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 78:
    print("wrong ans")

age_0 = 222
age_1 = 18
if age_0 >= 21 or age_1 >= 21 :
    print('True')
else:
    print("not true")

# Checking Whether a Value Is in a List

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('available')

car = 'subaru'
print('is car is ==subaru','i predict righr')
print(car=='subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#if
age = 19
if age>18:
    print('you  age is enogh for vote')

age = 17
if age>=18:
    print('you  age is enogh for vote')
else:
    print('you  age is not enogh for vote')

age = 12
if age<4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40.")

#Check Python version
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
