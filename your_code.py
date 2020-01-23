import builtins
from support_switch_ast import switch_to_if, support_switch

def exec(script):

	script = switch_to_if(script)

	builtins.exec(script)


a, b, c = 2, 4, 5
d = None

exec("""switch a*a:
	case b:
		print("Foo")
		d = 1
		break
	case c:
		print("Bar")
		d = 2
		break

assert d == 1
""")

@support_switch
def my_function_with_switch(a: int, b: int, c: int):
	"""
	switch a:
		case b:
			return True
		case c:
			return False
	"""


assert my_function_with_switch(2*2, 4, 5)
