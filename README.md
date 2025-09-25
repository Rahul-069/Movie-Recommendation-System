# 🎬 Anime Recommendation System  

This project implements an **Anime Recommendation Engine** that suggests anime to users based on their previous ratings and genre similarities.  
It uses **Content-Based Filtering** with **TF-IDF** and **Cosine Similarity** to recommend the most relevant anime titles.  

---

## 🚀 Features  

- Load and preprocess **anime dataset** and **user ratings dataset**.  
- Count number of users and movies in the dataset.  
- Display detailed information about any user and their ratings.  
- Display anime details by anime ID.  
- Generate **personalized anime recommendations** based on user preferences.  
- Simple **menu-driven CLI interface** for interaction.  

---

## ⚙️ Tech Stack  

- **Python 3.8+**  
- **pandas** → data preprocessing  
- **scikit-learn** → TF-IDF vectorization & cosine similarity  

---

## 📂 Dataset  

The project uses two CSV files:  

1. **anime.csv** – Contains details of anime (id, name, genre, type, episodes, rating, members).  
2. **rt.csv** – Contains user ratings (`user_id`, `anime_id`, `rating`).  

---

## 🖥️ Usage  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/anime-recommendation-system.git
cd anime-recommendation-system
```

###2. Install Requirements
```
pip install -r requirements.txt
```

###3. Run the script
```
python main.py
```
