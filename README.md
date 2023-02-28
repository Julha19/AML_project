# AML_project

## Applied Machine Learning, spring 2023
This repository is for the machine learning project in Applied Machine Learning

We will create one main file, which we will all contribute to, to get to a final project.
As for now the "Solar Power Generation Data" has been choosen for the project.

Feel welcome to create additional files, if you need to test something completely different, but relevant. Preferable put your name in the title of such files.

## Imports

The most common imports are NumPy, Pandas and Matplotlib:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

For loading the data I(Mathias) have created the function load_data() in the helpers.py file. Usage can be seen below, it simply load the csv files and does conversion from string to np.datetime64 for the DATE_TIME column.

For some reason Jupyter handles the importing of custom files in a weird way, and the path has be modified manually, which is the first 4 lines.
```python
import os
import sys
module_path = os.path.abspath(".")
sys.path.insert(0, module_path)
from helpers import load_data

plant1, plant2, weather1, weather2 = load_data()
```
