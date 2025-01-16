class Artist:
	def make_art(self):
		print("Some generic art.")

class Singer(Artist):
	def sing(self):
		print("The singer sings a song")

# Create instances of Artist and Singer classes
generic_artist = Artist()
singer = Singer()

# Call methods from both classes
generic_artist.make_art()
singer.make_art()
singer.sing()