from mathfunctions import pentagonalfinder


def collatzsequence():
    print("\nThis function finds which number in a given range produces the largest collatz sequence.\n")
    s = int(input("Start of range:\n"))
    e = int(input("\nEnd of range:\n"))
    list = []
    biglist = []
    listrange = [*range(s, e + 1)]
    for x in listrange:
        list.append(x)
        while 1 > 0:
            if x % 2 == 0:
                x = x / 2
                list.append(x)
                if x == 1:
                    break
            else:
                x = (3 * x) + 1
                list.append(x)
        a = int(len(list))
        biglist.append(a)
        list.clear()
    zipvalue = zip(biglist, listrange)
    sortedzip = [biglist for _,biglist in sorted(zipvalue)]
    print("\nThis is the start number with the longest collatz sequence:")
    print(sortedzip[-1])
    print("\nThis is the length of the sequence:")
    f = sorted(biglist)
    print(f[-1])
    print("\n")

def doublebasepalindrome():
    print("This function finds doublebased palindromes (in base 2 and 10). Enter a number to return a list of all doublebased palindromes from 0 to that number, and their sum.")
    plist = []
    u = int(input("NUMBER:\n"))
    r = [*range(1, u + 1)]
    a = 1
    while a < u:
        b = str(a)
        x = bin(a)
        y = str(x)
        startbinarylist = [i for i in y]
        startbinarylist.pop(0)
        startbinarylist.pop(0)
        binlist = [i for i in y]
        binlist.pop(0)
        binlist.pop(0)
        list = [i for i in b]
        startdecimallist = [i for i in b]

        # reverse the list...
        list.reverse()
        binlist.reverse()

        if binlist == startbinarylist and startdecimallist == list:
            plist.append(a)

        a += 1
    print(plist)
    s = sum(plist)
    print(s)

# amicable numbers
def amicablefinder():
    u = int(input("UPPER LIMIT:\n"))
    x = 1
    amicablenumbers = []
    while x < u:
        factorlist = []
        list = [*range(1, x)]

        for num in list:
            if x % num == 0:
                factorlist.append(num)

        sumit = sum(factorlist)
        nextfactorlist = []
        nextlist = [*range(1, sumit)]

        for num in nextlist:
            if sumit % num == 0:
                nextfactorlist.append(num)

        nextsumit = sum(nextfactorlist)

        if nextsumit == x and sumit != x:
            print (f"X: {x} and Y: {sumit}")
            #if not any(x for i in amicablenumbers):
            amicablenumbers.append(x)
            #amicablenumbers.append(sumit)

        x += 1

    print(amicablenumbers)

    total = sum(amicablenumbers)
    print(f"SUM OF AMICABLE PAIRS {total}")
def amicable():
    x = int(input("NUMBER:\n"))
    factorlist = []
    list = [*range(1, x)]
    for num in list:
        if x % num == 0:
            factorlist.append(num)
    #print(factorlist)
    sumit = sum(factorlist)
    #print(sumit)

    nextfactorlist = []
    nextlist = [*range(1, sumit)]
    for num in nextlist:
        if sumit % num == 0:
            nextfactorlist.append(num)
    #print(nextfactorlist)
    nextsumit = sum(nextfactorlist)
    #print(nextsumit)

    if nextsumit == x:
        print (f"{x} and {sumit} are AMICABLE NUMBERS!!!!")
    else:
        print(f"{x} has no amicable pair.")


# lattice paths
def latticepaths():
    x = int(input("""\nThis function shows the number of possible routes through a square lattice.
    Type a number to determine the length of one side of the square.
    NUMBER:\n"""))
    list1 = [*range(2, x + 2)]
    list2 = []
    wlist = []
    l = len(list1)
    w = l - 1
    a = 2
    while w != 0:
        q = 1
        while q <= w:
            if q == 1:
                if w == l - 1:
                    x = list1[q]
                    middle = x * 2
                    list2.append(middle)
                else:
                    x = list2[s - w]
                    middle = x * 2
                    list2.append(middle)
            else:
                if w == l - 1:
                    if q == 2:
                        next = list1[q] + middle
                        list2.append(next)
                    else:
                        next = list1[q] + next
                        list2.append(next)
                else:
                    next = list2[-1] + list2[-w]
                    list2.append(next)
            q += 1
        wlist.append(w)
        s = sum(wlist)
        w -= 1
        a += 1
    answer = list2.pop()
    print(f"\nThere are {answer} possible routes.\n")

    latticepaths()


# proving Golbach's conjecture wrong:
def gman():
    def primeyn(x):
        list = [*range(2, x)]
        if all(x % num != 0 for num in list):
            return True

    def primefinder(x):
        list = [*range(1, x + 1)]
        for num in list:
            y = primeyn(num)
            if y == True:
                primelist.append(num)

    def tsquarefinder(x):
        list = [*range(1, x + 1)]
        for num in list:
            y = 2 * (num ** 2)
            if y < x:
                tsquarelist.append(y)


    a = int(input("\nNUMBER:\n"))
    firstlist = [*range(1, a + 1)]
    for x in firstlist:
        y = primeyn(x)
        if x % 2 == 1 and y != True:
            primelist = []
            tsquarelist = []
            primefinder(x)
            tsquarefinder(x)
            simple = []
            for s in tsquarelist:
                for p in primelist:
                    if p + s == x:
                        print(f"{x}: Prime ({p}) + Square({s})")
                        simple.append(x)
            if len(simple) == 0:
                print(f"GOLDBACH IS WRONG FOR: {x}")
    print("\n")

