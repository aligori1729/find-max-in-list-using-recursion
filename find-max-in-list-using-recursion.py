import random

def get_max(lst,m):
 if len(lst)==0:
  return m
 elif len(lst)==1:
  return max(lst[len(lst)-1],m)
 else:
  m=max(lst[len(lst)-1],m)
  lst=lst[:len(lst)-1:]
  return get_max(lst,m)

print("Generating random number list")
s=int(input("Enter length of list: "))
lst=[random.randint(1,1000)
for _ in range(s)]
print("List content:",lst)
print("Max value:",get_max(lst,0))