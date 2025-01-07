import csv

def main():
	try:
		with open('output.csv', 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(['Name', 'Degree', 'Specialization'])
			writer.writerow(['Fatima Marie', 'MSCS', 'Programming'])
			writer.writerow(['Jerome', 'MSIT', 'System Analysis'])
			writer.writerow(['Gerald', 'MIT', 'Web Design'])
	except IOError:
		print("Failed to open the file.")

if __name__ == '__main__':
	main()