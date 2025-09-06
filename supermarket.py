
#NAME: DAVID WILLIAMS
#RESOURCES:
    #PROFESSOR'S VIDEOS,
    #PROFESSOR LECTURES,
    #CODEACADEMY


# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

#This is to greet our visitors and tell them the products we currently offer
print()
print()
print()

#----START OF MY CODE---------
import random

print("Welcome to the Supermarket!")
print()

print('Please see our in stock inventory below:')
constant_lottery_unit_price = 2
constant_apple_unit_price = 0.99
constant_canned_beans_unit_price = 1.58
constant_soda_unit_price = 1.23

print("– Lottery tickets cost $" + str(constant_lottery_unit_price) + " each")
print("– Apples cost $" + str(constant_apple_unit_price) + " each")
print("– Can of beans cost $" + str(constant_canned_beans_unit_price) + " each")
print("– Sodas cost $" + str(constant_soda_unit_price) + " each")
print()

#Starting budget and item purchase count
budget_total = 5
tickets_purchased = 0
lottery_winnings = 0
total_apples_purchased = 0
total_cans_of_beans_purchased = 0
total_sodas_purchased = 0

print("You currently have $" + str(round(budget_total,2)) + " available.")
print()

#Asking the customer if they would like to purchase a lottery ticket.

            
while True:
    
    choice = input("Would you like to purchase a $" + str(round(constant_lottery_unit_price,2)) + " lottery ticket for a chance of winning between $2-$10 (y/n)? ")
    if choice == 'y' or choice == 'Y':
        print('You\'ve purchased a lottery ticket. Good Luck!')
        
#Deduct cost from total budget if lottery ticket was purchased. 
        budget_total -= constant_lottery_unit_price
        tickets_purchased += 1
        lottery_result = random.randint(0,2)
        if lottery_result == 2:
            
#If the costumer wins! Display winning amount.
            lottery_winnings = random.randint(2,10)
            budget_total += lottery_winnings
            print('Congratulations! 🎉 You won the lottery and earned $' + str(round(lottery_winnings,2)) + "!")

#If the customer loses.
        else:
            print("Sorry, better luck next time.")
        break #Stopping the question after a "y" response.
    elif choice == 'n' or choice == 'N':
        print('No lottery ticket has been purchased.')
        break #Stopping the question loop after a "n" response.
#If invailid response is entered.
    else:
        print("An unrecgonized input was entered. Please try again.")
        continue
        
print()


print("You have a remaining balance of $" + str(round(budget_total,2)) + " available.")
print()

while True:
    choice = input("Would you be interested in purchasing any apples? ")

    if choice == "y" or choice == "Y":
        try:
            num_of_apples = input("How many apples would you like to purchase? ")
            apple_want = int(num_of_apples)
            apples_total_cost = apple_want * constant_apple_unit_price
            
            #Does the user have enough money?
            if budget_total >= apples_total_cost:
                budget_total -= apples_total_cost
                total_apples_purchased += apple_want
                print(str(round(apple_want,2)) + " apples have been added to your cart")
                print("Apples are $ " + str(round(constant_apple_unit_price,2)) + " each.")
                print("Your total cost is $ " + str(round(apples_total_cost,2)) + " for your " + str(round(apple_want,2)) + " apples.")
                break #Stopping the question loop
            
            else:
                print("You do not have enough money. Your balance is $" + str(round(budget_total,2)) + " and the cost is $" + str(round(apples_total_cost,2)) + ".")

        except ValueError:
            print("Sorry but it looks like you've entered an invalid number. Please enter only whole numbers.")
            continue
    elif choice == 'n' or choice == 'N':
        print('No apples were purchased. Moving on.')
        break #Stopping the question loop

    else:
        print("An unrecgonized input was entered. Please try again.")
   
print()

print("You have a remaining balance of $" + str(round(budget_total,2)) + ".")
print()

