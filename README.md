# Movie Recommendation System  

This project implements an **Anime Recommendation Engine** that suggests anime to users based on their previous ratings and genre similarities.  
It uses **Content-Based Filtering** with **TF-IDF** and **Cosine Similarity** to recommend the most relevant anime titles.  

---

## Features  

- Load and preprocess **anime dataset** and **user ratings dataset**.  
- Count number of users and movies in the dataset.  
- Display detailed information about any user and their ratings.  
- Display anime details by anime ID.  
- Generate **personalized anime recommendations** based on user preferences.  
- Simple **menu-driven CLI interface** for interaction.  

---

## Tech Stack  

- **Python 3.8+**  
- **pandas** → data preprocessing  
- **scikit-learn** → TF-IDF vectorization & cosine similarity  

---

## Dataset  

The project uses two CSV files:  

1. **anime.csv** – Contains details of anime (id, name, genre, type, episodes, rating, members).  
2. **ratings.csv** – Contains user ratings (`user_id`, `anime_id`, `rating`).  

---

## Usage  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/anime-recommendation-system.git
cd anime-recommendation-system
```

### 2. Install Requirements
```
pip install -r requirements.txt
```

### 3. Run the script
```
python main.py
```

## Menu Options
When you run the program, you’ll see a menu like this:
```
Menu:
a. Count Users
b. Count Movies
c. Display User Information
d. Display Movie Name
e. Recommend Movie
f. Exit
```

## Recommendation Logic
1. Identify anime highly rated (≥ 7) by the user.

2. Collect genres of these anime.

3. Convert genres into TF-IDF vectors.

4. Compute cosine similarity between user’s preferences and all other anime.

5. Recommend the Top 5 most similar anime (excluding already watched ones).
