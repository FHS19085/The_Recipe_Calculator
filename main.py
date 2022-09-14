#import Ingredients_function_V2
#print(Ingredients_function_V2)

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
			
def item_name(question, error):
	valid = False
	while not valid:
		response = input(question)
		if response != "":
			return response
		else:
			print(error)

def item_cost(question):
	error = "Please enter a valid item cost above 0"
	valid = False
	while not valid:
		try:
			response = int(input(question))
			if response <= 0:
				print(error)
			else:
				return response
		except ValueError:
			print(error)


# Main Routine
item = ""
item_count = 0

Recipe = Recipe_name("Name of recipe?\n", "Please enter a valid recipe name")
print("Recipe name\n", Recipe)
print()
Servings = Serving_size("Serving size?\n")
print("Serving size", Servings)

while item != "xxx":
	item_count += 1
	item = item_name("Next item:\n", "please enter a valid item name")
	if item == "xxx":
		break
	print("Item",item_count,"is\n",item)
	cost = item_cost("Item cost:\n")
	print("Item", item_count, "cost is ${}".format(cost))
item_count -= 1
print("You have entered", item_count,"items")