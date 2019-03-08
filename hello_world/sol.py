# using tabs and space as a secret enconding where each tab and apce can either be a 0 or 1


with open('hello_world.cpp', 'r') as f:
 lines = f.readlines()

a = []           
for line in lines:
 b = ''
 for c in line[2::].strip('\n'):
  b +="0" if c == " " else "1"
 a.append(b)


for line in lines:
 b = ''
 for c in line[2::].strip('\n'):
  b +="1" if c == " " else "0"
 a.append(b)

for i in a: print(i)



# gigem{0h_my_wh4t_sp4c1ng_y0u_h4v3}
