import math_functions as math
import menus as menus

OPERATIONS: list[str] = [ # List of possible operations
	"SIN",
	"COS",
	"TAN",
	"SEC",
	"CSC",
	"COT",
]

main_menu: menus.ChoosingMenu = menus.ChoosingMenu()
main_menu.name = "main"
main_menu.title = "Main Menu"
main_menu.options = OPERATIONS
main_menu.query = "Select an operation: "

operation_menu: menus.QueryMenu = menus.QueryMenu()
operation_menu.name = "operation"
operation_menu.title = "Operation"
operation_menu.queries = ["Enter the number: "]
operation_menu.query_types = [float]

result_menu: menus.ResultMenu = menus.ResultMenu()
result_menu.name = "result"
result_menu.title = "Results"
result_menu.result_names = ["Result: ", "As fraction: "]

current_menu: menus.Menu = main_menu
current_operation: int

while True:
	match current_menu.name:
		case "main":
			current_operation = main_menu.display_menu()
			current_menu = operation_menu
		case "operation":
			number: float = operation_menu.display_menu()[0]
			res: list = [None] * 2 # first element float, second element fraction string
			
			try:
				match OPERATIONS[current_operation]:
					case "SIN":
						res[0] = math.sin_degrees(number)
						buf: list = math.sin_degrees_fraction(number)
						res[1] = str(buf[0]) if buf[1] == 1 else f"{buf[0]}/{buf[1]}"
					case "COS":
						res[0] = math.cos_degrees(number)
						buf: list = math.cos_degrees_fraction(number)
						res[1] = str(buf[0]) if buf[1] == 1 else f"{buf[0]}/{buf[1]}"
					case "SEC":
						res[0] = 1/math.cos_degrees(number)
						buf: list = math.cos_degrees_fraction(number)
						buf[0], buf[1] = buf[1], buf[0]
						res[1] = str(buf[0]) if buf[1] == 1 else f"{buf[0]}/{buf[1]}"
					# Add the other operations (tan, csc, cot)
			except:
				res = ["undefined", "undefined"]
			result_menu.results = res
			current_menu = result_menu
		case "result":
			result_menu.display_menu()
			current_menu = main_menu

	print()
