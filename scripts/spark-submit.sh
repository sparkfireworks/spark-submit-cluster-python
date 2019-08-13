#!/bin/bash

SCRIPT_PATH=$(readlink -f $0)
CWD=S(dirname $SCRIPT_PATH)

name=test_cluster_mode
app_path=$CWD/../app/__init__.py
master_mode=yarn
deploy_mode=cluster
spark_queue=spark
py_files=$CWD/WD/spark-submit-cluster-python

spark-submit \
  --name $name \
  --master $master_mode \
  --deploy-mode $deploy_mode \
  --queue $spark_queue \
  --py-files $py_files \
  $app_path

