#!/usr/bin/python3

from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='html', attr = attr, content = content, tag_type='double')

class Head(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='head', attr = attr, content = content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='body', attr = attr, content = content, tag_type='double')

class Title(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='title', attr = attr, content = content, tag_type='double')

class Meta(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='meta', attr = attr, content = content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='table', attr = attr, content = content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='th', attr = attr, content = content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='tr', attr = attr, content = content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='td', attr = attr, content = content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ul', attr = attr, content = content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='ol', attr = attr, content = content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='li', attr = attr, content = content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h1', attr = attr, content = content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='h2', attr = attr, content = content, tag_type='double')

class P(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='p', attr = attr, content = content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='div', attr = attr, content = content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None, attr: dict = {}):
        super().__init__(tag='span', attr = attr, content = content, tag_type='double')

class Hr(Elem):
    def __init__(self):
        super().__init__(tag='hr', tag_type='simple')

class Br(Elem):
    def __init__(self):
        super().__init__(tag='br', tag_type='simple')


def test():
    html = Elem('html', content=[
        Elem('head', content=[
            Elem('title', content=[Text("Hello ground!")])
        ]),
        Elem('body', content=[
            Elem('h1', content=[Text("Oh no, not again!")]),
            Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])
    print(html)

if __name__ == '__main__':
    test()
