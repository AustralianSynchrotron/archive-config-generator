from xml.etree import ElementTree

from archiveconfig.render import render_template
from archiveconfig.parse import Channel


def test_render_template():
    groups = [{
        'name': 'SR03ID01',
        'channels': [
            Channel('CHANNEL_A', 'monitor', '1.0'),
            Channel('CHANNEL_B', 'scan', '1.0'),
        ]
    }]
    output = render_template(groups=groups)
    tree = ElementTree.fromstring(output)
    assert tree.find('./group/name').text == 'SR03ID01'
    ch1, ch2 = tree.findall('./group/channel')
    assert ch1.find('name').text == 'CHANNEL_A'
    assert ch1.find('monitor') is not None
    assert ch1.find('period').text == '1.0'
    assert ch2.find('name').text == 'CHANNEL_B'
