def pattern():
    for i in range(5):
        for j in range(5):
            print("*",end=" ") # to break the \n we use end = " " to get the output row wise
        print() # go to the next line we can also use print(end = " ") if we dont use this the output will be in a single row
pattern()
pattern()
pattern()
pattern()