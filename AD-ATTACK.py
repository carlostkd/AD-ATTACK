def print_banner():
    print("++++++++++AD Simple Attack Generator++++++++")
    print('Written by: carlostkd')   
    
    
print_banner()

count = 1
first_names = []
last_names = []

print("############################################")
print(" When you type the name, Caps will be ignored.")

while True:                                  
    print("#######################################")

    print("Possible User #", count)
    first_names.append(input("First Name >"))
    last_names.append(input("Last Name  >"))
    
    while True:                             
        res = input("do you want to add more users? (y/n)")
        if res == "y" or res == "n":
            break
        else:
            print("Type either 'y' or 'n'!")
    if res == "n":
        break

    count += 1

users = []
for indx, user in enumerate(first_names):   
    first_name = user.lower()               
    last_name = last_names[indx].lower()
    users.append(first_name + " " + last_name)

wordlist = []

def complete_names():
    for item in users:
        wordlist.append(item.replace(" ", ""))      
        wordlist.append(item.replace(" ", "."))     
        wordlist.append(item.replace(" ", "-"))     


def initial_of_first():
    for item in users:
        split = item.split()
        split[0] = split[0][:1]
        wordlist.append(split[0]+split[1])          
        wordlist.append(split[0] + "." + split[1])  
        wordlist.append(split[0] + "-" + split[1])  


def first_three():
    for item in users:
        split = item.split()
        split[0] = split[0][:3]
        split[1] = split[1][:3]
        wordlist.append(split[0] + split[1])        
        wordlist.append(split[0] + "." + split[1])  
        wordlist.append(split[0] + "-" + split[1])  

def write_list():
    with open("user_list.txt", "w") as f:
        for word in wordlist:
            f.write("%s\n" % word)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("###     Generating Wordlist for Users:   ###")

for user in users:
    print(user)

complete_names()
initial_of_first()
first_three()
print("###   Saving Wordlist to user_list.txt   ###")
write_list()
print("### Done, user your wordlist with GetNPUsers.py         ###")
