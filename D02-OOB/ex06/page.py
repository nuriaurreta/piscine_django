#!/usr/bin/python3

from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text, Elem

class Page:
    def __init__(self, page) -> None:
        if not isinstance(page, Elem):
            raise ValueError("my_elem must be an instance of Elem class")
        self.page = page

    def is_valid(self) -> bool:
        return self.validate_element(self)

    def validate_element(self, elem):
        valid_types = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul,
                    Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)
        if not isinstance(elem, valid_types):
            return False

        if isinstance(elem, Html):
            if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
                return False
        elif isinstance(elem, Head):
            title_count = 0
            for child in elem.content:
                if isinstance(child, Title):
                    title_count += 1
                if not self.validate_element(child):
                    return False
            if title_count != 1:
                return False
        elif isinstance(elem, Body) or isinstance(elem, Div):
            valid_body_children = (H1, H2, Div, Table, Ul, Ol, Span, Text, P)
            for child in elem.content:
                if not isinstance(child, valid_body_children) or not self.validate_element(child):
                    return False
        elif isinstance(elem, Title) or isinstance(elem, H1) or isinstance(elem, H2) or isinstance(elem, Li) \
                or isinstance(elem, Th) or isinstance(elem, Td):
            if len(elem.content) != 1 or not isinstance(elem.content[0], Text):
                return False
        elif isinstance(elem, P):
            if any(not isinstance(child, Text) for child in elem.content):
                return False
        elif isinstance(elem, Span):
            if any(not isinstance(child, (Text, P)) or not self.validate_element(child) for child in elem.content):
                return False
        elif isinstance(elem, Ul) or isinstance(elem, Ol):
            if len(elem.content) == 0 or any(not isinstance(child, Li) or not self.validate_element(child) for child in elem.content):
                return False
        elif isinstance(elem, Tr):
            th_count = sum(1 for child in elem.content if isinstance(child, Th))
            td_count = sum(1 for child in elem.content if isinstance(child, Td))
            if th_count > 0 and td_count > 0:
                return False
            if len(elem.content) == 0 or th_count + td_count != len(elem.content):
                return False
        elif isinstance(elem, Table):
            if len(elem.content) == 0 or any(not isinstance(child, Tr) or not self.validate_element(child) for child in elem.content):
                return False
        return True

    def __str__(self) -> str:
        result = ""
        if isinstance(self.page, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.page)
        return result

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

if __name__ == '__main__':
    pass
