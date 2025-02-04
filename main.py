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
main_menu.name = "main"
main_menu.title = "Trigonometry Calculator"
main_menu.options = OPERATIONS
main_menu.query = "Select an operation: "

operation_menu: menus.QueryMenu = menus.QueryMenu()
operation_menu.name = "operation"
operation_menu.title = "Operation"
operation_menu.queries = ["Enter the number: "]
operation_menu.query_types = [float]

# Add more menus below



# Set the current menu
current_menu: menus.Menu = operation_menu

current_operation: int

while True: # Main loop
	match current_menu.name:
		case "main":
			current_operation = current_menu.display_menu()
			current_menu = operation_menu
		case "operation":
			number: float = current_menu.display_menu()
			
			match current_operation:
				case OPERATIONS.get("SIN"):
					number = math.sin_degrees(number)
				# Do the other operations
			
			# Store the result somewhere
		case "result": pass
			# Create a new menu above named result and write the code here
