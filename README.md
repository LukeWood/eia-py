![](media/logo.png)

_Python bindings for the Energy Information Administration API_

## Repo Overview

Our repository consists of two major components: a package `eia-py` and a set of
exploratory data analysis notebooks (EDA).

The package can be found under `eia`.  The package handles data scraping and loading.
The `eda` directory holds all tools required to perform exploratory data analysis.  The
relationship between the two is that the scripts and notebooks in `eda` rely on the
package in `eia`.

## Plan of Action

- write methods to scrape data from the API and serialize
- write github action to automate this
- write way to load data to numpy array/pandas

## Development Setup

To get started working on the repository, please clone the repo:

```
git clone https://github.com/lukewood/eia-py
```

Then install the repo:

```
cd eia-py
python setup.py develop
```

This will link the package.  To test that your installation works, run the following
in a python interpreted of your choice:

```
import eia
```

Then, you need to export an environment variable for the API key:

```
export EIA_API_KEY="{your-key}"
```


### Commits and Pull Requests

To make our development process streamlined and minimize conflicts we are doing all
development via pull requests.

Please send all code updates via pull request on GitHub

The process to do so is documented here:

Please create a branch:

```
git checkout -b mybranch
```

Make a change:

```
echo 'hello_world = "123"' >> eia/test.py
```

Format the code:

```
./shell/format.sh
```

Next, make a commit:

```
git add .
git commit -m "Made some changes"
```

Push your changes to GitHub:

```
git push origin mybranch
```

Finally, go to the GitHub Repo URL, https://lukewood/eia-py, and create a pull request
from your branch.
Make sure everything looks good, and request a review.  Then we can merge it.
