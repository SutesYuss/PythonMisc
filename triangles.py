"""Author: Sudi Yussuf
"""
def triangles(n):
    count = 0
    l = []
    for i in range(1,n+1):
      count = count +i
      l.append(count)
    print(l)
    return l

# triangles(6)

def ctriangles(n):
  n = [i * (i+1)//2 for i in range(1,n+1)]
  print(n)
  return n
  
# ctriangles(6)

def pascal(r):
  list1 = [1]
  list2 = []
  for i in range(r):
    list2.append(list1)
    list3 = []
    list3.append(list1[0])
    for i in range(len(list1) - 1):
        list3.append(list1[i] + list1[i+1])
    list3.append(list1[-1])
    list1 = list3
  print(list2)
  return list2

# pascal(6)