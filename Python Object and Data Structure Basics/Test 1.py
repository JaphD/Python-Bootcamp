#Object Types and Data Structures

Numbers = 'Can be either integers which are whole numbers with no decimal points or floating points which have decimal places'
Strings = 'Is an ordered sequence of characters'
Lists = 'Is an ordered and mutable sequence of objects'
Tuples = 'Similar to list but is immutable'
Dictionaries = 'Has a key value pairing and is mutable. It is not ordered'


#Numbers
num = ((((5**2)*8)/2)+2)-1.75
print(num)


print(4*(6+5))
print(4*6+5)
print(4+6*5)


print(type(3+1.5+4))


y = 4
x = y**0.5
print(x)
x = y**2
print(x)


#Strings
s = 'hello'
print(s[1])


print(s[::-1])


print(s[4])
print(s[-1])


#Lists
my_list = [0,0,0]
x_list = [0,0]
y_list = [0]
x_plus_y_list = x_list + y_list
print(my_list)
print(x_plus_y_list)


list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)
list4 = [5,3,4,6,1]
list4.sort()
print(list4)


#Dictionaries
d = {'simple_key': 'hello'}
print(d['simple_key'])


d = {'k1': {'k2':'hello'}}
print(d['k1']['k2'])


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1])


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])


#We can't sort a dictionaries because they're not ordered mappings of objects

#Tuples
# Major difference between tuples and lists: Tuples are immutable and lists are mutable
#How do you create a tuple: We create tuples in similar fashion to lists but we use normal brackets instead of square ones


#Sets
#What is uniqye about a set? Sets only store unique elements, meaning only one representative for the same object


list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))


#Booleans
#F
#F
#F
#T
#F


#Final Question
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False? #Answer = False
print(l_one[2][0] >= l_two[2]['k1'])











