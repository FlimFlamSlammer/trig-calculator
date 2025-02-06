PRECISION: int = 9
MAX_ERROR: float = 1e-10 # absolute error
MAX_FRACTION_ERROR: float = 0.0001 # relative error
PI: float = 3.141592653589793

SIN_TABLE: dict = {
	45.0: ["√2", 2],
	60.0: ["√3", 2],
	120.0: ["√3", 2],
	135.0: ["√2", 2],
}

TAN_TABLE: dict = {
	30.0: [1, "√3"],
	60.0: ["√3", 1],
	90.0: [],
	120.0: ["-√3", 1],
	150.0: [-1, "√3"],
}

def sign(x: float) -> int:
	if x == 0: return 0
	return int(x / abs(x))

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
	if (x + 90) % 180 == 0:
		return None
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

def approximate_fraction(x: float) -> list[int]:
	x_sign: int = sign(x)
	top: int = x_sign
	bottom: int = 1

	while abs((top/bottom) - x) > abs(x * MAX_FRACTION_ERROR):
		if abs(top/bottom) > abs(x):
			bottom += 1
		else:
			top += x_sign
	
	return [top, bottom]

def sin_degrees_fraction(x: float) -> list:
	reduced: float = (abs(x) + 179) % 360 - 179

	precomp: list = SIN_TABLE.get(abs(reduced), [])
	if len(precomp):
		res_sign: int = sign(x) * sign(reduced)
		if res_sign < 0:
			return [f"-{precomp[0]}", precomp[1]]
		return precomp
	
	approx: list[int] = approximate_fraction(sin_degrees(x))
	return approx

def cos_degrees_fraction(x: float) -> list:
	return sin_degrees_fraction(x + 90)

def tan_degrees_fraction(x: float) -> list:
	reduced: float = (abs(x) + 179) % 360 - 179

	precomp: list = TAN_TABLE.get(abs(reduced), [])
	if len(precomp):
		res_sign: int = sign(x) * sign(reduced)
		if res_sign < 0:
			return TAN_TABLE[180 - abs(reduced)]
		return precomp
	
	approx: list[int] = approximate_fraction(tan_degrees(x))
	return approx