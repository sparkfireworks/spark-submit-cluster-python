import sys
sys.path.insert(0, "spark-submit-cluster-python.zip")

from pyspark.sql import sparkSession


def main(args=None):
    spark_session = sparkSession.builder.getOrCreate()
    count_dataframe.counting(spark_session=spark_session)


if __name__ == "__main__":
    from app.computations import count_dataframe

    main()
