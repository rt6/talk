# Python Packages

Write python packages to increase code re-use and increase development time

You can install the package using pip into a conda environment for better package version management.

This repo contains a module called `talk` that you can experiment with.

### Use the `talk` package in your project:

1) Install conda by following instructions on their website

2) Create a new conda environement
```sh
conda create -n talk-test python=3
```

3) Install the talk package from github repo
```sh

pip install git+ssh://git@github.com/rt6/talk.git
```

4) Use the talk package in your python project
```python
import talk
talk.hello()
```
or
```python
from talk import hello
hello()
```

5) Uninstall talk package
```sh
pip uninstall talk
```
