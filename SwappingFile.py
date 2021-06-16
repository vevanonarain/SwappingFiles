def fileSwapper() :
    
    fileName1 = input("Enter your oringinal filr name: ")
    fileName2 = input("Enter the file with which it has to be swapped: ")

    data_a = open("Test.txt", "r")
    data_b = open("Test(1).txt","r")

    data_a.read()
    data_b.read()

    data_a.close()
    data_b.close()

    data_a = open("Test.txt","w")
    data_b = open("Test(1).txt", "w")

    data_a.write(data_b)
    data_b.write(data_a)

    print(data_a)
    print(data_b)

fileSwapper()
