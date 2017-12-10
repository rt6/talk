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
# install latest github commit
pip install --upgrade git+ssh://git@github.com/rt6/talk.git

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

### Upgrade `talk` package version
Run this command to upgrade latest version or another version

Note: the  version shown in `conda list` is taken from setup.py, it is not the github tag
```sh
# upgrade to latest version
pip install --upgrade git+ssh://git@github.com/rt6/talk.git
```


### Install based on git tag
```sh`
pip install --upgrade git+ssh://git@github.com/rt6/talk.git@<tag name>

pip install --upgrade git+ssh://git@github.com/rt6/talk.git@v0.2.0
```

### Uninstall `talk` package
```sh
pip uninstall talk
```
