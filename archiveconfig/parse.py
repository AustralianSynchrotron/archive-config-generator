from collections import namedtuple


Channel = namedtuple('Channel', 'name type period')


def parse_file(file, **substitutions):
    for line in file:
        channel = parse_line(line, **substitutions)
        if channel is not None:
            yield channel


def parse_line(line, **substitutions):
    line = line.strip()
    if not line or line.startswith('#'):
        return None
    line = line.format(**substitutions)
    return Channel(*line.split())
