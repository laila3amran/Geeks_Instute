#Challenge1
# number = int(input("Enter a number :"))
# length = int(input("Enter the length of the list :"))

# list_of_multiples=[]
# for i in range(length):
#     num = number * (i + 1)
#     list_of_multiples.append(num)

# print(list_of_multiples)


#challenge2 

string_name = str(input("Enter a random alphabets:"))
new_string=""
for i in range(len(string_name)):
    if new_string == "":
        new_string += string_name[i]
    elif string_name[i] != string_name[i-1]:
        new_string += string_name[i]
    elif string_name[i] == string_name[i-1]:
        continue
print(new_string)
        
    