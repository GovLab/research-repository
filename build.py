from os import path, getcwd, makedirs, listdir, remove
from yaml import load
from shutil import rmtree
from slugify import slugify
from staticjinja import make_site


# We define constants for the deployment.
searchpath = path.join(getcwd(), 'templates')
outputpath = path.join(getcwd(), 'site')

# We load the data we want to use in the templates.
PUBLICATIONS = load(open('data/repo.yaml'))


def loadAcademyData():
    return {'publications': PUBLICATIONS}


# We generate a bunch of template pages; dirty hack for now.
template = open('%s/publication.html' % searchpath).read()

filters = {
    'slug': lambda x: slugify(x.lower()),
}

# Remove publication templates that are no longer needed.
for filename in listdir(searchpath):
    filepath = '%s/%s' % (searchpath, filename)

    if filename.startswith('publication-') and path.isfile(filepath):
        remove(filepath)

# Clean the output folder.
if path.exists(outputpath):
    rmtree(outputpath)

makedirs(outputpath)

for index, publication in enumerate(PUBLICATIONS):
    filename = slugify(publication['title'].lower())
    new_file = open('%s/publication-%s.html' % (searchpath, filename), 'w+')
    new_page = template.replace('publications[0]', 'publications[%d]' % index)

    new_file.write(new_page)
    new_file.close()

site = make_site(
    filters=filters,
    outpath=outputpath,
    contexts=[(r'.*.html', loadAcademyData)],
    searchpath=searchpath,
    staticpaths=['static', '../data']
)

site.render(use_reloader=True)
