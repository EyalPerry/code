from pyspark.sql import SparkSession

def init_spark() -> SparkSession:
    spark_scala_version = "2.12"
    spark_version = "3.5.0"
    delta_version = "3.3.0"

    # Set packages needed at runtime, including both Delta and Kafka
    all_packages = [
        f"org.apache.spark:spark-sql-kafka-0-10_{spark_scala_version}:{spark_version}",
        f"io.delta:delta-spark_{spark_scala_version}:{delta_version}"
    ]
    
    builder = SparkSession.builder \
        .master("local[*]") \
        .appName("MySparkApp") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.jars.packages", ",".join(all_packages))
    
    spark = builder.getOrCreate()
    return spark

if __name__ == "__main__":
    init_spark()
    a=5