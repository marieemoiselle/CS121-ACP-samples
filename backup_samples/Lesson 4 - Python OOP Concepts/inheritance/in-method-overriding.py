# Superclass
class Artist:
    def make_art(self):
        print("The artist makes art.")

# Subclass overriding the make_art() method
class Painter(Artist):
    def make_art(self):
        print("Painting...")