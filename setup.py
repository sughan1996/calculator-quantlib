from setuptools import setup, find_packages

requirements = open('requirements.txt').read().splitlines()

setup(
    name='CalculatorQuantApp',
    description='calculator-quantlib codebase',
    author='Sughan R Samson',
    author_email='sughanrichason1996@gmail.com',
    license='MIT',
    packages=find_packages(),
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=requirements,
    python_requires='>=3.6',
)
