from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('archiveconfig', 'templates'))


def render_template(groups):
    template = env.get_template('base.xml')
    return template.render(groups=groups)
