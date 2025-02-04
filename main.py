import math_functions as math
import menus

OPERATIONS: dict = { # List of possible operations
	"SIN": 0,
	"COS": 1,
	"TAN": 2,
	"SEC": 3,
	"CSC": 4,
	"COT": 5
}

main_menu: menus.ChoosingMenu = menus.ChoosingMenu()
main_menu.title = "Trigonometry Calculator"
main_menu.options = OPERATIONS
main_menu.query = "Select an operation: "

operation_menu: menus.QueryMenu = menus.QueryMenu()
operation_menu.title = "Operation"
operation_menu.queries = ["Enter the number: "]

# Add more menus below



# Set the current menu
current_menu: menus.Menu = main_menu

current_operation: int

while True: # Main loop
	match current_menu:
		case main_menu:
			current_operation = current_menu.display_menu()
