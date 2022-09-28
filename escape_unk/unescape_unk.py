import regex
import sys

escaped_re = regex.compile(r"\[\[[a-z\d]+\]\]")

def unescape(match):
    ''' Convert hex values to unicode string '''
    return bytes.fromhex((match.captures()[0].strip('[]'))).decode('utf-8')

for line in sys.stdin:
    # Find splits and matches inside the sentence
    escaped = list(escaped_re.finditer(line.strip()))
    splits = list(escaped_re.splititer(line.strip()))
    output = ''

    # Join splits with unescaped matches
    for i, split in enumerate(splits):
        if i != len(splits)-1:
            output += split + unescape(escaped[i])
        else:
            output += split

    print(output)
