choice = int(input(
    "Enter 1 -> Type CI and Get Z-score\nEnter 2 -> Type Z-score and get CI\nEnter choice 1 or 2: "))

if choice == 1:
    ci = int(input("\nEnter CI: "))
    if (ci == 90):
        print("Z-score is 1.645\n")
    elif (ci == 95):
        print("Z-score is 1.96\n")
    elif (ci == 99):
        print("Z-score is 2.575\n")
    else:
        print("Not an available parameter please consult the table")

if choice == 2:
    z = float(input("\nEnter your z-score: "))
    if (z == 1.96):
        print("Percentage is 95 % CI or 0.95\n")
    elif (z == 1.645):
        print("Percentage is 90 % CI or 0.9\n")
    elif (z == 2.575):
        print("Percentage is 99 % CI or 0.99\n")
    elif (z == 0.99):
        print("Percentage is 67.77 % CI or 0.6777\n")
    elif (z == 1.282):
        print("Percentage is 79.94 % CI or .7994\n")
    else:
        print("Not an available parameter please consult the table")
