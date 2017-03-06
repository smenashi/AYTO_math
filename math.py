#Math behind AYTO
import itertools

GIRLS = ["Kaylen", "Victoria", "Francesca", "Emma", "Camille", "Alyssa", "Mikala", "Julia", "Nicole", "Tori"] 
GUYS = ["Gio", "Cam", "Asaf", "John", "Prosper", "Sam", "Cameron", "Morgan", "Stephen", "Tyler"] 

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
	
	print(len(scenarios))

def calculate_odds():
	generate_scenarios()

calculate_odds()