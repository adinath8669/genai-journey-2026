tup=(12,34,56,23,24)

print(tup)

print(tup[0])

temp=list(tup)
temp.append(50)
tup=tuple(temp)

print(tup)

r=tup.count(12)

print(r)