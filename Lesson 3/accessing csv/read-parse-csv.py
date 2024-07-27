import csv

def main():
	try:
		with open('data.csv', 'r') as file:
			reader = csv.reader(file)
			for row in reader:
				for item in row:
					print(item)
	except FileNotFoundError:
		print("Failed to open the file.")

if __name__ == '__main__':
	main()