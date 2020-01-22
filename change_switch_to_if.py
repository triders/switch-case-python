import inspect

def switch_to_if(script):

	script = script.replace('    ', '	')

	# if script.startswith('@'):
	# 	script = script[script.find('\n'):]

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

	code = inspect.getsource(func)
	print(code)
	code = code[code.find('\n')+1:]  # remove @derorator
	def_part = code[:code.find('\n')]

	print(code)
	code = code[code.find('\n')+1:]  # remove def part
	code = code.replace('	switch', 'switch') # kostili
	print(code)

	# code from docstring

	num = 0
	while num < 6:
		ind = code.find('"')
		code = code[:ind] + '' + code[ind + 1:]
		num += 1

	def_part = 'def new_func ' + def_part[def_part.find('('):]
	code = def_part + code

	code = switch_to_if(code)

	code = code.replace('\nif', '\n\tif') # kostill

	exec(code)

	return new_func


#@support_switch
def my_function_with_switch(a: int, b: int, c: int):
    """
	switch a:
		case b:
			return True
		case c:
			return False
    """

# assert my_function_with_switch(2*2, 4, 5)

