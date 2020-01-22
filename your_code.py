import builtins
from change_switch_to_if import switch_to_if

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