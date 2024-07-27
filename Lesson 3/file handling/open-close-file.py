def main():
	try:
		file = open("test1.txt", "r")
		print("File opened successfully.")
		# Perform operations on the file
		file.close()
	except IOError:
		print("Failed to open the file.")

if __name__ == '__main__':
	main()