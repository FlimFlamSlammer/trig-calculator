class Menu: # Main menu class inherited by all menus
	def __init__(self):
		self.title: str
		self.name: str

	def display_menu(self):
		pass

class ChoosingMenu(Menu): # Menu for choosing options
	def __init__(self):
		super()
		self.options: dict
		self.query: str

	def display_menu(self) -> int:
		# Print the title
		print(self.title)
		
		# Print all the options
		for k, v in self.options:
			print(f" [{v}] {k}")

		# Query the user
		res: int
		max_res: int = len(self.options) - 1
		while True:
			try:
				res = int(input(f" {self.query}[0-{max_res}] "))
				# Validate the given response. Throw an error if invalid
				if res < 0 or res > max_res:
					raise ValueError
			except:
				# Print an error message
				print(" Invalid option! Try again.")

			else:
				break

		# Return the response if it's valid
		return res

class QueryMenu(Menu): # Menu for entering values
	def __init__(self):
		super()
		self.queries: list[str]
		self.query_types: list[type]

	def display_menu(self) -> list:
		# Print the title
		print(self.title)

		# Query the user all the queries
		res: list = [0] * len(self.queries)
		for i in range(len(self.queries)):
			while True:
				try:
					res[i] = self.query_types[i](input(f" {self.queries[i]}"))
				except:
					print(f" Value must be a {self.query_types[i].__name__}")
				else:
					break
		# Return the answers
		return res

class ResultMenu(Menu): # Menu for displaying results
	def __init__(self):
		self.result_names: list[str]
		self.results: list[any]

	def display_menu(self) -> None:
		# Print the title
		print(self.title)
		
		# Print all result names and the result itself
		for i in range(len(self.result_names)):
			print(f" {self.result_names[i]}: {self.results[i]}")

		# Ask the user to press enter
		input(" Press ENTER to continue... ")
		return