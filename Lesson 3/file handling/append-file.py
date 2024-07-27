def main():
	try:
		file = open("test3.txt", "a")
		file.write("This text has been added to the file.\n")
		file.close()
		print("File updated successfully.")
	except IOError:
		print("Failed to open the file.")

if __name__ == '__main__':
	main()