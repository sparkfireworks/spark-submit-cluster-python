def counting(spark_session):
    df = spark_session.createDataFrame(zip(range(10), range(10)), ["col_1", "col_2"])
    print("DataFrame size is: %s" % df.count())
