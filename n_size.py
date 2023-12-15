import math

choice = int(input(
    "Large size -> Enter 1\nProportion -> Enter 2\nSmall size -> Enter 3\nEnter your choice to calculate sample size: "))

if choice == 1:
    SE = float(input("Enter your sampling error: "))
    z = float(input("Enter your z-score based on your CI: "))
    s = float(input("Enter your standard deviation: "))

    n = (SE / (z * s))**2
    print("The sample size is: ", n)
    print("Remember to round to next number yourself. Tks!")

if choice == 2:
    SE = float(input("Enter your sampling error: "))
    z = float(input("Enter your z-score based on your CI: "))
    p = float(input("Enter your p-hat based on your success rate: "))
    n = (((z**2) * p * (1-p)) / (SE**2))
    print("The sample size is: ", n)
    print("Remember to round to next number yourself. Tks!")
