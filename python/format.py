def formatColor(style: int = -1, text: str = 'n', back: str = 'n') -> str:
    forecolor = {
        'w': '30',
        'r': '31',
        'g': '32',
        'y': '33',
        'b': '34',
        'm': '35',
        'c': '36',
        's': '37'
    }
    backcolor = {
        'w': '40',
        'r': '41',
        'g': '42',
        'y': '43',
        'b': '44',
        'm': '45',
        'c': '46',
        's': '47'
    }

    f = forecolor.get(text)
    b = backcolor.get(back)

    if style == -1:
        if f and b:
            return f'\033[{f};{b}m'
        elif f:
            return f'\033[{f}m'
        elif b:
            return f'\033[{b}m'
        else:
            return '\033[m'
    else:
        return f'\033[{style};{f if f else ""}{";" + b if b else ""}m'
