from setuptools import setup

setup(
    name='spark-submit-cluster-python',
    version='0.1.0',
    description='Sowcase how to create a Python Spark application that can be launch in both client and cluster mode.',
    author='Ricardo Miranda',
    author_email='mail@ricardoMiranda.com',
    url='https://github.com/ricardomiranda/spark-submit-cluster-python',
    packages=['app', 'app.computations'],
)

