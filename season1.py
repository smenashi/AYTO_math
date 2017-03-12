#Math behind AYTO
import itertools

GIRLS = ["Kayla", "Shanley", "Brittany", "Jacy", "Simone", "Jessica", "Paige", "Ashleigh", "Amber", "Coleysia"] 
GUYS = ["Wesley", "Ethan", "Adam", "Dre", "John", "Chris_T", "Joey", "Chris_S", "Ryan", "Dillan"] 

	
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
	# EX: beam_list = [("Kayla", "Wesley"), ("Shanley", "Ethan"), ("Brittany", "Adam"), ("Jacy", "Dre"), 
	# ("Simone", "John"), ("Jessica", "Chirs_T"), ("Paige", "Joey"), ("Ashleigh", "Chris_S"), 
	# ("Amber", "Ryan"), ("Coleysia", "Dillan")]
	# beam_num = 2
	# perm = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	# function returns FALSE

	match_count = 0

	for i in range(10):
		match = (GIRLS[i], GUYS[(perm[i])])
		if match == beam_list[i]:
			match_count += 1

	return match_count == beam_num

def perfectMatch(girl_index, guy_index, perm):
	# Creates restriction on acceptable perms
	# EX: perfectMatch(6, 6, perm) checks to see if the perm has 6 in the 6th spot
	# to eliminate all perms without the perfect match ("Paige", "Joey")

	return perm[girl_index] == guy_index

def noMatch(girl_index, guy_index, perm):
	# Creates restriction on acceptable perms
	# EX: noMatch(9, 4, perm) checks to see if the perm has 4 in the 9th spot
	# to elimante all persm with the no match ("Coleysia", "John")

	return perm[girl_index] != guy_index

def perm_check(perm):
	# Checks possibility of scenario against TBs and MUCs, returns TRUE or FALSE
	# Updated weekly

	week1_tb = noMatch(1, 5, perm)
	week1_muc = beam_elim([("Kayla", "Wesley"), ("Shanley", "Ethan"), ("Brittany", "Adam"), ("Jacy", "Dre"), 
						   ("Simone", "John"), ("Jessica", "Chirs_T"), ("Paige", "Joey"), ("Ashleigh", "Chris_S"), 
						   ("Amber", "Ryan"), ("Coleysia", "Dillan")], 2, perm)

	week2_tb = noMatch(5, 1, perm)
	week2_muc = beam_elim([("Kayla", "Ryan"), ("Shanley", "Adam"), ("Brittany", "Joey"), ("Jacy", "John"), 
						   ("Simone", "Chris_S"), ("Jessica", "Dillan"), ("Paige", "Chris_T"), ("Ashleigh", "Dre"), 
						   ("Amber", "Ethan"), ("Coleysia", "Wesley")], 4, perm)

	week3_tb = noMatch(4, 4, perm)
	week3_muc = beam_elim([("Kayla", "Ryan"), ("Shanley", "Joey"), ("Brittany", "Adam"), ("Jacy", "Wesley"), 
						   ("Simone", "Chris_T"), ("Jessica", "John"), ("Paige", "Chris_S"), ("Ashleigh", "Dre"), 
						   ("Amber", "Ethan"), ("Coleysia", "Dillan")], 2, perm)

	week4_tb = noMatch(5, 9, perm)
	week4_muc = beam_elim([("Kayla", "Ethan"), ("Shanley", "John"), ("Brittany", "Ryan"), ("Jacy", "Joey"), 
						   ("Simone", "Dre"), ("Jessica", "Wesley"), ("Paige", "Chris_S"), ("Ashleigh", "Chris_T"), 
						   ("Amber", "Adam"), ("Coleysia", "Dillan")], 2, perm)

	week5_tb1 = noMatch(7, 3, perm)
	week5_tb2 = perfectMatch(9, 9, perm)
	week5_muc = beam_elim([("Kayla", "Wesley"), ("Shanley", "Adam"), ("Brittany", "Dre"), ("Jacy", "John"), 
						   ("Simone", "Chris_S"), ("Jessica", "Joey"), ("Paige", "Chris_T"), ("Ashleigh", "Ryan"), 
						   ("Amber", "Ethan"), ("Coleysia", "Dillan")], 5, perm)

	week6_tb = perfectMatch(6, 5, perm)
	week6_muc = beam_elim([("Kayla", "Wesley"), ("Shanley", "Dre"), ("Brittany", "Chris_S"), ("Jacy", "John"), 
						   ("Simone", "Joey"), ("Jessica", "Ryan"), ("Paige", "Chris_T"), ("Ashleigh", "Adam"), 
						   ("Amber", "Ethan"), ("Coleysia", "Dillan")], 5, perm)

	week7_tb = noMatch(0, 8, perm)
	week7_muc = beam_elim([("Kayla", "Wesley"), ("Shanley", "Adam"), ("Brittany", "John"), ("Jacy", "Chris_S"), 
						   ("Simone", "Dre"), ("Jessica", "Joey"), ("Paige", "Chris_T"), ("Ashleigh", "Ryan"), 
						   ("Amber", "Ethan"), ("Coleysia", "Dillan")], 7, perm)

	return week1_tb and week1_muc and week2_tb and week2_muc and week3_tb and week3_muc and week4_tb and week4_muc and week5_tb1 and week5_tb2 and week5_muc and week6_tb and week6_muc and week7_tb and week7_muc


