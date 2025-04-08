
x = 5 + 3 #addition
print(x)

y = 10 - 4 #subtraction
print(y)

z = 2 * 6 #multiplication
print(z)

a = 2**6
print(a) #raised to the power

b = 10 % 3 #this is  to find modulus
print(b)

c = abs(5-10) #this gives us the absolute value
print(c)

boy = "antimonopologeographicationalism"
girl = boy[0:20:3] #its on the third count, the letter there that is noted
print(girl)


for var1 in range(3):
    print("Iteration " + str(var1 + 1) + " of outer loop")
    for var2 in range(2):
        print(var2 + 1)
    print("Out of inner loop")
print("out of outer loop")        