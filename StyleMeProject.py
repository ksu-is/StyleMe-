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
    
# Step 3: 

