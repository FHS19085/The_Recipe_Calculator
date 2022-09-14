def item_name(question, error):
	valid = False
	while not valid:
		response = input(question)
		if response != "":
			return response
		else:
			print(error)
item = ""
item_count = 0
def item_cost(question):
	error = "Please enter a valid item cost above 0"
	valid = False
	while not valid:
		try:
			response = float(input(question))
			if response <= 0:
				print(error)
			else:
				return response
		except ValueError:
			print(error)

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