def generate_scenarios():
	# Generates all possible permutations, and then checks each perm
	# If the perm passes (as described in perm_check()), a scenario is created

	girl2guy = []
	for girl in GIRLS:
		girl_list = []
		for guy in GUYS:
			girl_list.append((girl, guy))
		girl2guy.append(girl_list)

	perms = list(itertools.permutations(range(10)))

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

def generate_odds():
	# Generates and prints total number of scenarios and odds of each possible pairing
	
	scenarios = generate_scenarios()
	total = len(scenarios)
	color = Color()

	print("~Week Two~")
	print("Number of Scenarios: " + color.BOLD + str(total) + color.END)
	for match in range(total):
		print(scenarios[match])


	print("Kayla_Wesley =", calculate_odds(0, "Kayla", "Wesley", scenarios, total))
	print("Kayla_Ethan =", calculate_odds(0, "Kayla", "Ethan", scenarios, total)) 
	print("Kayla_Adam =", calculate_odds(0, "Kayla", "Adam", scenarios, total)) 
	print("Kayla_Dre =", calculate_odds(0, "Kayla", "Dre", scenarios, total)) 
	print("Kayla_John =", calculate_odds(0, "Kayla", "John", scenarios, total)) 
	print("Kayla_Chris_T =", calculate_odds(0, "Kayla", "Chris_T", scenarios, total)) 
	print("Kayla_Joey=", calculate_odds(0, "Kayla", "Joey", scenarios, total)) 
	print("Kayla_Chris_S =", calculate_odds(0, "Kayla", "Chris_S", scenarios, total)) 
	print("Kayla_Ryan =", calculate_odds(0, "Kayla", "Ryan", scenarios, total)) 
	print("Kayla_Dillan =", calculate_odds(0, "Kayla", "Dillan", scenarios, total)) 
	print("Shanley_Wesley =", calculate_odds(1, "Shanley", "Wesley", scenarios, total)) 
	print("Shanley_Ethan =", calculate_odds(1, "Shanley", "Ethan", scenarios, total))
	print("Shanley_Adam =", calculate_odds(1, "Shanley", "Adam", scenarios, total))
	print("Shanley_Dre =", calculate_odds(1, "Shanley", "Dre", scenarios, total))
	print("Shanley_John =", calculate_odds(1, "Shanley", "John", scenarios, total)) 
	print("Shanley_Chris_T =", calculate_odds(1, "Shanley", "Chris_T", scenarios, total)) 
	print("Shanley_Joey =", calculate_odds(1, "Shanley", "Joey", scenarios, total)) 
	print("Shanley_Chris_S = ",calculate_odds(1, "Shanley", "Chris_S", scenarios, total)) 
	print("Shanley_Ryan =", calculate_odds(1, "Shanley", "Ryan", scenarios, total)) 
	print("Shanley_Dillan =", calculate_odds(1, "Shanley", "Dillan", scenarios, total))	
	print("Brittany_Wesley =", calculate_odds(2, "Brittany", "Wesley", scenarios, total)) 
	print("Brittany_Ethan =", calculate_odds(2, "Brittany", "Ethan", scenarios, total)) 
	print("Brittany_Adam =", calculate_odds(2, "Brittany", "Adam", scenarios, total)) 
	print("Brittany_Dre =", calculate_odds(2, "Brittany", "Dre", scenarios, total)) 
	print("Brittany_John =", calculate_odds(2, "Brittany", "John", scenarios, total)) 
	print("Brittany_Chris_T =", calculate_odds(2, "Brittany", "Chris_T", scenarios, total))
	print("Brittany_Joey =", calculate_odds(2, "Brittany", "Joey", scenarios, total)) 
	print("Brittany_Chris_S =", calculate_odds(2, "Brittany", "Chris_S", scenarios, total)) 
	print("Brittany_Ryan =", calculate_odds(2, "Brittany", "Ryan", scenarios, total))
	print("Brittany_Dillan =", calculate_odds(2, "Brittany", "Dillan", scenarios, total))
	print("Jacy_Wesley =", calculate_odds(3, "Jacy", "Wesley", scenarios, total)) 
	print("Jacy_Ethan =", calculate_odds(3, "Jacy", "Ethan", scenarios, total))
	print("Jacy_Adam =", calculate_odds(3, "Jacy", "Adam", scenarios, total))
	print("Jacy_Dre =", calculate_odds(3, "Jacy", "Dre", scenarios, total))
	print("Jacy_John =", calculate_odds(3, "Jacy", "John", scenarios, total))
	print("Jacy_Chris_T =", calculate_odds(3, "Jacy", "Chris_T", scenarios, total))
	print("Jacy_Joey =", calculate_odds(3, "Jacy", "Joey", scenarios, total))
	print("Jacy_Chris_S =", calculate_odds(3, "Jacy", "Chris_S", scenarios, total))
	print("Jacy_Ryan =", calculate_odds(3, "Jacy", "Ryan", scenarios, total))
	print("Jacy_Dillan =", calculate_odds(3, "Jacy", "Dillan", scenarios, total))
	print("Simone_Wesley =", calculate_odds(4, "Simone", "Wesley", scenarios, total))
	print("Simone_Ethan =", calculate_odds(4, "Simone", "Ethan", scenarios, total))
	print("Simone_Adam =", calculate_odds(4, "Simone", "Adam", scenarios, total)) 
	print("Simone_Dre =", calculate_odds(4, "Simone", "Dre", scenarios, total))
	print("Simone_John =", calculate_odds(4, "Simone", "John", scenarios, total))
	print("Simone_Chris_T =", calculate_odds(4, "Simone", "Chris_T", scenarios, total))
	print("Simone_Joey =", calculate_odds(4, "Simone", "Joey", scenarios, total))
	print("Simone_Chris_S =", calculate_odds(4, "Simone", "Chris_S", scenarios, total))
	print("Simone_Ryan =", calculate_odds(4, "Simone", "Ryan", scenarios, total))
	print("Simone_Dillan =", calculate_odds(4, "Simone", "Dillan", scenarios, total))
	print("Jessica_Wesley =", calculate_odds(5, "Jessica", "Wesley", scenarios, total))
	print("Jessica_Ethan =", calculate_odds(5, "Jessica", "Ethan", scenarios, total))
	print("Jessica_Adam =", calculate_odds(5, "Jessica", "Adam", scenarios, total)) 
	print("Jessica_Dre =", calculate_odds(5, "Jessica", "Dre", scenarios, total)) 
	print("Jessica_John =", calculate_odds(5, "Jessica", "John", scenarios, total))
	print("Jessica_Chris_T =", calculate_odds(5, "Jessica", "Chris_T", scenarios, total))
	print("Jessica_Joey =", calculate_odds(5, "Jessica", "Joey", scenarios, total)) 
	print("Jessica_Chris_S =", calculate_odds(5, "Jessica", "Chris_S", scenarios, total))
	print("Jessica_Ryan =", calculate_odds(5, "Jessica", "Ryan", scenarios, total))
	print("Jessica_Dillan =", calculate_odds(5, "Jessica", "Dillan", scenarios, total))
	print("Paige_Wesley =", calculate_odds(6, "Paige", "Wesley", scenarios, total))
	print("Paige_Ethan =", calculate_odds(6, "Paige", "Ethan", scenarios, total))
	print("Paige_Adam =", calculate_odds(6, "Paige", "Adam", scenarios, total))
	print("Paige_Dre =", calculate_odds(6, "Paige", "Dre", scenarios, total))
	print("Paige_John =", calculate_odds(6, "Paige", "John", scenarios, total))
	print("Paige_Chris_T =", calculate_odds(6, "Paige", "Chris_T", scenarios, total))
	print("Paige_Joey =", calculate_odds(6, "Paige", "Joey", scenarios, total)) 
	print("Paige_Chris_S =", calculate_odds(6, "Paige", "Chris_S", scenarios, total)) 
	print("Paige_Ryan =", calculate_odds(6, "Paige", "Ryan", scenarios, total))
	print("Paige_Dillan =", calculate_odds(6, "Paige", "Dillan", scenarios, total))
	print("Ashleigh_Wesley =", calculate_odds(7, "Ashleigh", "Wesley", scenarios, total))
	print("Ashleigh_Ethan =", calculate_odds(7, "Ashleigh", "Ethan", scenarios, total))
	print("Ashleigh_Adam =", calculate_odds(7, "Ashleigh", "Adam", scenarios, total))
	print("Ashleigh_Dre =", calculate_odds(7, "Ashleigh", "Dre", scenarios, total))
	print("Ashleigh_John =", calculate_odds(7, "Ashleigh", "John", scenarios, total))
	print("Ashleigh_Chris_T =", calculate_odds(7, "Ashleigh", "Chris_T", scenarios, total))
	print("Ashleigh_Joey =", calculate_odds(7, "Ashleigh", "Joey", scenarios, total))
	print("Ashleigh_Chris_S =", calculate_odds(7, "Ashleigh", "Chris_S", scenarios, total))
	print("Ashleigh_Ryan =", calculate_odds(7, "Ashleigh", "Ryan", scenarios, total))
	print("Ashleigh_Dillan =", calculate_odds(7, "Ashleigh", "Dillan", scenarios, total))
	print("Amber_Wesley =", calculate_odds(8, "Amber", "Wesley", scenarios, total))
	print("Amber_Ethan =", calculate_odds(8, "Amber", "Ethan", scenarios, total))
	print("Amber_Adam =", calculate_odds(8, "Amber", "Adam", scenarios, total)) 
	print("Amber_Dre =", calculate_odds(8, "Amber", "Dre", scenarios, total))
	print("Amber_John =", calculate_odds(8, "Amber", "John", scenarios, total))
	print("Amber_Chris_T =", calculate_odds(8, "Amber", "Chris_T", scenarios, total))
	print("Amber_Joey =", calculate_odds(8, "Amber", "Joey", scenarios, total))
	print("Amber_Chris_S =", calculate_odds(8, "Amber", "Chris_S", scenarios, total))
	print("Amber_Ryan =", calculate_odds(8, "Amber", "Ryan", scenarios, total))
	print("Amber_Dillan =", calculate_odds(8, "Amber", "Dillan", scenarios, total))
	print("Coleysia_Wesley =", calculate_odds(9, "Coleysia", "Wesley", scenarios, total))
	print("Coleysia_Ethan =", calculate_odds(9, "Coleysia", "Ethan", scenarios, total))
	print("Coleysia_Adam =", calculate_odds(9, "Coleysia", "Adam", scenarios, total))
	print("Coleysia_Dre =", calculate_odds(9, "Coleysia", "Dre", scenarios, total)) 
	print("Coleysia_John =", calculate_odds(9, "Coleysia", "John", scenarios, total))
	print("Coleysia_Chris_T =", calculate_odds(9, "Coleysia", "Chris_T", scenarios, total))
	print("Coleysia_Joey =", calculate_odds(9, "Coleysia", "Joey", scenarios, total))
	print("Coleysia_Chris_S =", calculate_odds(9, "Coleysia", "Chris_S", scenarios, total))
	print("Coleysia_Ryan =", calculate_odds(9, "Coleysia", "Ryan", scenarios, total))
	print("Coleysia_Dillan =", calculate_odds(9, "Coleysia", "Dillan", scenarios, total))

generate_odds()






