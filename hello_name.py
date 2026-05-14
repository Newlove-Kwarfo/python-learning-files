
first_name = input("Type in your first name... ") #takes in user input
'''first_name = first_name.rstrip() #removes any extra spaces on the right
first_name = first_name.lstrip() #removes any extra spaces on the left'''
first_name = first_name.strip() #removes any extra spaces on the left and right

last_name = input("Type in your lastt name... ")
'''last_name = last_name.rstrip()
last_name = last_name.lstrip()'''
last_name = last_name.strip()

full_name = f"{first_name} {last_name}" #combines first_name and last_name into one variable
print(f"Hello, {full_name.title()} would you like to learn some python today?") #prints a combination of 'Hello' and full_name in title case
input('')
print("Well, I can't help you. Sorry your life sucks")