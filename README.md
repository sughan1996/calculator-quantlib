# calculator-quantlib
POC for CalculatorQuantApp
Updated the pyproject.toml

 - Tag has to be implemented for a prod release
 - pyproject.toml, setup.py and requirments.txt are important
 - Any project/repo dependant on quantlib repo must make sure 
   requirements.txt has the following line

```
git+https://github.com/sughan1996/calculator-quantlib.git
```

 - The latest tag (version) will be installed in the required repo.