# spark-submit-cluster-python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Showcase how to create a Python Spark application that can be launch in both client and cluster mode.

## How it works
To run Spark in cluster mode it is necessary to send the Spark application code in the spark-submit command. To do so we start by creating an egg file containing the code as described in the [setup.py](setup.py) file (packages property).

In the code it is necessary to import the package (app/__init__.py):
```Python
import sys
sys.path.insert(0, "spark-submit-cluster-python")
```
The spark-submit must have the option `--py-files` with the absolute path to the egg package ([spark-submit.sh](scripts/spark-submit.sh)):
```bash
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
  $app_pat
```

## Deploy
Clone this repository to a Hadoop node and build the egg:
```bash
$ bash scripts/create-egg.sh
```

## Run
Now just run the code:
```bash
$ bash scripts/spark-submit.sh
```

## Authors
*   [Gonçalo Castro](https://github.com/GoncaloCCastro)
*   [Ricardo Miranda](https://github.com/RicardoMiranda)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
