animal = 'fruitbat'
def print_global():
	print('inside print_global:', animal)



def change_and_print_global():
	print('inside change_and_print_global:', animal)
	animal = 'wombat'
	print('after the change:', animal)

print('at the top level:', animal)
print_global()

change_and_print_global()