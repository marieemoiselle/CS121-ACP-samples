import csv

def main():
	try:
		with open('output.csv', 'r') as file:
			reader = csv.reader(file)
			for row in reader:
				# Perform data manipulation operations
				if row[2] == 'Programming':
					print(f"Name: {row[0]}, Degree: {row[1]}, Specialization: {row[2]}")
	except FileNotFoundError:
		print("Failed to open the file.")

if __name__ == '__main__':
	main()