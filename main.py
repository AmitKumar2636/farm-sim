import os

def check_save_exists():
	if (os.path.exists("slot1.txt") or 
		os.path.exists("slot2.txt") or 
		os.path.exists("slot3.txt") or 
		os.path.exists("slot4.txt")):
		return True
	return False

def save_game(slot_number, player_name):
	filename = f"slot{slot_number}.txt"
	with open(filename, "w") as file:
		file.write(player_name)
	print(f"Game successfully saved to {filename}.")
def delete_menu():
	for i in range(1,5):
		print(f"{i}. slot {i}.txt")
	print("5. cancel")
	choice=input("select an option")
	if choice=="5":
		return "mainmenu"
	if choice in ["1","2","3","4"]:
		filename=f"slot{choice}.txt"
		print(f"Would you like to delete {filename}")
		choice=input("select y/n")
		if choice=="y":
			try:
				os.remove(filename)
				print("successfully deleted the file")

			except FileNotFoundError:
				print("the file is already deleted")
			return "mainmenu"
		else:
			print(f"{filename} was not deleted")
			return "mainmenu"
	else:
		print("invalid choice")
		return "mainmenu"
def main_menu():
	has_save = check_save_exists()
	print("Main Menu ")
	if has_save:
		print("1. Continue")
		print("2. Save")
		print("3. Delete")
		print("4. Help")
		print("5. Credits")
		print("6. Exit")
	else:
		print("1. New Game")
		print("2. Help")
		print("3. Credits")
		print("4. Exit")

	choice = input("Please choose an option: ").strip()

	if has_save:
		match choice:
			case "1": return "agriculturemenu"
			case "2": return "saveslotmenu"
			case "3": 
				return "deletemenu"

			case "4": 
				print("This is a farm simulator.")
				return "mainmenu"
			case "5": 
				print("Designed by Kavya.")
				return "mainmenu"
			case "6": return "exit"
			case _:
				print("Invalid choice.")
				return "mainmenu"
	else:
		match choice:
			case "1": return "saveslotmenu"
			case "2": 
				print("This is a farm simulator.")
				return "mainmenu"
			case "3": 
				print("Designed by Kavya.")
				return "mainmenu"
			case "4": return "exit"
			case _:
				print("Invalid choice.")
				return "mainmenu"

def save_slot_menu():
	print(" Save Slot Selection ")
	name = input("Enter your name: ")
	print("1. Slot 1")
	print("2. Slot 2")
	print("3. Slot 3")
	print("4. Slot 4")
	slot = input("Select a slot: ").strip()

	match slot:
		case "1": save_game("1", name)
		case "2": save_game("2", name)
		case "3": save_game("3", name)
		case "4": save_game("4", name)
		case _:
			print("Invalid choice.")
			return "saveslotmenu"
	return "agriculturemenu"

def agriculture_menu():
	print(" Agriculture Building")
	print("1. Ranch")
	print("2. Cropland")
	print("3. Go to main menu")
	choice = input("Select an option: ").strip()

	match choice:
		case "1": return "ranchmenu"
		case "2": return "cropland"
		case "3": return "mainmenu"
		case _:
			print("Invalid choice.")
			return "agriculturemenu"

def ranch_menu():
	menu_items=["Buy","sell","housing","storage","status","End turn","go back"]
	print("The Ranch ")
	for index, item in enumerate(menu_items,start=1):
		print(str(index)+"."+item)
	choice = input("Select an option: ").strip()

	match choice:
		case "1":
			print("In development.")
			return "ranchmenu"
		case "2":
			print("In development.")
			return "ranchmenu"
		case "3":
			print("In development.")
			return "ranchmenu"
		case "4":
			print("In development.")
			return "ranchmenu"
		
		case "5":
			print("In development.")
			return "ranchmenu"
		
		case "6":
			print("In development.")
			return "ranchmenu"
		
		
		case "7": return "agriculturemenu"
		case _:
			print("Invalid choice.")
			return "ranchmenu"

current_state = "mainmenu"
print("Welcome to Farm Simulator!")

while current_state != "exit":
	match current_state:
		case "mainmenu":
			current_state = main_menu()
		case "saveslotmenu":
			current_state = save_slot_menu()
		case "agriculturemenu":
			current_state = agriculture_menu()
		case "ranchmenu":
			current_state = ranch_menu()
		case "cropland":
			print("Cropland is under development.")
			current_state = "agriculturemenu"
		case "deletemenu":
			current_state=delete_menu()
		case _:
			print("Unknown State.")
			current_state = "exit"

