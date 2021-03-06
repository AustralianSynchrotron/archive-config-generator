from __future__ import print_function

import click

from .parse import parse_file
from .render import render_template


def parse_substitutions(s):
    substitutions = {}
    for sub in s.split(','):
        if not sub:
            continue
        key, value = sub.split('=')
        substitutions[key] = value
    return substitutions


@click.command()
@click.option('--dtd-path', required=True, help='Path to engineconfig.dtd')
@click.option('--group-name', required=True)
@click.option('--substitutions', default='')
@click.option('-o', '--output', type=click.File('w'))
@click.argument('files', nargs=-1)
def main(files, dtd_path, group_name, substitutions, output):
    substitutions = parse_substitutions(substitutions)
    channels = []
    for filename in files:
        with open(filename) as file:
            channels += list(parse_file(file, **substitutions))
    group = {'name': group_name, 'channels': channels}
    rendered_config = render_template(dtd=dtd_path, groups=[group])
    print(rendered_config, file=output)
