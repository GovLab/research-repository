from sys import argv
from yaml import safe_dump
from xlrd import open_workbook
from slugify import slugify
from collections import defaultdict


_COl_NAME_MAP = {
    'Publication Name': 'title',
    'Organization': 'organization',
    'Authors': 'authors',
    'Published On': 'date',
    'Link to Download': 'url',
    'Innovation':'category',
    'Objective': 'objective',
    'Sector':'sector',
    'Region':'region',
    'Methodology': 'methodology',
    'Abstract':'abstract'
}


# _LISTS = ['impact_areas', 'expertise', 'geographic_interest']


def get_sheet(filepath):
    return open_workbook(filepath).sheet_by_index(0)


def map_column_indexes(sheet):
    output = defaultdict(list)

    for idx, col_name in enumerate(sheet.row_values(0)):
        if col_name in _COl_NAME_MAP:
            output[_COl_NAME_MAP[col_name.strip()]].append(idx)

    return output


# def img_filename(first_name, last_name):
#     filename = first_name + '-' + last_name

#     return slugify(filename.decode('utf-8')).encode('ascii').title() + '.jpg'


def dump_yaml_file(filename, object_list):
    stream = file(filename + '.yaml', 'w')
    kwargs = {}

    kwargs['allow_unicode'] = True
    kwargs['explicit_start'] = True
    kwargs['default_flow_style'] = False

    safe_dump(object_list, stream, **kwargs)

    stream.close()

if __name__ == '__main__':
    sheet = get_sheet(argv[1])
    col_indexes_map = map_column_indexes(sheet)
    people = []

    for row_idx in xrange(1, sheet.nrows):
        row = sheet.row_values(row_idx)
        person = {}

        for col_name, col_indexes in col_indexes_map.items():
            if col_name not in _LISTS:
                val = row[col_indexes[0]].strip()

                if col_name == 'twitter':
                    val = '' if val == '@' else 'http://www.twitter.com/' + val

                elif col_name == 'role':
                    val = val if val != '' else '&nbsp'

                elif col_name == 'bio':
                    if val[0] == '"' and val[-1] == '"':
                        val = val[1:-1].strip()

                    elif val[0] == '\'' and val[-1] == '\'':
                        val = val[1:-1].strip()

                person[col_name] = val

            else:
                val = [row[x].strip() for x in col_indexes if row[x].strip()]

                person[col_name] = sorted(val)

        # person['image'] = img_filename(person['name'], person['last'])

        # people.append(person)

    dump_yaml_file('.'.join(argv[1].split('.')[:-1]), people)
