import json
from user import user
from readfile import read_file
from writefile import write_file
file_path = 'users.json'

# call user function
data_1 = user("Abdulhameed Yunusa", 1)
data_2 = user("Abdulhameed Yunusa", 2)
data_3 = user("Abdulhameed Yunusa", 3)
data_4 = user("Abdulhameed Yunusa", 4)

# write to file
write_file(file_path, data_1)
write_file(file_path, data_2)
write_file(file_path, data_3)
write_file(file_path, data_4)

read_data = read_file(file_path)
print(read_data)
