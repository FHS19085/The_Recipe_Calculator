import Ingredients_function_V2
print(Ingredients_function_V2)

# Functions
def Recipe_name(question, error):
	valid = False
	while not valid:
		response = input(question)
		if response != "":
			return response
		else:
			print(error)
def Serving_size(question):
	error = "Invalid serving size"
	valid = False
	while not valid:
		try:
			response = int(input(question))
			if response <= 0:
				print(error)
			elif response > 50:
				print(error)
			else:
				return response
		except ValueError:
			print(error)


# Main Routine
Recipe = Recipe_name("Name of recipe?\n", "Please enter a valid recipe name")
print("Recipe name\n", Recipe)
print()
Servings = Serving_size("Serving size?\n")
print("Serving size", Servings)