#!/usr/bin/python3

def get_line(line):
    name, atr = line.strip().split('=')
    d = dict(item.split(':') for item in atr.strip().replace(' ', '').split(','))
    d['name'] = name
    return d

def main():
    HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    <style>
        ul {{list-style: none; padding-left: 8px; padding-right: 8px;}} h4 {{text-align: center;}}
    </style>
</head>
<body>
    <table>
        {content}
    </table>
</body>
</html>
"""

    CELL = """
        <td style="border: solid 1px">
            <h4>{name}</h4>
            <ul>
                <li>No: {number}</li>
                <li>{small}</li>
                <li>{molar}</li>
                <li>El: {electron}</li>
            </ul>
        </td>
"""
    content = '<tr>'
    with open('periodic_table.txt', 'r') as f:
        elements = [get_line(line) for line in f.readlines()]
    pos = 0
    for el in elements:
        if pos > int(el['position']):
            content += '</tr>\n<tr>'
            pos = 0
        for _ in range(pos, int(el['position']) -1):
            content += '<td></td>\n'
        pos = int(el['position'])
        content += CELL.format(
            name = el['name'],
            number = el['number'],
            small = el['small'],
            molar = el['molar'],
            electron = el['electron'],
        )
    content += '</tr>\n'
    with open('periodic_table.html', 'w') as f:
        f.write(HTML.format(content = content))
            

if __name__ == '__main__':
    main()