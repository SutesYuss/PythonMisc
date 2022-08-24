"""Author: Sudi Yussuf
"""

def words(s):
  wordList= []
  i = 0
  newString = ""
  while i < len(s):
    if s[i].isalpha():
      newString = newString + s[i]
      i +=1
    else: 
      if len(newString) > 0:
        wordList.append(newString)
        newString = ""
      i+=1
  # print(wordList)
  for x in wordList:
    yield x

# words("Hello,_this_is Alan.")

def firstlines(file_name):
  mydict = {}
  with open(file_name) as f:
    lines = f.readlines()
    count = 0
  for i in lines:
    s = words(i)
    for j in s:
      mydict.update({j : count})
    count +=1
  print(mydict)
  return mydict
  

# firstlines("text")