import matplotlib.pyplot as plt
import seaborn as sns


def plot_dietary_options_vs_rating(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df,
        x="dietary_options_count",
        y="avg_rating",
        palette="viridis")

    plt.title("Restaurant Ratings by Number of Dietary Options", fontsize=14)
    plt.xlabel("Number of Dietary Options")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()


def plot_price_level_vs_popularity(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df,
        x="price_level",
        y="total_reviews_count",
        palette="magma")

    plt.yscale("log")
    plt.tight_layout()
    plt.title("Restaurant Popularity by Price Level", fontsize=14)
    plt.xlabel("Price Level")
    plt.ylabel("Total Reviews Count (log scale)")
    plt.show()


def plot_price_level_distribution(df):
    plt.figure(figsize=(8, 5))
    ax = sns.countplot(
        data=df,
        x="price_level",
        palette="magma")
    for container in ax.containers:
        ax.bar_label(container)

    plt.title("Restaurant Distribution by Price Level", fontsize=14)
    plt.xlabel("Price Level")
    plt.ylabel("Number of Restaurants")
    plt.tight_layout()
    plt.show()


def plot_median_reviews_by_price_level(df):
    price_median = (df.groupby("price_level")["total_reviews_count"].median().sort_values())

    plt.figure(figsize=(8, 5))
    ax = sns.barplot(
        x=price_median.index,
        y=price_median.values,
        palette="magma")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f")

    plt.title("Median Number of Reviews by Price Level", fontsize=14)
    plt.xlabel("Price Level")
    plt.ylabel("Median Total Reviews")
    plt.tight_layout()
    plt.show()


def plot_average_rating_by_region(df):
    top_regions = (df["region"].value_counts().head(10).index)

    df_regions = df[df["region"].isin(top_regions)]

    region_ratings = (df_regions.groupby("region")["avg_rating"].mean().sort_values(ascending=False))

    plt.figure(figsize=(12, 6))
    ax = sns.barplot(
        x=region_ratings.values,
        y=region_ratings.index,
        palette="viridis")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f")
    plt.title("Average Restaurant Rating by Region", fontsize=14)
    plt.xlabel("Average Rating")
    plt.ylabel("Region")
    plt.tight_layout()
    plt.xlim(3.5, 4.5)
    plt.show()


def plot_cuisine_variety_vs_rating(df):
    group_counts = (df["cuisine_count_grouped"].value_counts().sort_index())

    labels = [f"{i if i < 6 else '6+'}\n(n={group_counts[i]})"for i in group_counts.index]

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df,
        x="cuisine_count_grouped",
        y="avg_rating",
        palette="coolwarm")

    plt.xticks(ticks=range(len(labels)),labels=labels)

    plt.title("Restaurant Ratings by Cuisine Variety", fontsize=14)
    plt.xlabel("Number of Cuisines")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()


def plot_claimed_vs_rating(df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df,
        x="claimed",
        y="avg_rating",
        palette="Set2")

    plt.title("Restaurant Ratings: Claimed vs Unclaimed", fontsize=14)
    plt.xlabel("Tripadvisor Profile Status")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()