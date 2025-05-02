s = {1,2,3,44,"Suffi"}
empty = set()#Declare As Empty Set  If We USe {} this It declare Empty Dictionary
print("********Initial set********\n",s,type(s))
s.add(566)
print("\n********Adding 566 to set********\n",s)
s.remove(2)
print("\n********Removing 2 From Set********\n",s)
# s.clear()
# print(s)
s2= {1,2,55,"Suffi"}
print("\n********Union Of A Set********\n",s.union(s2))
print("\n********Intersection Of sets********\n",s.intersection(s2))