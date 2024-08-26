import jinja2
from jinja2 import Environment, select_autoescape
templateLoader = jinja2.FileSystemLoader( searchpath="/" )
something = ''

Environment(loader=templateLoader, load=templateLoader, autoescape=True)
templateEnv = jinja2.Environment(autoescape=True,
        loader=templateLoader )
Environment(loader=templateLoader, load=templateLoader, autoescape=True)
templateEnv = jinja2.Environment(autoescape=True, loader=templateLoader )
Environment(loader=templateLoader,
            load=templateLoader,
            autoescape=True)

Environment(loader=templateLoader,
            load=templateLoader, autoescape=True)

Environment(loader=templateLoader, autoescape=select_autoescape())

Environment(loader=templateLoader,
            autoescape=select_autoescape(['html', 'htm', 'xml']))

Environment(loader=templateLoader,
            autoescape=jinja2.select_autoescape(['html', 'htm', 'xml']))


def fake_func():
    return 'foobar'
Environment(loader=templateLoader, autoescape=True)
