"""""""""""""""""""""""""""""""""""""""""""""
* Math behind MTV's Are You the One?	    *
* Season 6				    *
*					    *
* Author: Sophie Menashi		    *	
*	  smenashi@hamilton.edu	            *
*					    *
* Date created: 9/13/17			    *
* Date uploaded: 11/22/17		    *
"""""""""""""""""""""""""""""""""""""""""""""

# Using itertools to generate permutations of possibly scenarios 
import itertools

GIRLS = ["Uche", "Keyana", "Nicole", "Audrey", "Jada", "Nurys", "Zoe", "Diandra", "Alexis", "Alivia", "Geles"] 
GUYS = ["Joe", "Kareem", "Michael", "Malcolm", "Ethan", "Shad", "Dmitri", "Clinton", "Keith", "Anthony", "Tyler"] 

class Color:
 	# CITE: http://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def beam_elim(beam_list, beam_num, perm):
	# EX: beam_list = [("Uche", "Joe"), ("Keyana", "Kareem"), ("Nicole", "Michael"), ("Audrey", "Malcolm"), 
	# ("Jada", "Ethan"), ("Nurys", "Shad"), ("Zoe", "Dmitri"), ("Diandra", "Clinton"), 
	# ("Nicole", "Keith") ("Alivia", "Tyler")]
	# beam_num = 3
	# perm = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	# function returns False

	match_count = 0

	for i in range(11):
		match = (GIRLS[i], GUYS[(perm[i])])
		if match == beam_list[i]:
			match_count += 1

	return match_count == beam_num

def perfectMatch(girl_index, guy_index, perm):
	# Creates restriction on acceptable perms
	# EX: perfectMatch(6, 6, perm) checks to see if the perm has 6 in the 6th spot
	# to eliminate all perms without the perfect match ("Zoe", "Dmitri")

	return perm[girl_index] == guy_index


def noMatch(girl_index, guy_index, perm):
	# Creates restriction on acceptable perms
	# EX: noMatch(9, 4, perm) checks to see if the perm has 4 in the 9th spot
	# to elimante all persm with the no match ("Alivia", "Ethan")

	return perm[girl_index] != guy_index

def perm_check(perm):
	# Checks possibility of scenario against TBs and MUs, returns True or False
	# Updated weekly

	if not noMatch(1, 4, perm):
		return False

	elif not beam_elim([("Uche", "Clinton"), ("Keyana", "Michael"), ("Nicole", "Tyler"), ("Audrey", "Shad"), 
						   ("Jada", "Ethan"), ("Nurys", "Malcolm"), ("Zoe", "Joe"), ("Diandra", "Dmitri"), 
						   ("Alexis", "Keith"), ("Alivia", "Kareem"), ("Geles", "Anthony")], 3, perm):
		return False

	elif not noMatch(10, 9, perm):
		return False

	elif not beam_elim([("Uche", "Clinton"), ("Keyana", "Michael"), ("Nicole", "Dmitri"), ("Audrey", "Joe"), 
						   ("Jada", "Ethan"), ("Nurys", "Malcolm"), ("Zoe", "Tyler"), ("Diandra", "Anthony"), 
						   ("Alexis", "Keith"), ("Alivia", "Kareem"), ("Geles", "Shad")], 1, perm):
		return False

	elif not noMatch(5, 3, perm):
		return False

	elif not beam_elim([("Uche", "Clinton"), ("Keyana", "Shad"), ("Nicole", "Tyler"), ("Audrey", "Michael"), 
						   ("Jada", "Anthony"), ("Nurys", "Dmitri"), ("Zoe", "Joe"), ("Diandra", "Keith"), 
						   ("Alexis", "Ethan"), ("Alivia", "Kareem"), ("Geles", "Malcolm")], 2, perm):
		return False

	elif not noMatch(2, 6, perm):
		return False

	elif not beam_elim([("Uche", "Clinton"), ("Keyana", "Anthony"), ("Nicole", "Ethan"), ("Audrey", "Shad"), 
						   ("Jada", "Tyler"), ("Nurys", "Keith"), ("Zoe", "Joe"), ("Diandra", "Kareem"), 
						   ("Alexis", "Dmitri"), ("Alivia", "Malcolm"), ("Geles", "Michael")], 3, perm):
		return False
    
	elif not noMatch(0, 7, perm):
		return False

	elif not beam_elim([("Uche", "Dmitri"), ("Keyana", "Tyler"), ("Nicole", "Anthony"), ("Audrey", "Shad"), 
						   ("Jada", "Clinton"), ("Nurys", "Michael"), ("Zoe", "Joe"), ("Diandra", "Malcolm"), 
						   ("Alexis", "Keith"), ("Alivia", "Kureem"), ("Geles", "Ethan")], 1, perm):
		return False

	elif not beam_elim([("Uche", "Michael"), ("Keyana", "Anthony"), ("Nicole", "Tyler"), ("Audrey", "Shad"), 
						   ("Jada", "Ethan"), ("Nurys", "Kureem"), ("Zoe", "Keith"), ("Diandra", "Dmitri"), 
						   ("Alexis", "Joe"), ("Alivia", "Malcolm"), ("Geles", "Clinton")], 4, perm):
		return False

	elif not noMatch(9, 8, perm):
		return False

	elif not beam_elim([("Uche", "Joe"), ("Keyana", "Anthony"), ("Nicole", "Tyler"), ("Audrey", "Michael"), 
						   ("Jada", "Keith"), ("Nurys", "Kureem"), ("Zoe", "Ethan"), ("Diandra", "Dmitri"), 
						   ("Alexis", "Malcolm"), ("Alivia", "Shad"), ("Geles", "Clinton")], 5, perm):
		return False	

	elif not noMatch(3, 2, perm):
		return False

	elif not beam_elim([("Uche", "Malcolm"), ("Keyana", "Michael"), ("Nicole", "Tyler"), ("Audrey", "Keith"), 
						   ("Jada", "Joe"), ("Nurys", "Kureem"), ("Zoe", "Shad"), ("Diandra", "Dmitri"), 
						   ("Alexis", "Ethan"), ("Alivia", "Anthony"), ("Geles", "Clinton")], 3, perm):
		return False

	else:
		return True


