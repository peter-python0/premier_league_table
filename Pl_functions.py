import class_pl as c
#class_pl is the file
#Pl is the class in the file

object1 = c.Pl('Premier League')
#collects, parses the data in a table
object1.collect_tabulate_data()

print("We can do lots of things with the Premier League table.")
print("1: print each team along with its position")
print("2: print which teams have a positive goal difference")
print("3: print which teams have a negative goal difference")
print("4: print which teams have a zero goal difference")
print("5: print which teams can still win the league")
print("6: print which teams can still get relegated")
choice = input("Type the number of your preferred option: ")

#all functions imported from class_pl file
if choice == '1':
    object1.league_pos()
elif choice == '2':
    object1.pos_gd()
elif choice == '3':
    object1.neg_gd()
elif choice == '4':
    object1.zero_gd()
elif choice == '5':
    object1.math_poss()
elif choice == '6':
    object1.math_could_drop()
