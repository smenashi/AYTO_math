#Math behind AYTO
import itertools

GIRLS = ["Kaylen", "Victoria", "Francesca", "Emma", "Camille", "Alyssa", "Mikala", "Julia", "Nicole", "Tori"] 
GUYS = ["Gio", "Cam", "Asaf", "John", "Prosper", "Sam", "Cameron", "Morgan", "Stephen", "Tyler"] 

def beam_elim(beam_list, beam_num, perm):
	# EX: beam_list = [("Kaylen", "Gio"), ("Victoria", "Cam"), ("Francesca", "Asaf"), ("Emma", "John"), 
	# ("Camille", "Prosper"), ("Alyssa", "Sam"), ("Mikala", "Cameron"), ("Julia", "Morgan"), 
	# ("Nicole", "Stephen") ("Tori", "Tyler")]
	# beam_num = 3
	# perm = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	# function returns FALSE

	match_count = 0

	for i in range(10):
		match = (GIRLS[i], GUYS[(perm[i])])
		if match == beam_list[i]:
			match_count += 1

	return match_count == beam_num

def perfectMatch(girl_index, guy_index, perm):
	#

	return perm[girl_index] == guy_index

def noMatch(girl_index, guy_index, perm):

	return perm[girl_index] != guy_index

def perm_check(perm):
	# Checks possibility of scenario against TBs and MUCs, returns TRUE or FALSE

	week1_tb = noMatch(9, 4, perm)
	week1_muc = beam_elim([("Kaylen", "Gio"), ("Victoria", "Cam"), ("Francesca", "Asaf"), ("Emma", "John"), 
						   ("Camille", "Prosper"), ("Alyssa", "Sam"), ("Mikala", "Cameron"), ("Julia", "Morgan"), 
						   ("Nicole", "Stephen"), ("Tori", "Tyler")], 3, perm)

	week2_tb = noMatch(7, 3, perm)
	week2_muc = beam_elim([("Kaylen", "Gio"), ("Victoria", "Tyler"), ("Francesca", "Sam"), ("Emma", "Prosper"), 
						   ("Camille", "Asaf"), ("Alyssa", "Morgan"), ("Mikala", "Cameron"), ("Julia", "Cam"), 
						   ("Nicole", "John"), ("Tori", "Stephen")], 3, perm)

	return week1_tb and week1_muc and week2_tb and week2_muc

def generate_scenarios():

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

	count = 0
	total = len(scenarios)
	for i in range(total):
		if scenarios[i][girl_index] == (girl, guy):
			count += 1
	odds = (count / total) * 100
	odds_string = str(odds) + "%"
	return odds_string

