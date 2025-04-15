def style_me():
  print("Hi! Welcome to Style Me' your new fashion hub to discover your everyday style!")
  print("First lets get to know a few details about you, answer the following questions to the best of your ability:")
  
# Step 1: Ask a few demographic questions, or starter questions
  name = input("Introduce yourself! What is your name? ")
  print(f"Hi {name}, Thank You for choosing StyleMe!")

# Step 2: User chooses their favorite music genre out of the list provided
genres = ["Hip-Hop", "Rock", "Country", "Pop", "R&B"]
print("Out of the provided list, pick your favorite music genre:")
for i, genre in enumerate(genres, 1):
    print(f"{i}. {genre}")

while True:
    try: 
        genre_choice = int(input("\Enter the number of your favorite genre: "))
        if 1 <= genre_choice <= len(genres):
            chosen_genre = genres[genre_choice - 1]
            print(f"To solidify,You picked {chosen_genre}!\n")
            break 
        else: 
            print("Invalid choice. Please enter a number between 1 and", len(genres))
    except ValueError:
       print("Invalid input. Please only enter a number.")
    
# Step 3: Introduce the music genre artist choices utilizing 2 choices each gennre
artist_choices = {
  "Hip-Hop": [
    ("Lil Wayne", "Lil Baby")
    ("Eminem", "J.Cole")
    ("Dr.Dre", "Metro Boomin")
    ("Lil Kim", "Meghan Thee Stallion")
    ("Nicki Minaj", "Flo Milli")
  ],
  "Rock": [
    ("Radiohead", "Red Hot Chili Peppers")
    ("Green Day", "The White Stripes")
    ("Nirvana", "Arctic Monkeys")
    ("Queen", "Blink-182")
  ],
  "Country": [
   ("Kane Brown", "Shaboozey")
   ("Chris Stapleton", "Luke Combs") 
   ("Blake Shelton", "Morgan Wallon")
   ("Dolly Parton", "Kacey Musgraves")
   ("Reba McEntire", "Carrie Underwood")
  ],
  "Pop"; [
  ("Whitney Houston", "Beyonce")
  ("Celine Deion", "Arianna grande")
  ("TLC", "Destinys's, Child")
  ("ColdPlay", "One-Direction")
  ("Michael Jackson", "Pharrell Williams")
 ],
  "R&B"; [
  ("Jhene Aiko", "Kehlani")
  ("Jeremih", "Bryson Tiller")
  ("Victoria Monet", "Muni Long")
  ("Usher", "Chris Brown")
  ("Alicia Keys", "Ella Mai")
],
}

chosen_artist = []
print(f"Now there will be 5 rounds where you have to choose between two popular artist within the {chosen_genre} genre! Have Fun!
artist_pairs = artist_choices.get(chosen_genre)
