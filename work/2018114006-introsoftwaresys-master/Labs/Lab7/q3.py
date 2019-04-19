def UniqueSort(u):  
   u=u.split(", ")
   my_set=set(u)
   u=list(my_set)
   u.sort()
   print(','.join(u))
x=input()
UniqueSort(x)