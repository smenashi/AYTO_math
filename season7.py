"""""""""""""""""""""""""""""""""""""""""""""
* Math behind MTV's Are You the One?	    *
* Season 7              				    *
*					   					    *
* Author: Sophie Menashi				    *	
*	  	  smenashi@hamilton.edu 	        *
*					                        *
* Date created: 8/27/18					    *
* Date updated: 8/30/18			  		    *
"""""""""""""""""""""""""""""""""""""""""""""

# Using itertools to generate permutations of possible scenarios 
import itertools

GIRLS = ["Asia", "Bria", "Cali", "Jasmine", "Kayla", "Kenya", "Lauren", "Maria", "Morgan", "Nutsa", "Samantha"] 
GUYS = ["Andrew", "Brett", "Cam", "Daniel", "Kwasi", "Lewis", "Moe", "Shamoy", "Tevin", "Tomas", "Zak"] 

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
	# EX: beam_list = [("Asia", "Andrew"), ("Bria", "Brett"), ("Cali", "Cam"), ("Jasmine", "Daniel"), 
	# ("Kayla", "Kwasi"), ("Kenya", "Lewis"), ("Lauren", "Moe"), ("Maria", "Shamoy"), 
	# ("Cali", "Tevin") ("Nutsa", "Zak")]
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
	# to eliminate all perms without the perfect match ("Lauren", "Moe")

	return perm[girl_index] == guy_index


def noMatch(girl_index, guy_index, perm):
	# Creates restriction on acceptable perms
	# EX: noMatch(9, 4, perm) checks to see if the perm has 4 in the 9th spot
	# to elimante all persm with the no match ("Nutsa", "Kwasi")

	return perm[girl_index] != guy_index

