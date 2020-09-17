import os
import ast

a_list = [1,2,3,4,5]
save_file = 'save_file.txt.'

# save list in file
with open(save_file, 'w') as f:
	f.write(str(a_list))

# load list from file
if os.path.exists(save_file):
	with open(save_file) as f:
		my_list = ast.literal_eval(f.read())

for x in my_list:
	print(x)