def generate_odds():

	scenarios = generate_scenarios()
	total = len(scenarios)

	print("~Week Two~")
	print("Number of Scenarios:", total)

	print("Kaylen_Gio =", calculate_odds(0, "Kaylen", "Gio", scenarios, total))
	print("Kaylen_Cam =", calculate_odds(0, "Kaylen", "Cam", scenarios, total)) 
	print("Kaylen_Asaf =", calculate_odds(0, "Kaylen", "Asaf", scenarios, total)) 
	print("Kaylen_John =", calculate_odds(0, "Kaylen", "John", scenarios, total)) 
	print("Kaylen_Prosper =", calculate_odds(0, "Kaylen", "Prosper", scenarios, total)) 
	print("Kaylen_Sam =", calculate_odds(0, "Kaylen", "Sam", scenarios, total)) 
	print("Kaylen_Cameron=", calculate_odds(0, "Kaylen", "Cameron", scenarios, total)) 
	print("Kaylen_Morgan =", calculate_odds(0, "Kaylen", "Morgan", scenarios, total)) 
	print("Kaylen_Stephen =", calculate_odds(0, "Kaylen", "Stephen", scenarios, total)) 
	print("Kaylen_Tyler =", calculate_odds(0, "Kaylen", "Tyler", scenarios, total)) 
	print("Victoria_Gio =", calculate_odds(1, "Victoria", "Gio", scenarios, total)) 
	print("Victoria_Cam =", calculate_odds(1, "Victoria", "Cam", scenarios, total))
	print("Victoria_Asaf =", calculate_odds(1, "Victoria", "Asaf", scenarios, total))
	print("Victoria_John =", calculate_odds(1, "Victoria", "John", scenarios, total))
	print("Victoria_Prosper =", calculate_odds(1, "Victoria", "Prosper", scenarios, total)) 
	print("Victoria_Sam =", calculate_odds(1, "Victoria", "Sam", scenarios, total)) 
	print("Victoria_Cameron =", calculate_odds(1, "Victoria", "Cameron", scenarios, total)) 
	print("Victoria_Morgan = ",calculate_odds(1, "Victoria", "Morgan", scenarios, total)) 
	print("Victoria_Stephen =", calculate_odds(1, "Victoria", "Stephen", scenarios, total)) 
	print("Victoria_Tyler =", calculate_odds(1, "Victoria", "Tyler", scenarios, total))	
	print("Francesca_Gio =", calculate_odds(2, "Francesca", "Gio", scenarios, total)) 
	print("Francesca_Cam =", calculate_odds(2, "Francesca", "Cam", scenarios, total)) 
	print("Francesca_Asaf =", calculate_odds(2, "Francesca", "Asaf", scenarios, total)) 
	print("Francesca_John =", calculate_odds(2, "Francesca", "John", scenarios, total)) 
	print("Francesca_Prosper =", calculate_odds(2, "Francesca", "Prosper", scenarios, total)) 
	print("Francesca_Sam =", calculate_odds(2, "Francesca", "Sam", scenarios, total))
	print("Francesca_Cameron =", calculate_odds(2, "Francesca", "Cameron", scenarios, total)) 
	print("Francesca_Morgan =", calculate_odds(2, "Francesca", "Morgan", scenarios, total)) 
	print("Francesca_Stephen =", calculate_odds(2, "Francesca", "Stephen", scenarios, total))
	print("Francesca_Tyler =", calculate_odds(2, "Francesca", "Tyler", scenarios, total))
	print("Emma_Gio =", calculate_odds(3, "Emma", "Gio", scenarios, total)) 
	print("Emma_Cam =", calculate_odds(3, "Emma", "Cam", scenarios, total))
	print("Emma_Asaf =", calculate_odds(3, "Emma", "Asaf", scenarios, total))
	print("Emma_John =", calculate_odds(3, "Emma", "John", scenarios, total))
	print("Emma_Prosper =", calculate_odds(3, "Emma", "Prosper", scenarios, total))
	print("Emma_Sam =", calculate_odds(3, "Emma", "Sam", scenarios, total))
	print("Emma_Cameron =", calculate_odds(3, "Emma", "Cameron", scenarios, total))
	print("Emma_Morgan =", calculate_odds(3, "Emma", "Morgan", scenarios, total))
	print("Emma_Stephen =", calculate_odds(3, "Emma", "Stephen", scenarios, total))
	print("Emma_Tyler =", calculate_odds(3, "Emma", "Tyler", scenarios, total))
	print("Camille_Gio =", calculate_odds(4, "Camille", "Gio", scenarios, total))
	print("Camille_Cam =", calculate_odds(4, "Camille", "Cam", scenarios, total))
	print("Camille_Asaf =", calculate_odds(4, "Camille", "Asaf", scenarios, total)) 
	print("Camille_John =", calculate_odds(4, "Camille", "John", scenarios, total))
	print("Camille_Prosper =", calculate_odds(4, "Camille", "Prosper", scenarios, total))
	print("Camille_Sam =", calculate_odds(4, "Camille", "Sam", scenarios, total))
	print("Camille_Cameron =", calculate_odds(4, "Camille", "Cameron", scenarios, total))
	print("Camille_Morgan =", calculate_odds(4, "Camille", "Morgan", scenarios, total))
	print("Camille_Stephen =", calculate_odds(4, "Camille", "Stephen", scenarios, total))
	print("Camille_Tyler =", calculate_odds(4, "Camille", "Tyler", scenarios, total))
	print("Alyssa_Gio =", calculate_odds(5, "Alyssa", "Gio", scenarios, total))
	print("Alyssa_Cam =", calculate_odds(5, "Alyssa", "Cam", scenarios, total))
	print("Alyssa_Asaf =", calculate_odds(5, "Alyssa", "Asaf", scenarios, total)) 
	print("Alyssa_John =", calculate_odds(5, "Alyssa", "John", scenarios, total)) 
	print("Alyssa_Prosper =", calculate_odds(5, "Alyssa", "Prosper", scenarios, total))
	print("Alyssa_Sam =", calculate_odds(5, "Alyssa", "Sam", scenarios, total))
	print("Alyssa_Cameron =", calculate_odds(5, "Alyssa", "Cameron", scenarios, total)) 
	print("Alyssa_Morgan =", calculate_odds(5, "Alyssa", "Morgan", scenarios, total))
	print("Alyssa_Stephen =", calculate_odds(5, "Alyssa", "Stephen", scenarios, total))
	print("Alyssa_Tyler =", calculate_odds(5, "Alyssa", "Tyler", scenarios, total))
	print("Mikala_Gio =", calculate_odds(6, "Mikala", "Gio", scenarios, total))
	print("Mikala_Cam =", calculate_odds(6, "Mikala", "Cam", scenarios, total))
	print("Mikala_Asaf =", calculate_odds(6, "Mikala", "Asaf", scenarios, total))
	print("Mikala_John =", calculate_odds(6, "Mikala", "John", scenarios, total))
	print("Mikala_Prosper =", calculate_odds(6, "Mikala", "Prosper", scenarios, total))
	print("Mikala_Sam =", calculate_odds(6, "Mikala", "Sam", scenarios, total))
	print("Mikala_Cameron =", calculate_odds(6, "Mikala", "Cameron", scenarios, total)) 
	print("Mikala_Morgan =", calculate_odds(6, "Mikala", "Morgan", scenarios, total)) 
	print("Mikala_Stephen =", calculate_odds(6, "Mikala", "Stephen", scenarios, total))
	print("Mikala_Tyler =", calculate_odds(6, "Mikala", "Tyler", scenarios, total))
	print("Julia_Gio =", calculate_odds(7, "Julia", "Gio", scenarios, total))
	print("Julia_Cam =", calculate_odds(7, "Julia", "Cam", scenarios, total))
	print("Julia_Asaf =", calculate_odds(7, "Julia", "Asaf", scenarios, total))
	print("Julia_John =", calculate_odds(7, "Julia", "John", scenarios, total))
	print("Julia_Prosper =", calculate_odds(7, "Julia", "Prosper", scenarios, total))
	print("Julia_Sam =", calculate_odds(7, "Julia", "Sam", scenarios, total))
	print("Julia_Cameron =", calculate_odds(7, "Julia", "Cameron", scenarios, total))
	print("Julia_Morgan =", calculate_odds(7, "Julia", "Morgan", scenarios, total))
	print("Julia_Stephen =", calculate_odds(7, "Julia", "Stephen", scenarios, total))
	print("Julia_Tyler =", calculate_odds(7, "Julia", "Tyler", scenarios, total))
	print("Nicole_Gio =", calculate_odds(8, "Nicole", "Gio", scenarios, total))
	print("Nicole_Cam =", calculate_odds(8, "Nicole", "Cam", scenarios, total))
	print("Nicole_Asaf =", calculate_odds(8, "Nicole", "Asaf", scenarios, total)) 
	print("Nicole_John =", calculate_odds(8, "Nicole", "John", scenarios, total))
	print("Nicole_Prosper =", calculate_odds(8, "Nicole", "Prosper", scenarios, total))
	print("Nicole_Sam =", calculate_odds(8, "Nicole", "Sam", scenarios, total))
	print("Nicole_Cameron =", calculate_odds(8, "Nicole", "Cameron", scenarios, total))
	print("Nicole_Morgan =", calculate_odds(8, "Nicole", "Morgan", scenarios, total))
	print("Nicole_Stephen =", calculate_odds(8, "Nicole", "Stephen", scenarios, total))
	print("Nicole_Tyler =", calculate_odds(8, "Nicole", "Tyler", scenarios, total))
	print("Tori_Gio =", calculate_odds(9, "Tori", "Gio", scenarios, total))
	print("Tori_Cam =", calculate_odds(9, "Tori", "Cam", scenarios, total))
	print("Tori_Asaf =", calculate_odds(9, "Tori", "Asaf", scenarios, total))
	print("Tori_John =", calculate_odds(9, "Tori", "John", scenarios, total)) 
	print("Tori_Prosper =", calculate_odds(9, "Tori", "Prosper", scenarios, total))
	print("Tori_Sam =", calculate_odds(9, "Tori", "Sam", scenarios, total))
	print("Tori_Cameron =", calculate_odds(9, "Tori", "Cameron", scenarios, total))
	print("Tori_Morgan =", calculate_odds(9, "Tori", "Morgan", scenarios, total))
	print("Tori_Stephen =", calculate_odds(9, "Tori", "Stephen", scenarios, total))
	print("Tori_Tyler =", calculate_odds(9, "Tori", "Tyler", scenarios, total))

generate_odds()