choice = input("Would you be interested in purchasing any cans of beans? ")
if choice == "y" or choice == "Y":
        if budget_total < constant_canned_beans_unit_price:
            print("You do not have enough money to purchase a single can of beans. Your balance is $" + str(round(budget_total,2)) + ".")
        else:
            while True:
                try:
                    num_of_cans_of_beans = input("How many cans of beans would you like to purchase? ")
                    cans_of_beans_want = int(num_of_cans_of_beans)
                    cans_of_beans_total_cost = cans_of_beans_want * constant_canned_beans_unit_price
        
#Does the user have enough money?
                    if budget_total >= cans_of_beans_total_cost:
                        budget_total -= cans_of_beans_total_cost
                        total_cans_of_beans_purchased += cans_of_beans_want
                    
                        print(str(round(cans_of_beans_want,2)) + " cans of beans have been added to your cart")
                        print("Cans of beans are $ " + str(round(constant_canned_beans_unit_price,2)) + " each.")
                        print("Your total cost is $ " + str(round(cans_of_beans_total_cost,2)) + " for your " + str(round(cans_of_beans_want,2)) + " cans of beans.")
                        break #moving on to the next item after this purchase.
                    else:
                        print("You do not have enough money. Your balance is $" + str(round(budget_total,2)) + " and the cost is $" + str(round(cans_of_beans_total_cost,2)) + ".")
                        continue #moving on because they dont have enough money
                except ValueError:
                    print("Sorry but it looks like you've entered an invalid number. Please enter only whole numbers.")
                    continue #prompt the question again so user can re-enter correct input
elif choice == 'n' or choice == 'N':
    print('No cans of beans were purchased. Moving on.')
else:
        print("An unrecgonized input was entered. Please try again.")
print()

print("You have a remaining balance of $" + str(round(budget_total,2)) + ".")
print()
choice = input("Would you be interested in purchasing any soda? ")
if choice == "y" or choice == "Y":
    if budget_total < constant_soda_unit_price:
        print("You do not have enough money to purchase a single soda. Your balance is $" + str(round(budget_total,2)) + ".")
    else:
        while True: #Starting the loop in case user enters invalid input.
            try:
                num_of_sodas = input("How many bottles of soda would you like to purchase? ")
                sodas_want = int(num_of_sodas)

                sodas_total_cost = sodas_want * constant_soda_unit_price

                #Does the user have enough money?
                if budget_total >= sodas_total_cost:
                    budget_total -= sodas_total_cost
                    total_sodas_purchased += sodas_want
                    print(str(round(sodas_want,2)) + " bottles of soda have been added to your cart")
                    print("Your total cost is $ " + str(round(sodas_total_cost,2)) + " for your " + str(round(sodas_want,2)) + " bottles of soda.")
                    print("Printing Shopping Summary")
                    print("You have a remaining balance of $" + str(round(budget_total,2)) + ".")
                    break #Stopping the question loop
                else:
                    print("You do not have enough money. Your balance is $" + str(round(budget_total,2)) + " and the cost is $" + str(round(sodas_total_cost,2)) + ".")
                    break
            except ValueError:
                print("Sorry but it looks like you've entered an invalid number. Please enter only whole numbers.")
                continue
elif choice == 'n' or choice == 'N':
    print('No bottles of soda were purchased. Printing Shopping Summary.')
else:
    print("An unrecgonized input was entered. Please try again.")
     
print()

print()
print()
print("Thank you for shopping with us!")
print()
print("--- Shopping Trip Summary ---")
print()
print("Remaining Balance: $" + str(round(budget_total, 2)))
print("Lottery Tickets Purchased: " + str(round(tickets_purchased,2)))
print("Lottery Winnings: $" + str(lottery_winnings))
print("Apples Purchased: " + str(total_apples_purchased))
print("Cans of Beans Purchased: " + str(total_cans_of_beans_purchased))
print("Sodas Purchased: " + str(total_sodas_purchased))
print()
print("Have a nice day!")


      
