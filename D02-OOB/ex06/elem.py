#!/usr/bin/python3

class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')

class Elem:
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("incorrect behaviour.")

    def __init__(self, tag: str = 'div', attr: dict = {}, content=None, tag_type: str = 'double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if not (self.check_type(content) or content is None):
            raise self.ValidationError
        if type(content) == list:
            self.content = content
        elif content is not None:
            self.content.append(content)
        if (tag_type != 'double' and tag_type != 'simple'):
            raise self.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        attr_str = self.__make_attr()
        content_str = self.__make_content()
        result = f'<{self.tag}{attr_str}'

        if self.tag_type == 'double':
            result += '>'
            if content_str:
                result += f'\n{content_str}\n</{self.tag}>'
            else:
                result += f'</{self.tag}>'
        elif self.tag_type == 'simple':
            result += ' />'

        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if not self.content:
            return ''
        result = ''
        for el in self.content:
            if isinstance(el, Text) and str(el) == '':
                continue
            result += '  ' + str(el).replace("\n", "\n  ") + '\n'
        return result.rstrip('\n')

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or isinstance(content, Text) or
                (isinstance(content, list) and all(isinstance(elem, (Text, Elem)) for elem in content)))

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
