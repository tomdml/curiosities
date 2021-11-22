inverse = {
    '}': '{', '{': '}',
    ']': '[', '[': ']',
    ')': '(', '(': ')'
}


def parse(fp):
    stack, chunk = [], ''

    # Iterate over the file pointer, it's much more efficient than saving it all.
    for line in fp:
        for char in line:

            # We've entered a set of brackets
            if char in '{[(':
                # We yield all of the collected characters before the brackets
                if not stack:
                    yield chunk
                    chunk = ''

                stack.append(char)

            # We're leaving a set of brackets
            elif char in '}])':
                # Get the corresponding opening bracket and compare it to the top of the stack
                if inverse[char] != stack.pop():
                    raise ValueError('Mismatched closing brackets')

            # Char is not an opening or closing bracket
            else:
                # Check to see if we're inside any brackets.
                if not stack:
                    chunk += char

    yield chunk


with open('file.txt') as fp:
    # Parse is a generator - Easiest way to expand it is with the splat (*) operator.
    print(*parse(fp))
