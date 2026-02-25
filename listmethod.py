a = [3,5,6,8,6,4,3,2]
a.sort()
print(a)
#output: [2, 3, 3, 4, 5, 6, 6, 8]

a.reverse()
print(a)
#output: [8, 6, 6, 5, 4, 3, 3, 2]
a.append(10)
print(a)
#`output: [8, 6, 6, 5, 4, 3, 3, 2, 10]
a.insert(2, 11)
print(a)
 #output: [8, 6, 11, 6, 5, 4, 3, 3, 2, 10]

a.remove(6)
print(a)
#output: [8, 11, 6, 5, 4, 3, 3, 2, 10]
a.pop()
print(a)

#output: [8, 11, 6, 5, 4, 3, 3, 2]
print(a.count(3))
#output: 2
  
print(a.index(4)) 
      #output: 4