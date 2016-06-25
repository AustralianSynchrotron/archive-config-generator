from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('archiveconfig', 'templates'))


def render_template(dtd, groups):
    template = env.get_template('base.xml')
    return template.render(dtd=dtd, groups=groups)
