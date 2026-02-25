#output: [ ## The syntax for slicing is: list[start:stop:step]1, 3, 4, 2, 5, 6]
number = [1,3,4,2,5,6,7,8,9,10]
print(number[0:6])


print(number[0:6:2])
#output: [1, 4, 5]

print(number[::-1])
#output: [10, 9, 8, 7, 6, 5, 2, 4, 3, 1]

print(number[::2])

#output: [1, 4, 5, 7, 9]    
print(number[::-2])\

#output: [10, 8, 6, 2, 4]


a = [x for x in range(100) ]
print(a)


b = [x for x in range(100) if x % 2 == 0]
print(b)
#list comprehension
squared = [x**2 for x in range(0, 10) ]
print(squared)

 