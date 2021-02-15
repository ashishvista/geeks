# “{“,”}”,”(“,”)”,”[“,”]”

def parenthesis_check(str):
    stack = []
    p1 = ['{', '(', '[']
    p2 = ['}', ')', ']']
    h = {'(': ')', '{': '}', '[': ']'}
    for c in str:
        if c in p1:
            stack.append(c)
        else:
            if len(stack) == 0:
                print('not balanced')
                return
            s = stack.pop()
            if h[s] != c:
                print('not balanced')
                return

    if len(stack) > 0:
        print('not balanced')
    else:
        print('balanced')


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        str = input()
        parenthesis_check(str)
