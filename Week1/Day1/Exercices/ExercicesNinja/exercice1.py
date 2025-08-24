# Boolean comparisons
print(3 <= 3 < 9)       # True (3 <= 3 and 3 < 9)
print(3 == 3 == 3)      # True (all equal)
print(bool(0))          # False (0 is considered False)
print(bool(5 == "5"))   # False (integer 5 != string "5")
print(bool(4 == 4) == bool("4" == "4"))  # True == True -> True
print(bool(bool(None))) # False (None is False, so bool(False) -> False)

# Variable testing
x = (1 == True)     # True (because True == 1)
y = (1 == False)    # False (because False == 0)
a = True + 4        # 1 + 4 = 5
b = False + 10      # 0 + 10 = 10

print("x is", x)  
print("y is", y)  
print("a:", a)  
print("b:", b)  
