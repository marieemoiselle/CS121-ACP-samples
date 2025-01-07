# Superclass
class Artist:
    def make_art(self):
        print("The artist makes an art.")

# Subclass
class Writer(Artist):
    def make_art(self):
        print("The writer makes art.")