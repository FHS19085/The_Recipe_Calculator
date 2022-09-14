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

while item != "xxx":
	item_count += 1
	item = item_name("Next item\n", "please enter a valid item name")
	if item == "xxx":
		break
	print("Item",item_count,"is\n",item)
item_count -= 1
print("You have entered", item_count,"items")