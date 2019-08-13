#!/bin/bash

SCRIPT_PATH=$(readlink -f $0)
CWD=S(dirname $SCRIPT_PATH)

name=test_cluster_mode
app_path=$CWD/../app/__init__.py
master_mode=yarn
deploy_mode=cluster
spark_queue=spark
py_files=$CWD/../dist/spark_submit_cluster_python-0.1.0-py2.7.egg

spark-submit \
  --name $name \
  --master $master_mode \
  --deploy-mode $deploy_mode \
  --queue $spark_queue \
  --py-files $py_files \
  $app_path

