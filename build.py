import staticjinja
import os
import json
import yaml
import sys
from slugify import slugify
from dateutil.parser import parse

# We define constants for the deployment.
cwd = os.getcwd()
searchpath  = os.path.join(cwd, "templates")
outputpath  = os.path.join(cwd, "site")

# We load the data we want to use in the templates.
PUBLICATIONS    = yaml.load(open('data/publications.yaml'))

def loadAcademyData():
	return { 'publications': PUBLICATIONS,
					 'resources': None }

# We define some filters we want to use in the templates.
def containsTag(x, y):
	if x['tags'] is None:
		return None
	return x if y in x['tags'] else None

def debug(text):
  print text
  sys.stdout.flush()
  return ''

def isEmpty(seq):
	return len([k for k in seq]) == 0

def nameTest(name, value):
	return "%s %s" % (name['first'], name['last']) == value

filters = {
	'byName': lambda x: [p for p in PEOPLE if p.name == x],
	'containsTag': containsTag,
	'debug': debug,
	'isEmpty': isEmpty,
	'slug': lambda x: slugify(x, to_lower=True),
	'nameTest': nameTest,
}

site = staticjinja.make_site(
	searchpath=searchpath,
	outpath=outputpath,
	staticpaths=['static', '../data'],
	filters=filters,
	contexts=[(r'.*.html', loadAcademyData),]
	)
site.render(use_reloader=True)