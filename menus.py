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

		
		# Print all the options


		# Query the user
		res: int
		while True:
			res = input(self.query)
			valid: bool = False
			# Validate the given response. Break if it's valid


			if (valid): break

		# Return the response if it's valid (finished)
		return res

class QueryMenu(Menu): # Menu for entering values
	def __init__(self):
		super()
		self.queries: list[str]
		self.query_types: list[type]

	def display_menu(self) -> list:
		# Print the title


		# Query the user all the queries (finished)
		res: list = [0] * len(self.queries)
		for i in range(len(self.queries)):
			while True:
				try:
					res[i] = self.query_types[i](input(self.queries[i]))
				except:
					print(f"Value must be a {self.query_types[i].__name__}")
				else:
					break
		# Return the answers in order (finished)
		return res

class ResultMenu(Menu): # Menu for displaying results
	def __init__(self):
		self.result_names: list[str]
		self.result: list[any]

	def display_menu(self) -> None:
		# Print the title

		
		# Print all result names and the result itself


		# Ask the user to press enter

		return
