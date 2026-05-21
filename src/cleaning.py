import pandas as pd

def drop_unused_columns(df):
    # Remove columns with excessive missing values or low analytical value.
    columns_to_drop = [
        "keywords",
        "atmosphere",
        "awards",
        "average",
        "default_language",
        "reviews_count_in_default_language",
        "price_range",
        "features",
        "special_diets",
        "restaurant_link",
        "original_location",
        "poor",
        "terrible",
        "excellent",
        "very_good",
        "latitude",
        "longitude"]
    df = df.drop(columns=columns_to_drop)
    return df


def clean_missing_ratings(df):
    """
    Remove rows with missing average ratings.
    """
    df = df.dropna(subset=["avg_rating"])
    return df


def encode_binary_columns(df):
    """
    Convert binary categorical columns
    from Y/N to 1/0.
    """
    binary_cols = ["vegetarian_friendly","vegan_options","gluten_free"]
    for col in binary_cols:
        df[col] = df[col].map({
            "Y": 1,
            "N": 0})
    return df