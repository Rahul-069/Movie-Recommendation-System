import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings('ignore')

anime_df = pd.read_csv('anime.csv')
rating_df = pd.read_csv('rt.csv')

user_dict = {}
anime_dict = {}

for _, row in anime_df.iterrows():
    anime_dict[row['anime_id']] = {
        'name': row['name'],
        'genre': row['genre'],
        'type': row['type'],
        'episodes': row['episodes'],
        'rating': row['rating'],
        'members': row['members']
    }

for _, row in rating_df.iterrows():
    if row['user_id'] not in user_dict:
        user_dict[row['user_id']] = {} 
    user_dict[row['user_id']][row['anime_id']] = row['rating']  

def count_users():
    return len(user_dict)

def count_movies():
    return len(anime_dict)

def display_user_info(user_id):
    if user_id in user_dict:
        user_info = user_dict[user_id]
        print(f"User {user_id} has rated the following anime:")
        for anime_id, rating in user_info.items():
            anime_name = anime_dict[anime_id]['name'] if anime_id in anime_dict else "Unknown"
            print(f"Anime: {anime_name}, Rating: {rating}")
    else:
        print(f"No information available for User ID: {user_id}")

def display_movie_name(anime_id):
    if anime_id in anime_dict:
        print(f"Anime Name: {anime_dict[anime_id]['name']}")
    else:
        print(f"No movie found with Anime ID: {anime_id}")

def recommend_movie(user_id):
    if user_id not in user_dict:
        return "User not found."

    user_ratings = user_dict[user_id]
    
    highly_rated_anime_ids = [anime_id for anime_id, rating in user_ratings.items() if rating >= 7]
    
    if not highly_rated_anime_ids:
        return "No highly rated anime found for this user."
    
    genres = [anime_dict[anime_id]['genre'] for anime_id in highly_rated_anime_ids if anime_id in anime_dict and anime_dict[anime_id]['genre']]

    combined_genres = ' '.join(genres)
    
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    anime_genres_tfidf = tfidf_vectorizer.fit_transform(anime_df['genre'].fillna(''))
    
    user_genre_tfidf = tfidf_vectorizer.transform([combined_genres])
    
    cosine_similarities = cosine_similarity(user_genre_tfidf, anime_genres_tfidf).flatten()
    
    anime_df['similarity_score'] = cosine_similarities
    recommendations = anime_df[~anime_df['anime_id'].isin(user_ratings.keys())].sort_values(by='similarity_score', ascending=False)
    
    if recommendations.empty:
        return "No recommendations available."
    else:
        top_recommendations = recommendations.head(5)
        result = "Top 5 Recommended Anime:\n"
        for idx, row in top_recommendations.iterrows():
            result += f"{idx + 1}. {row['name']} (Genre: {row['genre']}, Similarity Score: {row['similarity_score']:.2f})\n"
        return result

def menu():
    while True:
        print("\nMenu:")
        print("a. Count Users")
        print("b. Count Movies")
        print("c. Display User Information")
        print("d. Display Movie Name")
        print("e. Recommend Movie")
        print("f. Exit")
        
        choice = input("Choose an option: ").lower()
        
        if choice == 'a':
            print(f"Total Users: {count_users()}")
        elif choice == 'b':
            print(f"Total Movies: {count_movies()}")
        elif choice == 'c':
            user_id = int(input("Enter User ID: "))
            display_user_info(user_id)
        elif choice == 'd':
            anime_id = int(input("Enter Anime ID: "))
            display_movie_name(anime_id)
        elif choice == 'e':
            user_id = int(input("Enter User ID: "))
            print(recommend_movie(user_id))
        elif choice == 'f':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")
menu()