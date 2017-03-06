# -*- coding: utf-8 -*-

from __future__ import print_function
import re

KEYWORDS = [
    'Closes-Bug',
    'Fixes-Bug',
    'Depends-On',
    'Implements',
    'Change-Id',
    'Co-Authored-By',
    'Author',
    'Date'
]

COMMIT_RE = r'commit ([a-z0-9]+)'
HASH_RE = r'[a-zA-Z0-9]{42}'

FIX_TEMPLATE = """---
fixes:
  - |
    {}"""

FEATURE_TEMPLATE = """---
features:
  - |
    {}"""


def get_re():
    parts = '|'.join(map(lambda x: x.lower(), KEYWORDS))
    f = '({}):([a-zA-Z0-9\-\.#:<>@\+ ]+)$'
    return re.compile(f.format(parts), re.IGNORECASE)


def get_bug_url(bug_number):
    return 'https://launchpad.net/bugs/' + str(bug_number)


def get_blueprint_url(tag):
    return 'https://blueprints.launchpad.net/openstack/?searchtext={}'.format(
        tag)


def is_bug(data):
    if 'closes-bug' in data:
        return True
    if 'fixes-bug' in data:
        return True


def is_blueprint(data):
    return 'implements' in data


def parse(diff):
    data = {}

    p = get_re()

    lines = diff.split('\n')
    data['sha'] = lines.pop(0).split(' ')[1]

    has_date = False

    for line in lines:
        if not line:
            continue

        if line.startswith('diff --git'):
            break

        res = p.findall(line)

        if res:
            res = res[0]
            data[res[0].lower()] = res[1]

            if res[0] == 'Date':
                has_date = True

        else:
            if has_date and 'commit_message' not in data:
                data['commit_message'] = line

    return data


def expand(data):

    if is_bug(data):
        number = data['closes-bug']
        number = number.replace('#', '').strip()
        data['closes-bug'] = {
            'bug_number': number,
            'bug_url': get_bug_url(number)
        }

    if is_blueprint(data):
        s = data['implements'].strip().split(' ')

        assert s[0].lower() == 'blueprint', 'Wrong blueprint format'

        data['implements'] = {
            'blueprint': s[1],
            'blueprint_url': get_blueprint_url(s[1])
        }

    return data


def generate_bug(data):
    return "Fixes `bug {} <{}>`__\n{}".format(
        data['closes-bug']['bug_number'],
        data['closes-bug']['bug_url'],
        data['commit_message']
    )


def generate_feature(data):
    return "Implements `{} <{}>`__\n{}".format(
        data['implements']['blueprint'],
        data['implements']['blueprint_url'],
        data['commit_message']
    )


def generate(data):
    if is_bug(data):
        print(FIX_TEMPLATE.format(generate_bug(data)))
    elif is_blueprint(data):
        print(FEATURE_TEMPLATE.format(generate_feature(data)))
    else:
        raise 'Unknown'


def run(diff):
    data = parse(diff)
    data = expand(data)
    return generate(data)
