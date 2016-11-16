import re

def autocorrect(input):
    x = re.sub(r'\bu\b', 'your sister', input)
    z = re.sub(r'\b[yY]ou+\b', 'your sister', x)

    return z

autocorrect("u")

import re

# (?i) starts case-insensitive mode
def autocorrect(input):
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)