from pathlib import Path

from src.io import load_dataset
from src.cleaning import (
    drop_unused_columns,
    clean_missing_ratings,
    encode_binary_columns)

from src.features import (
    create_dietary_feature,
    create_popularity_bucket,
    create_cuisine_count,
    group_cuisine_counts)

from src.utils import assert_columns, print_dataframe_shape


def main():
    root = Path(__file__).resolve().parent

    raw_path = root / "data" / "raw" / "tripadvisor_spain.csv"
    output_path = root / "data" / "processed" / "tripadvisor_spain_clean.csv"

    df = load_dataset(raw_path)

    required_columns = [
        "avg_rating",
        "total_reviews_count",
        "cuisines",
        "price_level",
        "vegetarian_friendly",
        "vegan_options",
        "gluten_free"]

    assert_columns(df, required_columns)

    df = drop_unused_columns(df)
    df = clean_missing_ratings(df)
    df = encode_binary_columns(df)

    df = create_dietary_feature(df)
    df = create_popularity_bucket(df)
    df = create_cuisine_count(df)
    df = group_cuisine_counts(df)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print("Clean dataset saved to:", output_path)
    print_dataframe_shape(df)


if __name__ == "__main__":
    main()