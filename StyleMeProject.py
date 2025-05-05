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
    ("Guns N' Roses", "The Strokes"),
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

#Step 4: Style Generation dictionary

style_descriptions = {
    "Hip-Hop": {
        "group1": "90s streetwear would be worn by celebrities of all kinds, rappers, athletes, and the youthful eyes that look up to them. Staples of this era are oversized shirts and jackets, baggy jeans, distinctive shoes, significance on logos, the style is a unique blend of underground culture as a meaningful way to express the communities that created it. When shopping you should look for chunky sneakers, bold colors, oversized jeans, oversized graphic tees, bucket hats, chuncky jewlrey, and the names brands to match toembrace this unique and edgy style.",
        "group2": "Much like its 90s counterpart, the contemporary emergance of urban streetwear is now a staple for many celebrities, influencers, and wearers of all ages alike. However, the once solely street wear has taken a high fashion turn. The style has taken on the world from the United States all the wau to Tokyo and beyond, the style now highlights high fashion luxury brands and runway ready oufits. Staples still include the baggy jeans and shirts, sneaker fashion has become a greater staple with brands like new balance, addidas, and nike. Snap backs, crocheted hats, and skull caps have become a staple along with stacking jewlrey pieces, patches, layering clothes, and cplementary colors, the style has taken an all new high.",
    },
    "Rock": {
        "group1": "The rebellious spirit of Rock has long sense made its mark on the work starting in the early 1900s. The fashion sense of the era is no exception. The early introductions of rock include the tight pants, leather jackets, high colored shirts, mini skirts, bold prints, chaggy haricuts, ripped jeans, band t-shirts, laced gloves, and layered jewlrey were staples. The perfect way to express your love for early rock legends.",
        "group2": "Modern rock fashion looks quite different, but still holds its bold rebellious essence to stand out from the crowd. Staples from bands like Nirvana and Pearl Jam began an almost anti-fashion style to deny the abundance of things. Staples such as cardigans, ripped jeans, converse, baggy jeans, and oversized graphic tees. Grundge is the staple for many of the 90s to modern rock styles.",
    }, 
    "Country": {
        "group1": "The western style, cowboy boots and button ups, the classic introduction to the onstage singing cowboy. This is the signature look of the classic country vibe. It doesn’t stop there with iconic styles like Nudie Suits. Intricate designs, rhinstones, and appliques. These are the perfect stand out styles yourself.",
        "group2": "Much like many aspects of the world  the revolutionary counterculture movement the genre has taken on a new life. Denim is the new you! The perfect combination of bell bottoms, jean jackets, denim vests, flowy skirts, and rhinestone cowboy hats. The new urban cowboy, the perfect blend of cowboy and western fashion.",
    },
    "Pop": {
        "group1": "The early pop culture resignating Glam, Disco, and the material world. Adrogonous, nontraditional styles of clothing, lots of glitter, lace gloves, layered necklaces, leather jackes, tight clothes, and the princess persona.",
        "group2": "Then theres the layed back, cute but low effort style perfect for those wishing to keep it simple yet outstanding. With an influence of hip-hop, the big clothes, layered jewlrey, flannels, fun colorful shoes. The fun mix of layed back street style and the bright material pop style blend well in this modern era.",
    },
    "R&B": {
        "group1": "The highlight of R&B’s finest include glamourus gowns, make-up to match, beautiful and bold wigs, afros, big earings, sunglasses, off the shoulder shirts, flip hairstyles, pantsuits, shoulder pads, leotards, denim, and oversized sweaters. A glamouros and sophisticated style, highlighting the greats that made the genre what it is.",
        "group2": "The modern R&B style only built on to the glory of the early R&B style. The style manifested into daisy dukes, low-rise jeans, tunics worn with a belt, knee high boots, fitted tees, camo patterns, sheer or lace materials, cross body bags, small purses, and the pairing of form-fitting and baggy clothes together(like a form fitting cropped shirt with oversized jeans.",
    },
}
#Step 4: Style Generation (complete description will be added later)

print("\n--- Style Generation----")
genre_styles = style_descriptions.get(chosen_genre)
first_artist_choices = 0
second_artist_choices = 0 

if artist_pairs and chosen_artist and genre_styles:
    for i, choice in enumerate(chosen_artist):
        artist1, artist2 = artist_pairs[i]
        if choice == artist1:
            first_artist_choices += 1
        elif choice == artist2:
            second_artist_choices += 1

    if first_artist_choices > second_artist_choices: 
        final_style = genre_styles.get("group1", f"Your style is insipired by the early sounds of {chosen_genre}.")
    elif second_artist_choices > first_artist_choices: 
        final_style = genre_styles.get("group2", f"Your style is insipired by the modern evolution of {chosen_genre} classics.")
    else: 
        final_style =f"Based on your prefence your style is a blend of both classic and modern elements of the genre {chosen_genre}."
else:
    final_style = f"Based on your chosen genre ({chosen_genre}), your style has been crafted just for you!."
    
print(f"Based on your chosen genre and artist, StyleMe! will now create your new style!: {final_style}")
print(f"first_artist_choices: {first_artist_choices}")
print(f"second_artist_choices: {second_artist_choices}")


style_me()