def perm_check(perm):
	# Checks possibility of scenario against TBs and MUs, returns True or False
	# Updated weekly

 	# Week 1
	if not noMatch(7, 9, perm):
		return False

	elif not beam_elim([("Asia", "Kwasi"), ("Bria", "Zak"), ("Cali", "Brett"), ("Jasmine", "Moe"), 
						   ("Kayla", "Cam"), ("Kenya", "Tevin"), ("Lauren", "Andrew"), ("Maria", "Shamoy"), 
						   ("Morgan", "Tomas"), ("Nutsa", "Daniel"), ("Samantha", "Lewis")], 3, perm):
		return False
	
	# Week 2
	if not noMatch(0, 0, perm):
		return False

	elif not beam_elim([("Asia", "Brett"), ("Bria", "Moe"), ("Cali", "Tomas"), ("Jasmine", "Lewis"), 
						   ("Kayla", "Cam"), ("Kenya", "Tevin"), ("Lauren", "Kwasi"), ("Maria", "Shamoy"), 
						   ("Morgan", "Andrew"), ("Nutsa", "Daniel"), ("Samantha", "Zak")], 3, perm):
		return False

	# Week 3 (Perfect Match!!)
	if not perfectMatch(7, 7, perm):
		return False

	elif not beam_elim([("Asia", "Lewis"), ("Bria", "Tomas"), ("Cali", "Brett"), ("Jasmine", "Kwasi"), 
						   ("Kayla", "Cam"), ("Kenya", "Tevin"), ("Lauren", "Andrew"), ("Maria", "Shamoy"), 
						   ("Morgan", "Zak"), ("Nutsa", "Moe"), ("Samantha", "Daniel")], 3, perm):
		return False

	# Week 4 
	if not noMatch(5, 1, perm):
		return False

	elif not beam_elim([("Asia", "Cam"), ("Bria", "Kwasi"), ("Cali", "Tomas"), ("Jasmine", "Tevin"), 
						   ("Kayla", "Brett"), ("Kenya", "Lewis"), ("Lauren", "Daniel"), ("Maria", "Shamoy"), 
						   ("Morgan", "Zak"), ("Nutsa", "Andrew"), ("Samantha", "Moe")], 2, perm):
		return False

	# Week 5 
	if not noMatch(1, 10, perm):
		return False

	elif not beam_elim([("Asia", "Moe"), ("Bria", "Daniel"), ("Cali", "Tomas"), ("Jasmine", "Kwasi"), 
						   ("Kayla", "Cam"), ("Kenya", "Tevin"), ("Lauren", "Lewis"), ("Maria", "Shamoy"), 
						   ("Morgan", "Zak"), ("Nutsa", "Brett"), ("Samantha", "Andrew")], 4, perm):
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
		odds_string = color.YELLOW + str(odds) + "%" + color.END
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
	
	print("~Week Five~")
	
	scenarios = generate_scenarios()
	total = len(scenarios)

	color = Color()

	print("Number of Scenarios: " + color.BOLD + str(total) + color.END)
	print(" ")
	
	# print_scenarios(scenarios, color)

	print("Asia_Andrew =", calculate_odds(0, "Asia", "Andrew", scenarios, total))
	print("Asia_Brett =", calculate_odds(0, "Asia", "Brett", scenarios, total)) 
	print("Asia_Cam =", calculate_odds(0, "Asia", "Cam", scenarios, total)) 
	print("Asia_Daniel =", calculate_odds(0, "Asia", "Daniel", scenarios, total)) 
	print("Asia_Kwasi =", calculate_odds(0, "Asia", "Kwasi", scenarios, total)) 
	print("Asia_Lewis =", calculate_odds(0, "Asia", "Lewis", scenarios, total)) 
	print("Asia_Moe=", calculate_odds(0, "Asia", "Moe", scenarios, total)) 
	print("Asia_Shamoy =", calculate_odds(0, "Asia", "Shamoy", scenarios, total)) 
	print("Asia_Tevin =", calculate_odds(0, "Asia", "Tevin", scenarios, total)) 
	print("Asia_Tomas =", calculate_odds(0, "Asia", "Tomas", scenarios, total)) 
	print("Asia_Zak =", calculate_odds(0, "Asia", "Zak", scenarios, total)) 
	print("Bria_Andrew =", calculate_odds(1, "Bria", "Andrew", scenarios, total)) 
	print("Bria_Brett =", calculate_odds(1, "Bria", "Brett", scenarios, total))
	print("Bria_Cam =", calculate_odds(1, "Bria", "Cam", scenarios, total))
	print("Bria_Daniel =", calculate_odds(1, "Bria", "Daniel", scenarios, total))
	print("Bria_Kwasi =", calculate_odds(1, "Bria", "Kwasi", scenarios, total)) 
	print("Bria_Lewis =", calculate_odds(1, "Bria", "Lewis", scenarios, total)) 
	print("Bria_Moe =", calculate_odds(1, "Bria", "Moe", scenarios, total)) 
	print("Bria_Shamoy = ",calculate_odds(1, "Bria", "Shamoy", scenarios, total)) 
	print("Bria_Tevin =", calculate_odds(1, "Bria", "Tevin", scenarios, total)) 
	print("Bria_Tomas =", calculate_odds(1, "Bria", "Tomas", scenarios, total))	
	print("Bria_Zak =", calculate_odds(1, "Bria", "Zak", scenarios, total))
	print("Cali_Andrew =", calculate_odds(2, "Cali", "Andrew", scenarios, total)) 
	print("Cali_Brett =", calculate_odds(2, "Cali", "Brett", scenarios, total)) 
	print("Cali_Cam =", calculate_odds(2, "Cali", "Cam", scenarios, total)) 
	print("Cali_Daniel =", calculate_odds(2, "Cali", "Daniel", scenarios, total)) 
	print("Cali_Kwasi =", calculate_odds(2, "Cali", "Kwasi", scenarios, total)) 
	print("Cali_Lewis =", calculate_odds(2, "Cali", "Lewis", scenarios, total))
	print("Cali_Moe =", calculate_odds(2, "Cali", "Moe", scenarios, total)) 
	print("Cali_Shamoy =", calculate_odds(2, "Cali", "Shamoy", scenarios, total)) 
	print("Cali_Tevin =", calculate_odds(2, "Cali", "Tevin", scenarios, total))
	print("Cali_Tomas =", calculate_odds(2, "Cali", "Tomas", scenarios, total))
	print("Cali_Zak =", calculate_odds(2, "Cali", "Zak", scenarios, total))
	print("Jasmine_Andrew =", calculate_odds(3, "Jasmine", "Andrew", scenarios, total)) 
	print("Jasmine_Brett =", calculate_odds(3, "Jasmine", "Brett", scenarios, total))
	print("Jasmine_Cam =", calculate_odds(3, "Jasmine", "Cam", scenarios, total))
	print("Jasmine_Daniel =", calculate_odds(3, "Jasmine", "Daniel", scenarios, total))
	print("Jasmine_Kwasi =", calculate_odds(3, "Jasmine", "Kwasi", scenarios, total))
	print("Jasmine_Lewis =", calculate_odds(3, "Jasmine", "Lewis", scenarios, total))
	print("Jasmine_Moe =", calculate_odds(3, "Jasmine", "Moe", scenarios, total))
	print("Jasmine_Shamoy =", calculate_odds(3, "Jasmine", "Shamoy", scenarios, total))
	print("Jasmine_Tevin =", calculate_odds(3, "Jasmine", "Tevin", scenarios, total))
	print("Jasmine_Tomas =", calculate_odds(3, "Jasmine", "Tomas", scenarios, total))
	print("Jasmine_Zak =", calculate_odds(3, "Jasmine", "Zak", scenarios, total))
	print("Kayla_Andrew =", calculate_odds(4, "Kayla", "Andrew", scenarios, total))
	print("Kayla_Brett =", calculate_odds(4, "Kayla", "Brett", scenarios, total))
	print("Kayla_Cam =", calculate_odds(4, "Kayla", "Cam", scenarios, total)) 
	print("Kayla_Daniel =", calculate_odds(4, "Kayla", "Daniel", scenarios, total))
	print("Kayla_Kwasi =", calculate_odds(4, "Kayla", "Kwasi", scenarios, total))
	print("Kayla_Lewis =", calculate_odds(4, "Kayla", "Lewis", scenarios, total))
	print("Kayla_Moe =", calculate_odds(4, "Kayla", "Moe", scenarios, total))
	print("Kayla_Shamoy =", calculate_odds(4, "Kayla", "Shamoy", scenarios, total))
	print("Kayla_Tevin =", calculate_odds(4, "Kayla", "Tevin", scenarios, total))
	print("Kayla_Tomas =", calculate_odds(4, "Kayla", "Tomas", scenarios, total))
	print("Kayla_Zak =", calculate_odds(4, "Kayla", "Zak", scenarios, total))
	print("Kenya_Andrew =", calculate_odds(5, "Kenya", "Andrew", scenarios, total))
	print("Kenya_Brett =", calculate_odds(5, "Kenya", "Brett", scenarios, total))
	print("Kenya_Cam =", calculate_odds(5, "Kenya", "Cam", scenarios, total)) 
	print("Kenya_Daniel =", calculate_odds(5, "Kenya", "Daniel", scenarios, total)) 
	print("Kenya_Kwasi =", calculate_odds(5, "Kenya", "Kwasi", scenarios, total))
	print("Kenya_Lewis =", calculate_odds(5, "Kenya", "Lewis", scenarios, total))
	print("Kenya_Moe =", calculate_odds(5, "Kenya", "Moe", scenarios, total)) 
	print("Kenya_Shamoy =", calculate_odds(5, "Kenya", "Shamoy", scenarios, total))
	print("Kenya_Tevin =", calculate_odds(5, "Kenya", "Tevin", scenarios, total))
	print("Kenya_Tomas =", calculate_odds(5, "Kenya", "Tomas", scenarios, total))
	print("Kenya_Zak =", calculate_odds(5, "Kenya", "Zak", scenarios, total))
	print("Lauren_Andrew =", calculate_odds(6, "Lauren", "Andrew", scenarios, total))
	print("Lauren_Brett =", calculate_odds(6, "Lauren", "Brett", scenarios, total))
	print("Lauren_Cam =", calculate_odds(6, "Lauren", "Cam", scenarios, total))
	print("Lauren_Daniel =", calculate_odds(6, "Lauren", "Daniel", scenarios, total))
	print("Lauren_Kwasi =", calculate_odds(6, "Lauren", "Kwasi", scenarios, total))
	print("Lauren_Lewis =", calculate_odds(6, "Lauren", "Lewis", scenarios, total))
	print("Lauren_Moe =", calculate_odds(6, "Lauren", "Moe", scenarios, total)) 
	print("Lauren_Shamoy =", calculate_odds(6, "Lauren", "Shamoy", scenarios, total)) 
	print("Lauren_Tevin =", calculate_odds(6, "Lauren", "Tevin", scenarios, total))
	print("Lauren_Tomas =", calculate_odds(6, "Lauren", "Tomas", scenarios, total))
	print("Lauren_Zak =", calculate_odds(6, "Lauren", "Zak", scenarios, total))
	print("Maria_Andrew =", calculate_odds(7, "Maria", "Andrew", scenarios, total))
	print("Maria_Brett =", calculate_odds(7, "Maria", "Brett", scenarios, total))
	print("Maria_Cam =", calculate_odds(7, "Maria", "Cam", scenarios, total))
	print("Maria_Daniel =", calculate_odds(7, "Maria", "Daniel", scenarios, total))
	print("Maria_Kwasi =", calculate_odds(7, "Maria", "Kwasi", scenarios, total))
	print("Maria_Lewis =", calculate_odds(7, "Maria", "Lewis", scenarios, total))
	print("Maria_Moe =", calculate_odds(7, "Maria", "Moe", scenarios, total))
	print("Maria_Shamoy =", calculate_odds(7, "Maria", "Shamoy", scenarios, total))
	print("Maria_Tevin =", calculate_odds(7, "Maria", "Tevin", scenarios, total))
	print("Maria_Tomas =", calculate_odds(7, "Maria", "Tomas", scenarios, total))
	print("Maria_Zak =", calculate_odds(7, "Maria", "Zak", scenarios, total))
	print("Morgan_Andrew =", calculate_odds(8, "Morgan", "Andrew", scenarios, total))
	print("Morgan_Brett =", calculate_odds(8, "Morgan", "Brett", scenarios, total))
	print("Morgan_Cam =", calculate_odds(8, "Morgan", "Cam", scenarios, total)) 
	print("Morgan_Daniel =", calculate_odds(8, "Morgan", "Daniel", scenarios, total))
	print("Morgan_Kwasi =", calculate_odds(8, "Morgan", "Kwasi", scenarios, total))
	print("Morgan_Lewis =", calculate_odds(8, "Morgan", "Lewis", scenarios, total))
	print("Morgan_Moe =", calculate_odds(8, "Morgan", "Moe", scenarios, total))
	print("Morgan_Shamoy =", calculate_odds(8, "Morgan", "Shamoy", scenarios, total))
	print("Morgan_Tevin =", calculate_odds(8, "Morgan", "Tevin", scenarios, total))
	print("Morgan_Tomas =", calculate_odds(8, "Morgan", "Tomas", scenarios, total))
	print("Morgan_Zak =", calculate_odds(8, "Morgan", "Zak", scenarios, total))
	print("Nutsa_Andrew =", calculate_odds(9, "Nutsa", "Andrew", scenarios, total))
	print("Nutsa_Brett =", calculate_odds(9, "Nutsa", "Brett", scenarios, total))
	print("Nutsa_Cam =", calculate_odds(9, "Nutsa", "Cam", scenarios, total))
	print("Nutsa_Daniel =", calculate_odds(9, "Nutsa", "Daniel", scenarios, total)) 
	print("Nutsa_Kwasi =", calculate_odds(9, "Nutsa", "Kwasi", scenarios, total))
	print("Nutsa_Lewis =", calculate_odds(9, "Nutsa", "Lewis", scenarios, total))
	print("Nutsa_Moe =", calculate_odds(9, "Nutsa", "Moe", scenarios, total))
	print("Nutsa_Shamoy =", calculate_odds(9, "Nutsa", "Shamoy", scenarios, total))
	print("Nutsa_Tevin =", calculate_odds(9, "Nutsa", "Tevin", scenarios, total))
	print("Nutsa_Tomas =", calculate_odds(9, "Nutsa", "Tomas", scenarios, total))
	print("Nutsa_Zak =", calculate_odds(9, "Nutsa", "Zak", scenarios, total))
	print("Samantha_Andrew =", calculate_odds(10, "Samantha", "Andrew", scenarios, total))
	print("Samantha_Brett =", calculate_odds(10, "Samantha", "Brett", scenarios, total))
	print("Samantha_Cam =", calculate_odds(10, "Samantha", "Cam", scenarios, total))
	print("Samantha_Daniel =", calculate_odds(10, "Samantha", "Daniel", scenarios, total)) 
	print("Samantha_Kwasi =", calculate_odds(10, "Samantha", "Kwasi", scenarios, total))
	print("Samantha_Lewis =", calculate_odds(10, "Samantha", "Lewis", scenarios, total))
	print("Samantha_Moe =", calculate_odds(10, "Samantha", "Moe", scenarios, total))
	print("Samantha_Shamoy =", calculate_odds(10, "Samantha", "Shamoy", scenarios, total))
	print("Samantha_Tevin =", calculate_odds(10, "Samantha", "Tevin", scenarios, total))
	print("Samantha_Tomas =", calculate_odds(10, "Samantha", "Tomas", scenarios, total))
	print("Samantha_Zak =", calculate_odds(10, "Samantha", "Zak", scenarios, total))

generate_odds()