def generate_scenarios():
	# Generates all possible permutations, and then checks each perm
	# If the perm passes (as described in perm_check()), a scenario is created

	girl2guy = []
	for girl in GIRLS:
		girl_list = []
		for guy in GUYS:
			girl_list.append((girl, guy))
		girl2guy.append(girl_list)

	perms = list(itertools.permutations(range(11)))

	scenarios = []
	for i in range(len(perms)):
		if perm_check(perms[i]):
			scenario = []
			scenario.append(girl2guy[0][(perms[i][0])])
			scenario.append(girl2guy[1][(perms[i][1])])
			scenario.append(girl2guy[2][(perms[i][2])])
			scenario.append(girl2guy[3][(perms[i][3])])
			scenario.append(girl2guy[4][(perms[i][4])])
			scenario.append(girl2guy[5][(perms[i][5])])
			scenario.append(girl2guy[6][(perms[i][6])])
			scenario.append(girl2guy[7][(perms[i][7])])
			scenario.append(girl2guy[8][(perms[i][8])])
			scenario.append(girl2guy[9][(perms[i][9])])
			scenario.append(girl2guy[10][(perms[i][10])])
			scenarios.append(scenario)
	
	return scenarios

def calculate_odds(girl_index, girl, guy, scenarios, total):
	# Calculates odds of a particualr pairing by dividing the number of scenarios 
	# with that pairing by the total number of available scenarios
	# Returns string with the percent value

	count = 0
	total = len(scenarios)
	for i in range(total):
		if scenarios[i][girl_index] == (girl, guy):
			count += 1
	odds = (count / total) * 100
	
	color = Color()

	if odds == 0.0:
		odds_string = color.RED + str(odds) + "%" + color.END

	elif odds >= 35.0 and odds < 75.0:
		odds_string = color.PURPLE + str(odds) + "%" + color.END
	elif odds >= 75.0 and odds < 100.0:
		odds_string = color.DARKCYAN + str(odds) + "%" + color.END
	elif odds == 100.0:
		odds_string = color.GREEN + str(odds) + "%" + color.END
	else:
		odds_string = str(odds) + "%"
	return odds_string

	return odds_string

def print_scenarios(scenarios, color):
	# OPTIONAL: Prints out each remaining scenario in a nice format
	# Best for when there are only <10 scenarios left
	
	count = 1
	for scenario in scenarios:
		title = "Scenario " + str(count) + ":"
		print(color.BOLD + title + color.END)
		for match in scenario:
			print(match[0], "-", match[1])
		print(" ")
		count += 1



