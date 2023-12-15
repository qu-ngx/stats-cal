import math
z = float(input("Enter your z-score: "))
s = float(input("Enter your population standard deviation: "))
n = int(input("Enter your sample size: "))

SE = z * (s / (math.sqrt(n)))

print("Sampling Error is: ", SE)
