# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 10:41:02 2022

@author: 唐琪登
"""

class Polygon:
    def __init__(self, no_of_sides=3):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def findArea(self):
        a,b,c = self.sides
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f'the area of this triangle is {area}')


triangle = Triangle()

#%%
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)

#%% iterator
numbers = [1, 2, 3]
value = iter(numbers)

while True:
    try:
        element = next(value)
        print(element)
    except:
        print('end of iteration',f"length is {len(numbers)}")
        break
    
#%% 
# Python code showing use of iter() using OOPs

class Counter:
	def __init__(self, start, end):
		self.num = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.num > self.end:
			raise StopIteration
		else:
			self.num += 1
			return self.num - 1
			
			
# Driver code
if __name__ == '__main__' :
	
	a, b = 2, 5
	
	c1 = Counter(a, b)
	c2 = Counter(a, b)
	
	# Way 1-to print the range without iter()
	print ("Print the range without iter()")
	
	for i in c1:
		print ("Eating more Pizzas, counting ", i, end ="\n")
	
	print ("\nPrint the range using iter()\n")
	
	# Way 2- using iter()
	obj = iter(c2)
	try:
		while True: # Print till error raised
			print ("Eating more Pizzas, counting ", next(obj))
	except:
		# when StopIteration raised, Print custom message
		print ("\nDead on overfood, GAME OVER")

#%%
# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3


# Driver code to check above generator function
a = simpleGeneratorFun()

while True:
    print(next(a))

#%%
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

#%% The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
    
    def bark(self):
        print(f'the max value is {self.max}')
    
sample = PowTwo(10)

#%%
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
    raise InterruptedError()

try:
    sample_1 = PowTwoGen(10)
    while True:
        print(next(sample_1))
except:
    print('error')


#%%
def fibonacci():
    n_0 = 0; n_1 = 1
    while True:
        yield n_0
        n_0, n_1 = n_1, n_0 + n_1
        

f = fibonacci()
for i in range(5):
    print(next(f))

#%%
a = 10

def plus():
    # a += 1
    print(a)
    

plus()

#%% 
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

#%%
# Python program to illustrate
# closures
import logging
logging.basicConfig(filename='example.log',
					level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))
        print('cheer up')
        
		
	# Necessary for closure to
	# work (returning WITHOUT parenthesis)
    return log_func			

@logger
def add(x, y):
	return x+y

@logger
def sub(x, y):
	return x-y

# add_logger = logger(add)
# sub_logger = logger(sub)

add(3, 3)
add(4, 5)

sub(10, 5)
sub(20, 10)

#%%
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

#%%
def test(a,*args, **kwargs):
    for value in args:
        print(value)
    
    for _,v in kwargs.items():
        print(v)
    
    print(a)
test(1,2,3,c=1,d=2)

#%% decorator
# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
	
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
	def inner1(*args, **kwargs):

		# storing time before function execution
		begin = time.time()
		
		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)

	return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	print(math.factorial(num))

# calling the function.
factorial(100000)

#%% 
# Basic method of setting and getting attributes in Python
class Celsius:
    def __init__(self, temperature=[0]):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    def __getitem__(self ,i):
        return self.temperature[i]
    


# Create a new object
human = Celsius()

# Set the temperature
human.temperature = [31,32,33]

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
#print(human.to_fahrenheit())

#%%
# using property class
class Celsius:
    def __init__(self, t=0):
        self.temperature = t

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

human.temperature = -300

#%% map;filter
x1 = [1,2,3]
x2 = [4,5,6]

for i,v in zip(x1,x2):
    print(i,v)

x3 = list(map(lambda x:x+2,x1))
x4 = list(filter(lambda x:x % 2 == 0, x2))
print(x4)

#%%
class studentInfo:
    
    def __init__(self, ID, age):
        self.ID = ID
        self.age = age
        self.i = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.i += 1
        
        return self.ID[self.i - 1]
    
sInfo = studentInfo([1,2,3], [4,5,6])

x5 = list(map(lambda x:x+1, sInfo))

#%%
class Human:
    
    def __init__(self,age=0,gender='male',weight=45,height=165):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.h = height
    
    def bark(self, content):
        print(f'human can bark {content}')

class Student(Human):
    def __init__(self, ID):
        super().__init__()
        self.ID = ID
        
    def voice(self, content):
        super().bark(content)
        

xiaoMing = Student(10)
xiaoMing.voice('hahahah')

#%%
l = [1, 2, 3, 4, 5, 6, 7, 8]
n = [i if i < 5 else 5 for i in l]
print(n)

#%%
li = list(map(lambda x, y: str(x)+'_'+y, range(5), list('abcde')))
print(li)

another_li = list(map(lambda x,y: x+y,[1,2,3],[4,5,6]))
print(another_li)

#%%
import numpy as np
a = np.linspace(0, 10, 100)

b = np.arange(0,10)
c = np.random.rand()

#%% 布尔索引
target = np.arange(9).reshape(3,3)
target[np.ix_([True, False, True], [True, False, True])]
target[np.ix_([1,2], [True, False, True])]

new = np.random.rand(3,4)
mul = target @ new






