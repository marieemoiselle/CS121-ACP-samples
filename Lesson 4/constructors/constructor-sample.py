class Song:
	def __init__(self, title, genre, artist, year):
		self.title = title
		self.genre = genre
		self.artist = artist
		self.year = year
	
	def display_info(self):
		print(f"Title: {self.title}, Genre: {self.genre}, Artist: {self.artist}, Year: {self.year}")

# Create instances of Song class
song1 = Song("Te Quiero", "KPop", "KISS OF LIFE", 2024)
song2 = Song("ABCD", "KPop", "NAYEON", 2024)

# Call the display_info method for each song
song1.display_info()
song2.display_info()