#solve quadratic equation ax**2 + bx + c = 0
#coefficents a,b,c are provided by user

def quad():
    #import math
    from math import sqrt
    print("this program will find the roots of the equation")
    print()

    while(True):
        try:
            a = float(input("enter value of a: "))
            if (a == 0):
                print("All nonzero values are allowed.")
                continue
        except ValueError:
                print("All nonzero values are allowed.")
        else:
                    break
    b = float(input("enter value of b: "))
    c = float(input("enter value of c: "))

    #calculate the discriminant
    d = b**2 - 4*a*c
    d1 = sqrt(d)  #value of the discriminant

    #calculate the 2 solutions
    solution1 = (-b + d1) / (2*a)
    solution2 = (-b - d1) / (2*a)

    #output 2 solutions
    print("the values of the equation are {0}, and {1}".format(solution1,solution2))

    do_calculation = True
    while (do_calculation):
            #get input from user
            #perform the calculation
            #output the result

        another_calculation = input("Do you want to perform another calculation? (y/n): ")
        if (another_calculation != "y"):
            do_calculation = False
