from archiveconfig.cli import parse_substitutions


def test_parse_substitutions():
    parsed = parse_substitutions('prefix=SR03ID01,foo=bar')
    assert parsed == {'prefix': 'SR03ID01', 'foo': 'bar'}


def test_parse_substitutions_for_empty_str():
    parsed = parse_substitutions('')
    assert parsed == {}
