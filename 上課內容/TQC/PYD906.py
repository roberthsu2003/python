f_name = input()
str_old = input()
str_new = input()

infile = open(f_name, 'r')
data = infile.read()

print("=== Before the replacement")
print(data)
infile.close()

print("=== After the replacement")
new_data = data.replace(str_old, str_new)
print(new_data)

outfile = open(f_name, 'w')
outfile.write(new_data)
outfile.close()