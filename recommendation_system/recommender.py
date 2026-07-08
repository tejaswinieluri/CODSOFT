# recommender.py
from data import movies

def recommend_by_genre(preferred_genre):
    recommendations = [m["title"] for m in movies if m["genre"] == preferred_genre.lower()]
    return recommendations

# Main program
print("Welcome to the Movie Recommendation System!")
genre = input("Enter your favorite genre (sci-fi, action, romance): ")

results = recommend_by_genre(genre)

if results:
    print("We recommend these movies:")
    for r in results:
        print("-", r)
else:
    print("Sorry, no recommendations found for that genre.")
