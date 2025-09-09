import random

num_friends = int(input("Enter the number of friends joining (including you):\n> "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    
    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0
    
    total_bill = float(input("Enter the total bill value:\n"))
    
    split_amount = round(total_bill / num_friends, 2)
    
    for friend in friends_dict:
        friends_dict[friend] = split_amount
    
    use_lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    
    if use_lucky_feature == "Yes":
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")
        
        if num_friends > 1:
            new_split = round(total_bill / (num_friends - 1), 2)
        else:
            new_split = 0
            
        for friend in friends_dict:
            if friend == lucky_one:
                friends_dict[friend] = 0
            else:
                friends_dict[friend] = new_split
    else:
        print("No one is going to be lucky")
    
    print(friends_dict)
