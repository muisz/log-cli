import sys
import json
import os

## 
## python version: 3.x
##

def get_args():
	args = sys.argv
	return args[1:]

def get_file_content(file_path):
	result = None
	with open(file_path, 'r') as file:
		result = file.read()
	return result

def read_as_json(data):
	data_list = data.split('\n')
	result = []
	for item in data_list:
		temp = {
			'log': item
		}
		result.append(temp)
	return result

def check_directory(path):
	if not os.path.exists(path):
		os.makedirs(path)

def save_to_file(path, data):
	file_location = get_file_location(path)
	check_directory(file_location)
	with open(path, 'w') as file:
		if path.endswith('.json'):
			file.write(json.dumps(data))
		else:
			file.write(data)

def get_file_location(path):
	paths = path.split('/')
	return str(os.sep).join(p for p in paths[:len(paths) -1])

def main():
	try:
		args = get_args()
		output = 'text'
		save_log = None
		output_key = '-t'
		output_file_key = '-o'
		help_key = '-h'

		if help_key in args:
			print('usage:\n\tpython3 main.py <logfile> [-h] [-t <format>] [-o <output file>]')
			print('valid format:\n\tJSON or text')
			sys.exit(0)

		if output_key in args:
			t_index = args.index(output_key)
			output_value = args[t_index + 1]
			output = output_value

		if output_file_key in args:
			f_index = args.index(output_file_key)
			file_value = args[f_index + 1]
			save_log = file_value

		file_content = get_file_content(args[0])
		result = None
		if output == 'text':
			result = file_content

		elif output == "JSON":
			result = read_as_json(file_content)

		else:
			print("invalid format value of ", output)
			sys.exit(1)

		if not save_log:
			print(result)
			sys.exit(0)

		save_to_file(save_log, result)

	except Exception as e:
		print('error: ', str(e))


if __name__ == '__main__':
	main()