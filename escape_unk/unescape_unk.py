import regex
import sys

escaped_re = regex.compile(r"\[\[\d+\]\]")

# Remove escape delimiter and convert to char
def unescape(match):
    return chr(int(match.captures()[0].strip('[]')))

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
