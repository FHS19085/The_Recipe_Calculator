recipe_name = ""
servings = ""

while recipe_name == "" or servings == "":
	recipe_name = input("Name of recipe?\n")
	servings = int(input("Serving size?\n"))
	if servings <= 0:
		print("Invalid serving size")
		servings = ""
	elif servings > 50:
		print("Invalid serving size")
		servings = ""
	if recipe_name and servings != "":
		print("Recipe name\n",recipe_name)
		print("Serving size\n",servings)
		break
	else:
		print("Please enter a valid recipe name and serving size")
		print()