def frame(phrase='', ch='*'):
    empty_frame = f'{4 * ch}\n{ch}  {ch}\n{ch}  {ch}\n{4 * ch}'

    if not phrase:
        return empty_frame

    head = f'{(len(phrase) + 4) * ch}\n{ch}{(len(phrase) + 2) * " "}{ch}'
    middle_line = f'{ch} {phrase} {ch}'

    return '\n'.join((head, middle_line, head[::-1]))