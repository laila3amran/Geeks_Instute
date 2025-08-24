# Keep asking the name until the correct one is given
my_name = "Imran"   # you can change this to your own name

while True:
    name = input("Enter your name: ")
    if name == my_name:
        print("Hello,", my_name)
        break
