import pandas as pd

def create_dietary_feature(df):
    """
    Count number of dietary options offered
    by each restaurant.
    """
    df["dietary_options_count"] = (
        df[["vegetarian_friendly","vegan_options","gluten_free"]].sum(axis=1))
    return df


def create_popularity_bucket(df):
    """
    Categorize restaurants according
    to popularity level.
    """
    df["popularity_bucket"] = pd.cut(df["total_reviews_count"],bins=[-1, 20, 100, df["total_reviews_count"].max()], labels=["Low", "Medium", "High"])
    return df


def create_cuisine_count(df):
    """
    Count number of cuisine categories
    associated with each restaurant.
    """
    df["cuisine_count"] = (df["cuisines"].fillna("").apply(lambda x: len(x.split(",")) if x != "" else 0))
    return df


def group_cuisine_counts(df):
    """
    Group cuisine counts above 5
    into a single category.
    """
    df["cuisine_count_grouped"] = (df["cuisine_count"].apply(lambda x: x if x <= 5 else 6))
    return df