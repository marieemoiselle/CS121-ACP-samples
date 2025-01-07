import os

def main():
	try:
		os.remove("test4.txt")
		print("File deleted successfully.")
	except FileNotFoundError:
		print("Failed to delete the file.")

if __name__ == '__main__':
	main()