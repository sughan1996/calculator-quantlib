from setuptools import setup, find_packages

requirements = open('requirements.txt').read().splitlines()

setup(
    name='CalculatorQuantApp',
    description='Your package description',
    author='Sughan R Samson',
    author_email='sughanrichason1996@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
