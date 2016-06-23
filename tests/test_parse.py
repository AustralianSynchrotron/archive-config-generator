from archiveconfig.parse import parse_line, parse_file


def test_parse_line():
    channel = parse_line('SR03BM01:FOO scan 1')
    assert channel.name == 'SR03BM01:FOO'
    assert channel.type == 'scan'
    assert channel.period == '1'


def test_parse_line_with_multiple_spaces():
    channel = parse_line('SR03BM01:FOO    scan       1')
    assert channel.name == 'SR03BM01:FOO'
    assert channel.type == 'scan'
    assert channel.period == '1'


def test_parse_line_returns_none_on_blank_lines():
    assert parse_line('') is None
    assert parse_line('  ') is None


def test_parse_line_returns_none_on_comment_lines():
    assert parse_line('# this is a comment') is None


def test_parse_line_with_subs():
    channel = parse_line('{prefix}:FOO scan {rate}', prefix='SR03', rate='2.0')
    assert channel.name == 'SR03:FOO'
    assert channel.period == '2.0'


def test_parse_file():
    file = ['{prefix}:CHANNEL_A scan 1\n',
            '{prefix}:CHANNEL_B monitor 2\n']
    channels = list(parse_file(file, prefix='SR03'))
    assert len(channels) == 2
    assert channels[0].name == 'SR03:CHANNEL_A'


def test_parse_file_skips_comments_and_blank_lines():
    file = ['FOO scan 1\n',
            '\n',
            '# a comment\n',
            'BAR monitor 2\n']
    channels = list(parse_file(file, prefix='SR03'))
    assert len(channels) == 2
    assert channels[0].name == 'FOO'
    assert channels[1].name == 'BAR'
