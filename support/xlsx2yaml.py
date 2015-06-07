from sys import argv
from yaml import safe_dump
from xlrd import open_workbook
from collections import defaultdict


_COl_NAME_MAP = {
    'Sector': 'sector',
    'Region': 'region',
    'Authors': 'authors',
    'Abstract': 'abstract',
    'Objective': 'objective',
    'Innovation': 'category',
    'Methodology': 'methodology',
    'Organization': 'organization',
    'Published On': 'date',
    'Publication Name': 'title',
    'Link to download': 'url',
}


def get_sheet(filepath):
    return open_workbook(filepath).sheet_by_index(0)


def map_column_indexes(sheet):
    output = defaultdict(list)

    for idx, col_name in enumerate(sheet.row_values(0)):
        if col_name in _COl_NAME_MAP:
            output[_COl_NAME_MAP[col_name.strip()]].append(idx)

    return output


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
    items = []

    for row_idx in xrange(1, sheet.nrows):
        row = sheet.row_values(row_idx)
        item = {}

        for col_name, col_indexes in col_indexes_map.items():
            val = row[col_indexes[0]]

            if isinstance(val, (float, int)):
                val = str(int(val)).strip()

            if col_name == 'abstract':
                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1].strip()

                elif val[0] == '\'' and val[-1] == '\'':
                    val = val[1:-1].strip()

            item[col_name] = val

        items.append(item)

    dump_yaml_file('.'.join(argv[1].split('.')[:-1]), items)
