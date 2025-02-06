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

# Add ResultsMenu here




current_menu: menus.Menu = operation_menu
current_operation: int

while True:
	match current_menu.name:
		case "main":
			current_operation = current_menu.display_menu()
			current_menu = operation_menu
		case "operation":
			number: float = current_menu.display_menu()
			res: list # first element float, second element fraction string
			
			try:
				match current_operation:
					case OPERATIONS.get("SIN"):
						res[0] = math.sin_degrees(number)
						buf: list = math.sin_degrees_fraction(number)
						res[1] = str(buf[0]) if buf[1] == 1 else f"{buf[0]}/{buf[1]}"
					case OPERATIONS.get("COS"):
						res[0] = math.cos_degrees(number)
						buf: list = math.cos_degrees_fraction(number)
						res[1] = str(buf[0]) if buf[1] == 1 else f"{buf[0]}/{buf[1]}"
					case OPERATIONS.get("SEC"):
						res[0] = 1/math.cos_degrees(number)
						buf: list = math.cos_degrees_fraction(number)
						buf = [buf[1], buf[0]]
						res[1] = str(buf[0]) if buf[1] == 1 else f"{buf[0]}/{buf[1]}"
					# Do the other operations (tan, csc, cot)
			except:
				res = ["MATH ERROR!", "MATH ERROR!"]
			
			# Store the result somewhere
		case "result": pass
			# Create a new ResultsMenu above named result and write the code here
