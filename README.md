# Tripadvisor Spain Restaurants EDA

## Project Overview

This project presents an Exploratory Data Analysis (EDA) of restaurant data extracted from Tripadvisor, focusing exclusively on restaurants located in Spain.

The main objective of the analysis is to explore how factors such as dietary inclusivity, cuisine diversity, pricing level, geographical location and Tripadvisor profile management relate to customer satisfaction and restaurant popularity.

The project follows a modular and reproducible Data Science workflow including data cleaning, feature engineering, visualization and analytical interpretation.
Due to GitHub file size limitations, the raw dataset is not included in this repository. Please download the dataset from the Kaggle link above and place it inside the `data/raw/` directory before running the project.

---

## Dataset Information

- **Dataset:** Tripadvisor European Restaurants
- **Source:** Kaggle
- **Original Dataset Link:**  
https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants


The original dataset contains restaurant information from multiple European countries. For this project, the dataset was filtered to include only restaurants located in Spain.

---

## Dataset Summary

- Original dataset: Tripadvisor European Restaurants
- Selected country: Spain
- Unit of analysis: restaurants
- Main variables analysed:
  - Customer rating
  - Price level
  - Region
  - Cuisine types
  - Dietary options
  - Tripadvisor profile status
- Dataset not included in this repository due to file size limitations.

---

## Project Objectives

The analysis aims to answer the following research questions:

1. Does offering a wider variety of dietary options help restaurants receive better ratings?

2. Is there a relationship between restaurant price level and popularity?

3. Which regions in Spain concentrate the highest-rated restaurants?

4. Do restaurants offering a wider variety of cuisines receive better customer ratings?

5. Do claimed Tripadvisor profiles receive better customer ratings?

---

## Project Structure

```text
project_root/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── io.py
│   ├── cleaning.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Data Cleaning

Several cleaning operations were performed throughout the project:

- Removal of highly incomplete or low-value columns
- Handling of missing values
- Removal of redundant variables
- Encoding of binary categorical variables
- Validation of required columns
- Creation of a cleaner and more manageable Spain-only dataset

---

## Feature Engineering

The following engineered features were created:

- `dietary_options_count`
- `popularity_bucket`
- `cuisine_count`
- `cuisine_count_grouped`

Additional cuisine-related binary variables were also generated for selected cuisine categories.

---

## Exploratory Data Analysis

The EDA focused on identifying relationships between restaurant characteristics and customer behavior through:

- Distribution analysis
- Boxplots
- Barplots
- Countplots
- Regional aggregations
- Cuisine diversity analysis

All visualizations include analytical interpretation and business-oriented insights.

---

## Visualizations

The project includes several visualizations to support the analysis, including:

- Rating distribution by dietary options
- Popularity distribution by price level
- Average ratings by Spanish region
- Rating distribution by cuisine diversity
- Rating comparison between claimed and unclaimed profiles

---

## Business Insights

- Restaurants offering more dietary options tend to show more stable and consistently positive customer ratings.
- Premium restaurants generally achieve higher median popularity levels, although high popularity can also be found across lower pricing categories.
- The Canary Islands and Balearic Islands show some of the highest average restaurant ratings among the most represented Spanish regions.
- Restaurants with broader cuisine diversity tend to maintain more concentrated positive rating distributions.
- Claimed Tripadvisor profiles show slightly more stable customer evaluations compared to unclaimed establishments.
---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## How to Run

### Clone repository

```bash
git clone <repository_url>
cd <project_folder>
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run pipeline

```bash
python main.py
```

### Launch notebook

```bash
jupyter notebook notebooks/eda.ipynb
```

---

## Future Improvements

Future work could include:

- Sentiment analysis from customer reviews
- Machine learning models for rating prediction
- Clustering analysis of restaurant profiles
- Integration of tourism and demographic datasets
- Temporal analysis of restaurant performance trends
