# research-repository

Document repository and search tool for selected research papers and resources.

## Install

To install, clone this repository and run the following commands in the base directory:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python build.py runserver
```

## Deploy

To deploy on github pages, use the following command:

`git subtree push --prefix site origin gh-pages`