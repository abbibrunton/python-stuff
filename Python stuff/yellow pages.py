yellow_pages = {
	'Fred':7580,
	'Janet':6485,
	'Laura':9582,
	'Karen':3201,
	'Scooby Doo':9204,
	'Theresa May':8172,
	'Charles Darwin':5098,
	'Lil Wayne':6381,
	'Squidward':5163,
	'Matt Damon':2910,
	'Lucy Liu':2374,
	'Ringo Star':1928,
	'Mr T': 4832,
	'The Queen':3947,
	'Q from Steps':2841,
	'Mum':4552,
	'Jason Bourne':3917,
	'Beyonce':2871,
	'Danny Devito':2571,
	'Lisa Simpson':6754
}

names = list(yellow_pages.keys())
numbers = list(yellow_pages.values())
print(numbers[0:20:2])
print(names[-5:])