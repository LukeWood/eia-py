![](media/logo.png)

[Check out our live data understanding dashboard!](https://lukewood.github.io/eia-py/dashboard/)

[Check out the presentation slides](https://lukewood.github.io/eia-py/slides/)

_Python bindings for the Energy Information Administration API_

## Repo Overview

Our repository consists of two major components: a package `eia-py` and a set of
exploratory data analysis notebooks (EDA).

The package can be found under `eia`.  The package handles data scraping and loading.
The `notebooks/` directory holds all tools required to perform exploratory data analysis.  The
relationship between the two is that the scripts and notebooks in `notebooks/` rely on the
package in `eia`.

## Links

- [GitHub repo](https://github.com/lukewood/eia-py)
- [API Docs](https://lukewood.github.io/eia-py)
- [Data Understanding Dashboard](https://lukewood.github.io/eia-py/dashboard)
- [Per-Dataset Data Analysis](https://lukewood.github.io/eia-py/auto-reports)
- [Presentation Slide Deck](https://lukewood.github.io/eia-py/slides)

## Quickstart

The easiest way to get started is to install from PyPi:

```
pip install eia-py-api
```

Next you'll need to export an API key in your environment variables:

```
export EIA_API_KEY="{your-key}"
```

You can get an API key from [the EIA website](https://www.eia.gov/opendata/).

## Examples

For examples, please check out our [notebooks directory](https://github.com/LukeWood/eia-py/tree/master/notebooks).

## Contributing

Contribute to the [eia-py](https://github.com/lukewood/eia-py) GitHub repo.

### Development Setup

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
