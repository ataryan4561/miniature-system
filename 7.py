def palindromize(S):
    return S + S[::-1]
def hyphenate(S):
    S = palindromize(S)
    n = len(S)
    return S[:n//2] + '-' + S[n//2:]
def change_case(S):
    S = hyphenate( S[0].lower() + S[1:] )
    return S
def solve(S, k):
    if k == 0 and 'A' <= S[0] <= 'Z':
        print(change_case(S))
    else:
        print(hyphenate(S))

solve("Foobar",0)
solve("fooBar",0)
solve("PythonProg",-1)