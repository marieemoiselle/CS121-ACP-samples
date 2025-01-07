def main():
	try:
		file = open("test5.txt", "w")
		file.write("This text has been written to the file.\n")
		file.close()
		print("Data written to the file.")
	except IOError:
		print("Failed to open the file.")

if __name__ == '__main__':
	main()