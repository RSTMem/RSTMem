from pyspark.sql import SparkSession

# Инициализация SparkSession
spark = SparkSession.builder \
    .appName("Пары") \
    .getOrCreate()

# Пример данных
products = [
    (1, "Первый"),
    (2, "Второй"),
    (3, "Третий"),
    (4, "Четвертый"),
    (5, "Пятый"),
    (6, "Шестой"),
    (7, "Седьмой"),
    (8, "Восьмой"),
    (9, "Девятый"),
    (10, "Десятый")
]

categories = [
    (1, "Первая"),
    (2, "Вторая"),
    (3, "Третья"),
    (4, "Четвертая"),
    (5, "Пятая"),
    (6, "Шестая"),
    (7, "Седьмая"),
    (8, "Восьмая"),
    (9, "Девятая"),
    (10, "Десятая")
]

reations = [
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (4, 1),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 2),
    (9, 9)
]

products_df = spark.createDataFrame(products, ["product_id", "product_name"])
categories_df = spark.createDataFrame(categories, ["category_id", "category_name"])
reations_df = spark.createDataFrame(reations, ["product_id", "category_id"])

product_category_df = reations_df \
    .join(products_df, on="product_id", how="inner") \
    .join(categories_df, on="category_id", how="inner") \
    .select("product_name", "category_name")

print("Имя продукта – Имя категории:")
product_category_df.show()

products_yes_df = reations_df \
    .select("product_id").distinct()

products_no_df = products_df \
    .join(products_yes_df, on="product_id", how="left_anti") \
    .select("product_name")

print("Продукты без категорий:")
products_no_df.show()

spark.stop()
