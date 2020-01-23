import ast, astunparse
import inspect


def switch_to_if(script):

	script = script.replace('    ', '	')

	if not script.startswith('\n'):
		script = '\n' + script

	# split by "\nswitch"

	code = script.split('\nswitch')
	
	# split by "\tcase"

	new_code = []
	for piece in code:
		new_code.append(piece.split('\tcase'))
	code = new_code 

	# remove breaks (kostili)

	new_code = []
	for i in code:
		tmp = []
		for j in i:
			tmp.append(j.replace('break', ''))
		new_code.append(tmp)
	code = new_code

	# add ifs

	new_code = code[0][0]

	for i in range(1, len(code)):
		prefix = '\nif' + code[i][0][:code[i][0].find('\n') - 1] + ' =='
		for j in range(1, len(code[1])):
			end = code[i][j]
			new_code += prefix + end 

	return new_code


def support_switch(func):
	""" IN PROCESS. NOT WORKING """

	code = inspect.getsource(func)
	code = code.replace('	switch', 'switch') # kostili
	code = code[code.find('\n')+1:]  # remove @derorator
	# code from docstring

	num = 0
	while num < 6:
		ind = code.find('"')
		code = code[:ind] + '' + code[ind + 1:]
		num += 1

	new_code = switch_to_if(code)
	new_code = new_code.replace('\nif', '\n\tif') # kostill

	tree = ast.parse(new_code)
	tree.body[0].name = 'new_func'


	# print(ast.dump(tree))
	# print(astunparse.unparse(tree))

	exec(compile(tree, filename="<ast>", mode="exec"))

	return new_func


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
