import re

def uncollapse(input_str):
    EX = 'zero|one|two|three|four|five|six|seven|eight|nine'
    digits = re.findall(EX, input_str)
    return ' '.join(digits)