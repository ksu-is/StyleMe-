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
        genre_choice = int(input("\nEnter the number of your favorite genre: "))
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
    ("Lil Wayne", "Lil Baby"),
    ("Eminem", "J.Cole"),
    ("Dr.Dre", "Metro Boomin"),
    ("Lil Kim", "Meghan Thee Stallion"),
    ("Nicki Minaj", "Flo Milli"),
  ],
  "Rock": [
    ("Radiohead", "Red Hot Chili Peppers"),
    ("Green Day", "The White Stripes"),
    ("Nirvana", "Arctic Monkeys"),
    ("Queen", "Blink-182"),
  ],
  "Country": [
   ("Kane Brown", "Shaboozey"),
   ("Chris Stapleton", "Luke Combs"), 
   ("Blake Shelton", "Morgan Wallon"),
   ("Dolly Parton", "Kacey Musgraves"),
   ("Reba McEntire", "Carrie Underwood"),
  ],
  "Pop": [
  ("Whitney Houston", "Beyonce"),
  ("Celine Deion", "Arianna grande"),
  ("TLC", "Destinys's, Child"),
  ("ColdPlay", "One-Direction"),
  ("Michael Jackson", "Pharrell Williams"),
 ],
  "R&B": [
  ("Jhene Aiko", "Kehlani"),
  ("Jeremih", "Bryson Tiller"),
  ("Victoria Monet", "Muni Long"),
  ("Usher", "Chris Brown"),
  ("Alicia Keys", "Ella Mai"),
],
}

chosen_artist = []
print(f"Now there will be {len(artist_choices.get(chosen_genre, []))} rounds where you have to choose between two popular artist within the {chosen_genre} genre! Have Fun!")
artist_pairs = artist_choices.get(chosen_genre)

if artist_pairs:
  for i, (artist1, artist2) in enumerate(artist_pairs, 1):
      while True: 
          choice = input(f"Round {i}: Who do you prefer?\n(1) {artist1}\n(2) {artist2}\nEnter 1 or 2: ")
          if choice == "1": 
              chosen_artist.append(artist1)
              print(f"You chose {artist1}!/n")
              break 
          elif choice == "2":
              chosen_artist.append(artist2)
              print(f"You chose {artist2}!\n")
              break
          else:
              print("Invalid choice. Please go back and enter 1 or 2.")
else: 
    print(f"Sorry, we dont have artist choices for the {chosen_genre} genre yet.")

#Step 4: Style Generation (complete description will be added later)
print("\n--- Style Generation will be put here----")
print(f"Based on your chosen genre and artist(Genre: {chosen_genre}, Artists: {chosen_artist}), StyleMe! will now create your new style!")

style_me()
