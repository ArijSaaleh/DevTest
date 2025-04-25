from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

def get_product_category_pairs(
    products: DataFrame,
    categories: DataFrame,
    product_category: DataFrame
):
    # Join product_category with products and categories
    product_category_pairs = (
        product_category
        .join(products, on="product_id", how="inner")
        .join(categories, on="category_id", how="inner")
        .select("product_name", "category_name")
    )

    # Products without categories: left anti join
    products_without_category = (
        products
        .join(product_category, on="product_id", how="left_anti")
        .select("product_name")
    )

    return product_category_pairs, products_without_category
