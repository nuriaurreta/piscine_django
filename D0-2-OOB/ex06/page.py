#!/usr/bin/python3

from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text, Elem

class Page:
    def __init__(self, page) -> None:
        if not isinstance(page, Elem):
            raise page.ValidationError()
        self.page = page

    def is_valid(self) -> bool:
        return self.validate_element(self.page)

    def validate_element(self, page) -> bool:
        if not (isinstance(page, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li,
                                  H1, H2, P, Div, Span, Hr, Br)) or type(page) == Text):
            return False
        if type(page) == Text or isinstance(page, Meta):
            return True
        if isinstance(page, Html) and len(page.content) == 2 \
                and type(page.content[0]) == Head and type(page.content[1]) == Body:
            if (all(self.validate_element(el) for el in page.content)):
                return True
        elif isinstance(page, Head) and [isinstance(el, Title) for el in page.content].count(True) == 1:
            if (all(self.validate_element(el) for el in page.content)):
                return True
        elif isinstance(page, (Body, Div)) and \
                all([isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span)) or
                    type(el) == Text for el in page.content]):
            if (all(self.validate_element(el) for el in page.content)):
                return True
        elif isinstance(page, (Title, H1, H2, Li, Th, Td)) and \
                len(page.content) == 1 and type(page.content[0]) == Text:
            return True
        elif isinstance(page, P) and \
                all([isinstance(el, Text) for el in page.content]):
            return True
        elif isinstance(page, Span) and \
                all([isinstance(el, (Text, P)) for el in page.content]):
            if (all(self.validate_element(el) for el in page.content)):
                return True
        elif isinstance(page, (Ul, Ol)) and len(page.content) > 0 and \
                all([isinstance(el, Li) for el in page.content]):
            if (all(self.validate_element(el) for el in page.content)):
                return True
        elif isinstance(page, Tr) and len(page.content) > 0 and\
                all([isinstance(el, (Th, Td)) for el in page.content]) and \
                all([type(el) == type(page.content[0]) for el in page.content]):
            return True
        elif isinstance(page, Table) and \
                all([isinstance(el, Tr) for el in page.content]):
            return True
        return False

    def __str__(self) -> str:
        result = ""
        if isinstance(self.page, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.page)
        return result

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.__str__()))
