import yaml
import csv

"""
Screenshot,Publication Name,Authors,Published On,Link to download,Innovation,Objective,Sector,Region,Methodology,Abstract
"""

PUBLICATIONS = []
with open('data/publications.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for item in reader:
        (thumbnail, title, authors, date, url,
            innovation_tags, objective_tags, sector_tags, region_tags, methodology_tags,
            abstract) = item
        innovation = innovation_tags.split(',')
        objective = objective_tags.split(',')
        sector = sector_tags.split(',')
        region = region_tags.split(',')
        methodology = methodology_tags.split(',')
        PUBLICATIONS.append({'title': title,
            'authors': authors,
            'date': date,
            'url': url,
            'tags': {'innovation': innovation, 'objective': objective, 'sector': sector, 'region': region, 'methodology': methodology},
            'abstract': abstract})

print PUBLICATIONS