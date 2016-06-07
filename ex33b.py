def lister(limit, add):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i += add

        print "Numbers now :", numbers
        print "At the bottom i is %d" % i
    return numbers

print "The numbers: "

for num in lister(16, 2):
    print num
