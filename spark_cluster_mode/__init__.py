import sys
sys.path.insert(0, "spark-submit-cluster-python-0.1.0-py2.7")

from pyspark.sql import sparkSession


def main(args=None):
    spark_session = sparkSession.builder.getOrCreate()
    count_dataframe.counting(spark_session=spark_session)


if __name__ == "__main__":
    from spark_cluster_mode.computations import count_dataframe

    main()
