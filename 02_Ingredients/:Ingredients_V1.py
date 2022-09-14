item_name = ""
item_count = 0

while item_name != "xxx":
	item_count += 1
	print("Item", item_count)
	item_name = input()
item_count -= 1
print("You have entered", item_count,"items")