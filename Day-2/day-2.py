type(123)
print(type(123))


type(9.99)
print(type(9.99))

type(5+6j)
print(type(5+6j))

type(True)
print(type(True))


# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# boolean variable.
b=True
print("The type of variable having value", b, " is ", type(b))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))

type("Welcome To Python")
print(type("Welcome To Python"))

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

type([2023, "Python", 3.11, 5+6j, 1.23E-4])
print(type([2023, "Python", 3.11, 5+6j, 1.23E-4]))

type([['One', 'Two', 'Three'], [1,2,3], [1.0, 2.0, 3.0]])
print(type([['One', 'Two', 'Three'], [1,2,3], [1.0, 2.0, 3.0]]))


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

for i in range(5):
  print(i)

for i in range(1, 5, 2):
  print(i)

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

a = True
# display the value of a
print(a)

# display the data type of a
print(type(a))

# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns True as a is 10
a = 10
print(bool(a))