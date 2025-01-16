def main():
	try:
		file = open("test2.txt", "r")
		line = file.readline()
		print("Read from file:", line)
		file.close()
	except IOError:
		print("Failed to open the file.")

if __name__ == '__main__':
	main()