def generate_odds():
	# Generates and prints total number of scenarios and odds of each possible pairing
	
	print("~Week Eight~")
	
	scenarios = generate_scenarios()
	total = len(scenarios)

	color = Color()

	print("Number of Scenarios: " + color.BOLD + str(total) + color.END)
	print(" ")
	
	# OPTIONAL: only two remaining scenarios at this point
	print_scenarios(scenarios, color)

	print("Uche_Joe =", calculate_odds(0, "Uche", "Joe", scenarios, total))
	print("Uche_Kareem =", calculate_odds(0, "Uche", "Kareem", scenarios, total)) 
	print("Uche_Michael =", calculate_odds(0, "Uche", "Michael", scenarios, total)) 
	print("Uche_Malcolm =", calculate_odds(0, "Uche", "Malcolm", scenarios, total)) 
	print("Uche_Ethan =", calculate_odds(0, "Uche", "Ethan", scenarios, total)) 
	print("Uche_Shad =", calculate_odds(0, "Uche", "Shad", scenarios, total)) 
	print("Uche_Dmitri=", calculate_odds(0, "Uche", "Dmitri", scenarios, total)) 
	print("Uche_Clinton =", calculate_odds(0, "Uche", "Clinton", scenarios, total)) 
	print("Uche_Keith =", calculate_odds(0, "Uche", "Keith", scenarios, total)) 
	print("Uche_Anthony =", calculate_odds(0, "Uche", "Anthony", scenarios, total)) 
	print("Uche_Tyler =", calculate_odds(0, "Uche", "Tyler", scenarios, total)) 
	print("Keyana_Joe =", calculate_odds(1, "Keyana", "Joe", scenarios, total)) 
	print("Keyana_Kareem =", calculate_odds(1, "Keyana", "Kareem", scenarios, total))
	print("Keyana_Michael =", calculate_odds(1, "Keyana", "Michael", scenarios, total))
	print("Keyana_Malcolm =", calculate_odds(1, "Keyana", "Malcolm", scenarios, total))
	print("Keyana_Ethan =", calculate_odds(1, "Keyana", "Ethan", scenarios, total)) 
	print("Keyana_Shad =", calculate_odds(1, "Keyana", "Shad", scenarios, total)) 
	print("Keyana_Dmitri =", calculate_odds(1, "Keyana", "Dmitri", scenarios, total)) 
	print("Keyana_Clinton = ",calculate_odds(1, "Keyana", "Clinton", scenarios, total)) 
	print("Keyana_Keith =", calculate_odds(1, "Keyana", "Keith", scenarios, total)) 
	print("Keyana_Anthony =", calculate_odds(1, "Keyana", "Anthony", scenarios, total))	
	print("Keyana_Tyler =", calculate_odds(1, "Keyana", "Tyler", scenarios, total))
	print("Nicole_Joe =", calculate_odds(2, "Nicole", "Joe", scenarios, total)) 
	print("Nicole_Kareem =", calculate_odds(2, "Nicole", "Kareem", scenarios, total)) 
	print("Nicole_Michael =", calculate_odds(2, "Nicole", "Michael", scenarios, total)) 
	print("Nicole_Malcolm =", calculate_odds(2, "Nicole", "Malcolm", scenarios, total)) 
	print("Nicole_Ethan =", calculate_odds(2, "Nicole", "Ethan", scenarios, total)) 
	print("Nicole_Shad =", calculate_odds(2, "Nicole", "Shad", scenarios, total))
	print("Nicole_Dmitri =", calculate_odds(2, "Nicole", "Dmitri", scenarios, total)) 
	print("Nicole_Clinton =", calculate_odds(2, "Nicole", "Clinton", scenarios, total)) 
	print("Nicole_Keith =", calculate_odds(2, "Nicole", "Keith", scenarios, total))
	print("Nicole_Anthony =", calculate_odds(2, "Nicole", "Anthony", scenarios, total))
	print("Nicole_Tyler =", calculate_odds(2, "Nicole", "Tyler", scenarios, total))
	print("Audrey_Joe =", calculate_odds(3, "Audrey", "Joe", scenarios, total)) 
	print("Audrey_Kareem =", calculate_odds(3, "Audrey", "Kareem", scenarios, total))
	print("Audrey_Michael =", calculate_odds(3, "Audrey", "Michael", scenarios, total))
	print("Audrey_Malcolm =", calculate_odds(3, "Audrey", "Malcolm", scenarios, total))
	print("Audrey_Ethan =", calculate_odds(3, "Audrey", "Ethan", scenarios, total))
	print("Audrey_Shad =", calculate_odds(3, "Audrey", "Shad", scenarios, total))
	print("Audrey_Dmitri =", calculate_odds(3, "Audrey", "Dmitri", scenarios, total))
	print("Audrey_Clinton =", calculate_odds(3, "Audrey", "Clinton", scenarios, total))
	print("Audrey_Keith =", calculate_odds(3, "Audrey", "Keith", scenarios, total))
	print("Audrey_Anthony =", calculate_odds(3, "Audrey", "Anthony", scenarios, total))
	print("Audrey_Tyler =", calculate_odds(3, "Audrey", "Tyler", scenarios, total))
	print("Jada_Joe =", calculate_odds(4, "Jada", "Joe", scenarios, total))
	print("Jada_Kareem =", calculate_odds(4, "Jada", "Kareem", scenarios, total))
	print("Jada_Michael =", calculate_odds(4, "Jada", "Michael", scenarios, total)) 
	print("Jada_Malcolm =", calculate_odds(4, "Jada", "Malcolm", scenarios, total))
	print("Jada_Ethan =", calculate_odds(4, "Jada", "Ethan", scenarios, total))
	print("Jada_Shad =", calculate_odds(4, "Jada", "Shad", scenarios, total))
	print("Jada_Dmitri =", calculate_odds(4, "Jada", "Dmitri", scenarios, total))
	print("Jada_Clinton =", calculate_odds(4, "Jada", "Clinton", scenarios, total))
	print("Jada_Keith =", calculate_odds(4, "Jada", "Keith", scenarios, total))
	print("Jada_Anthony =", calculate_odds(4, "Jada", "Anthony", scenarios, total))
	print("Jada_Tyler =", calculate_odds(4, "Jada", "Tyler", scenarios, total))
	print("Nurys_Joe =", calculate_odds(5, "Nurys", "Joe", scenarios, total))
	print("Nurys_Kareem =", calculate_odds(5, "Nurys", "Kareem", scenarios, total))
	print("Nurys_Michael =", calculate_odds(5, "Nurys", "Michael", scenarios, total)) 
	print("Nurys_Malcolm =", calculate_odds(5, "Nurys", "Malcolm", scenarios, total)) 
	print("Nurys_Ethan =", calculate_odds(5, "Nurys", "Ethan", scenarios, total))
	print("Nurys_Shad =", calculate_odds(5, "Nurys", "Shad", scenarios, total))
	print("Nurys_Dmitri =", calculate_odds(5, "Nurys", "Dmitri", scenarios, total)) 
	print("Nurys_Clinton =", calculate_odds(5, "Nurys", "Clinton", scenarios, total))
	print("Nurys_Keith =", calculate_odds(5, "Nurys", "Keith", scenarios, total))
	print("Nurys_Anthony =", calculate_odds(5, "Nurys", "Anthony", scenarios, total))
	print("Nurys_Tyler =", calculate_odds(5, "Nurys", "Tyler", scenarios, total))
	print("Zoe_Joe =", calculate_odds(6, "Zoe", "Joe", scenarios, total))
	print("Zoe_Kareem =", calculate_odds(6, "Zoe", "Kareem", scenarios, total))
	print("Zoe_Michael =", calculate_odds(6, "Zoe", "Michael", scenarios, total))
	print("Zoe_Malcolm =", calculate_odds(6, "Zoe", "Malcolm", scenarios, total))
	print("Zoe_Ethan =", calculate_odds(6, "Zoe", "Ethan", scenarios, total))
	print("Zoe_Shad =", calculate_odds(6, "Zoe", "Shad", scenarios, total))
	print("Zoe_Dmitri =", calculate_odds(6, "Zoe", "Dmitri", scenarios, total)) 
	print("Zoe_Clinton =", calculate_odds(6, "Zoe", "Clinton", scenarios, total)) 
	print("Zoe_Keith =", calculate_odds(6, "Zoe", "Keith", scenarios, total))
	print("Zoe_Anthony =", calculate_odds(6, "Zoe", "Anthony", scenarios, total))
	print("Zoe_Tyler =", calculate_odds(6, "Zoe", "Tyler", scenarios, total))
	print("Diandra_Joe =", calculate_odds(7, "Diandra", "Joe", scenarios, total))
	print("Diandra_Kareem =", calculate_odds(7, "Diandra", "Kareem", scenarios, total))
	print("Diandra_Michael =", calculate_odds(7, "Diandra", "Michael", scenarios, total))
	print("Diandra_Malcolm =", calculate_odds(7, "Diandra", "Malcolm", scenarios, total))
	print("Diandra_Ethan =", calculate_odds(7, "Diandra", "Ethan", scenarios, total))
	print("Diandra_Shad =", calculate_odds(7, "Diandra", "Shad", scenarios, total))
	print("Diandra_Dmitri =", calculate_odds(7, "Diandra", "Dmitri", scenarios, total))
	print("Diandra_Clinton =", calculate_odds(7, "Diandra", "Clinton", scenarios, total))
	print("Diandra_Keith =", calculate_odds(7, "Diandra", "Keith", scenarios, total))
	print("Diandra_Anthony =", calculate_odds(7, "Diandra", "Anthony", scenarios, total))
	print("Diandra_Tyler =", calculate_odds(7, "Diandra", "Tyler", scenarios, total))
	print("Alexis_Joe =", calculate_odds(8, "Alexis", "Joe", scenarios, total))
	print("Alexis_Kareem =", calculate_odds(8, "Alexis", "Kareem", scenarios, total))
	print("Alexis_Michael =", calculate_odds(8, "Alexis", "Michael", scenarios, total)) 
	print("Alexis_Malcolm =", calculate_odds(8, "Alexis", "Malcolm", scenarios, total))
	print("Alexis_Ethan =", calculate_odds(8, "Alexis", "Ethan", scenarios, total))
	print("Alexis_Shad =", calculate_odds(8, "Alexis", "Shad", scenarios, total))
	print("Alexis_Dmitri =", calculate_odds(8, "Alexis", "Dmitri", scenarios, total))
	print("Alexis_Clinton =", calculate_odds(8, "Alexis", "Clinton", scenarios, total))
	print("Alexis_Keith =", calculate_odds(8, "Alexis", "Keith", scenarios, total))
	print("Alexis_Anthony =", calculate_odds(8, "Alexis", "Anthony", scenarios, total))
	print("Alexis_Tyler =", calculate_odds(8, "Alexis", "Tyler", scenarios, total))
	print("Alivia_Joe =", calculate_odds(9, "Alivia", "Joe", scenarios, total))
	print("Alivia_Kareem =", calculate_odds(9, "Alivia", "Kareem", scenarios, total))
	print("Alivia_Michael =", calculate_odds(9, "Alivia", "Michael", scenarios, total))
	print("Alivia_Malcolm =", calculate_odds(9, "Alivia", "Malcolm", scenarios, total)) 
	print("Alivia_Ethan =", calculate_odds(9, "Alivia", "Ethan", scenarios, total))
	print("Alivia_Shad =", calculate_odds(9, "Alivia", "Shad", scenarios, total))
	print("Alivia_Dmitri =", calculate_odds(9, "Alivia", "Dmitri", scenarios, total))
	print("Alivia_Clinton =", calculate_odds(9, "Alivia", "Clinton", scenarios, total))
	print("Alivia_Keith =", calculate_odds(9, "Alivia", "Keith", scenarios, total))
	print("Alivia_Anthony =", calculate_odds(9, "Alivia", "Anthony", scenarios, total))
	print("Alivia_Tyler =", calculate_odds(9, "Alivia", "Tyler", scenarios, total))
	print("Geles_Joe =", calculate_odds(10, "Geles", "Joe", scenarios, total))
	print("Geles_Kareem =", calculate_odds(10, "Geles", "Kareem", scenarios, total))
	print("Geles_Michael =", calculate_odds(10, "Geles", "Michael", scenarios, total))
	print("Geles_Malcolm =", calculate_odds(10, "Geles", "Malcolm", scenarios, total)) 
	print("Geles_Ethan =", calculate_odds(10, "Geles", "Ethan", scenarios, total))
	print("Geles_Shad =", calculate_odds(10, "Geles", "Shad", scenarios, total))
	print("Geles_Dmitri =", calculate_odds(10, "Geles", "Dmitri", scenarios, total))
	print("Geles_Clinton =", calculate_odds(10, "Geles", "Clinton", scenarios, total))
	print("Geles_Keith =", calculate_odds(10, "Geles", "Keith", scenarios, total))
	print("Geles_Anthony =", calculate_odds(10, "Geles", "Anthony", scenarios, total))
	print("Geles_Tyler =", calculate_odds(10, "Geles", "Tyler", scenarios, total))

generate_odds()






