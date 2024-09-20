def makeSquare(size):
    for i in range(size):
        for x in range (size):
            print("*", end=''),
        print("")


size = int(input("Size of square? "))
makeSquare(size)