def selfpowersum():
    x = int(input("\nNUMBER:\n"))
    list = [*range(1, x + 1)]
    emptylist = []
    for num in list:
        power = num ** num
        print(f"{num}: {power}")
        emptylist.append(power)
    sumit = sum(emptylist)
    print(f"\nSUM: {sumit}\n")

def sumdigitsofpower():
    a = int(input("\nNUMBER:\n"))
    b = int(input("POWER:\n"))
    x = a ** b
    print(f"\nANSWER: {x}")
    y = str(x)
    list = [i for i in y]
    for i in range(0, len(list)):
        list[i] = int(list[i])
    sumit = sum(list)
    print(f"\nSUM OF DIGITS: {sumit}\n")

# pythagorean triplets:
def pythagtriples():
    f = int(input("\nThis function finds pythagorean triples,\na^2 + b^2 = c^2\nUPPER LIMIT FOR C:\n"))
    s = int(input("\nThe sum of a b and c to be found:\n"))
    flist = [*range(1, f + 1)]
    for x in flist:
        c = x ** 2
        list = [*range(1, x)]
        alist = []
        blist = []
        for num in list:
            y = num ** 2
            alist.append(y)
            blist.append(y)
        clist = []
        aalist = []
        bblist = []
        for a in alist:
            for b in blist:
                if b >= a:
                    if a + b == c:
                        import math
                        cs = math.sqrt(c)
                        bs = math.sqrt(b)
                        ass = math.sqrt(a)
                        print(f"{ass}^2 + {bs}^2 = {cs}^2")
                        sumit = ass + bs + cs
                        print(f"SUM: {sumit}")
                        if sumit == s:
                            print("\n\n**********\nANSWER\n*********\n\n")
                            print(f"{ass} + {bs} = {cs}\nSUM: {sumit}")
                            print("\n\n**********\nANSWER\n*********\n\n")
    print("\n")

def fareyfinder():

    n = int(input("\nThis function finds the Farey sequence of a number.\nNUMBER:\n"))
    numerator = [*range(1, n + 1)]
    emptylist = []
    numeratorlist = []
    denominatorlist = []
    for num in numerator:
        x = 0
        denominator = [*range(1, n + 1)]
        while x < n:
            number = denominator[x]
            a = num / number
            if a < 1 and a not in emptylist:
                emptylist.append(a)
                numeratorlist.append(num)
                denominatorlist.append(number)
            x += 1
    print("\n")
    zipnum = zip(emptylist, numeratorlist)
    zipden = zip(emptylist, denominatorlist)
    snl = [numeratorlist for _,numeratorlist in sorted(zipnum)]
    sdl = [denominatorlist for _,denominatorlist in sorted(zipden)]
    length = len(numeratorlist)
    a = 0
    valuelist = []
    while a < length:
        b = snl[a]
        c = sdl[a]
        d = (f"{b} / {c}")
        e = b / c
        valuelist.append(e)
        print(d)
        a += 1
    print("\n")
    print(f"NUMBER OF VALUES: {length}\n")
    print(valuelist)

def trianglefinder():
    a = 1
    x = 2
    y = int(input("What number do you want to find triangle numbers up to?\n"))
    print(a)
    list = [1]
    while a < y:
        a = a + x
        print(a)
        list.append(a)
        x = x + 1
    print(f"There are {len(list)} triangle numbers up to {y}.")

def fibonaccifinder():
    y = int(input("Find fibonacci numbers up to:\n"))
    b = 0
    c = 1
    a = 1
    while c < y and a < y and b < y:
        a = b + c
        if a < y:
            print(a)
            b = a + c
            if b < y:
                print(b)
                c = a + b
                if c < y:
                    print(c)

print("""\nThis program helps solve mathematical sequences / problems.
Type the corresponding number and hit enter to access the respective program:


1 This function finds which number in a given range produces the largest collatz sequence.

2 This function finds doublebased palindromes (in base 2 and 10). Enter a number to return a list of all doublebased palindromes from 0 to that number, and their sum.

3 This function shows the number of possible routes through a square lattice. Input a number to determine the length of one side of the square.

4 This function determines whether an input has an amicable pair, and if so, it finds the amicable pair of the number you input.

5 This function prints a list of all the amicable pairs up to the limit you input, and their sum.

6 This function finds all the pythagorean triples (a^2 + b^2 = c^2) up to your input for c. The second input is the sum of a, b, and c which you are looking to find. If this sum is found in a triplet, it will be noted in the printed list.

7 This function prints the answer for x^x for every number from 1 up to the number you input.

8 This function prints the prime and square numbers which sum to give every odd composite number from 9 to the number you input. If this is impossible, it will print GOLDBACH IS WRONG FOR x.

9 This function finds the Farey sequence of a given number.

10 This function finds triangle numbers up to your input.

11 This function finds pentagonal numbers up to your input.

12 This function finds fibonacci numbers up to your input.""")



x = int(input("\n\nInput a number from 1 to 12 to select the corresponding function."))

if x == 1:
    collatzsequence()
if x == 2:
    doublebasepalindrome()
if x == 3:
    latticepaths()
if x == 4:
    amicable()
if x == 5:
    amicablefinder()
if x == 6:
    pythagtriples()
if x == 7:
    selfpowersum()
if x == 8:
    gman()
if x == 9:
    fareyfinder()
if x == 10:
    trianglefinder()
if x == 11:
    pentagonalfinder()
if x == 12:
    fibonaccifinder()




# end of script
