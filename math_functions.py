PRECISION: int = 9
MAX_ERROR: float = 1e-10 # absolute error
MAX_FRACTION_ERROR: float = 0.0001 # relative error
PI: float = 3.141592653589793

def factorial(x: float) -> float:
	result: float = 1.0
	for i in range(x, 1, -1):
		result *= i
	return result

def to_degrees(x: float) -> float:
	return x * 180 / PI

def to_radians(x: float) -> float:
	return x * PI / 180

# Taylor Series approximation of the sine function, where x is in radians.
def sin(x: float) -> float:
	exponent: int = 1
	result: float = 0.0
	taylor_res: float = x

	while abs(taylor_res) > MAX_ERROR:
		result += taylor_res
		taylor_res *= -(x ** 2) / ((exponent + 1) * (exponent + 2))
		exponent += 2
	return round(result, PRECISION)

# Taylor Series approximation of the cosine function, where x is in radians.
def cos(x: float) -> float:
	exponent: int = 0
	result: float = 0.0
	taylor_res: float = 1.0

	while abs(taylor_res) > MAX_ERROR:
		result += taylor_res
		taylor_res *= -(x ** 2) / ((exponent + 1) * (exponent + 2))
		exponent += 2
	return round(result, PRECISION)

def tan(x: float) -> float:
	return round(sin(x) / cos(x), PRECISION)

def sin_degrees(x: float) -> float:
	reduced: float = (abs(x) + 179) % 360 - 179
	result: float = sin(to_radians(reduced))
	if x < 0:
		result = -result
	return result

def cos_degrees(x: float) -> float:
	reduced: float = (abs(x) + 179) % 360 - 179
	result: float = cos(to_radians(reduced))
	return result

def tan_degrees(x: float) -> float:
	return round(sin_degrees(x) / cos_degrees(x), PRECISION)

def approximate_fraction(x: float) -> list:
	sign: int = int(x / abs(x))
	top: int = sign
	bottom: int = 1

	while abs((top/bottom) - x) > abs(x * MAX_FRACTION_ERROR):
		if abs(top/bottom) > abs(x):
			bottom += 1
		else:
			top += sign
	
	return [top, bottom]
