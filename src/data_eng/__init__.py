from pyspark.sql import SparkSession


def init_spark() -> SparkSession:
    from delta import configure_spark_with_delta_pip

    # Set packages needed at runtime, including both Delta and Kafka
    extra_packages = [
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0"
    ]
    
    builder = SparkSession.builder \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder, extra_packages).getOrCreate()
    return spark

if __name__ == "__main__":
    pass