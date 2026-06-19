mark=[13,24,13,12,14,"adi",True]

print(type(mark))
print(mark)
print(mark[0])

mark.append(25)

print(mark)

# mark.sort()
# print(mark)
# mark.revers()

print(mark[-1])

if 12 in mark:
    print("12 is in marks")


print(mark[:])

lst=[i*i for i in range (4)]
print(lst)

mark.extend(lst)
print(mark)


k=mark+lst
print(k)

