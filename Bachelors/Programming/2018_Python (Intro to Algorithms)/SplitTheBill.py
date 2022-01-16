#purpose: this program calculates how much each person has to pay on the
   #specific bill with the indicated tip
#input: user enters the total bill amount they have to pay, the tip they
   #want to leave and the amount of people that are splitting the bill
#post condition: the program prints out the amount in dollars that
   #each person has to pay
#assumptions: For the bill amount user enters positive number,
   #For the tip percent and number of people user enters integer number

bill_amount=float(input("Enter the bill amount \n"))
tip_percent=int(input("Enter a tip percent as a whole number (not decimal) \n"))
number_of_people=int(input("Enter the amount of people\n"))

pay=((bill_amount*(tip_percent/100))+bill_amount)/number_of_people
pay=round(pay, 2)

print("Each person has to pay $",pay,)

#Test cases
  #Enters: bill_amount - 100, tip_percent - 18, amount_of_people - 5      Expect:23,6
  #Enters: bill_amount - 100.2, tip_percent - 18, amount_of_people - 5    Expect:23,65
  #Enters: bill_amount - 100, tip_percent - 18.2, amount_of_people - 5    Expect:Value Error
  #Enters: bill_amount - 100, tip_percent - 18, amount_of_people - 5.2    Expect:Value Error
  #Enters: bill_amount - 0, tip_percent - 0, amount_of_people - 0         Expect:Zero Devision Error
  #Enters: bill_amount - 0, tip_percent - 0, amount_of_people - 5         Expect:0
  #Enters: bill_amount - A, tip_percent - 18, amount_of_people - 5        Expect:ValueError
  #Enters: bill_amount - -1, tip_percent - 18, amount_of_people - 5       Expect:-0.24

#the last test case kind of makes sence. If you enter negative amount it is like someone has to pay you
  

