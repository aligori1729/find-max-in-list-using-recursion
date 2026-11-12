import random

def get_max(lst,m):
 if len(lst)==0:
  return m
 elif len(lst)==1:
  if lst[len(lst)-1]>m:
   return lst[len(lst)-1]
  else:
   return m
 else:
  m=max(lst[len(lst)-1],m)
  lst=lst[:len(lst)-1:]
  return get_max(lst,m)

print("Generating random number list")
s=int(input("Enter length of list: "))
min_interval=int(input("Enter min interval: "))
max_interval=int(input("Enter max interval: "))
lst=[random.randint(min_interval,max_interval)
for _ in range(s)]
print("List content:",lst)
print("Max:",get_max(lst,lst[s-1]))