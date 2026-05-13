from collections import deque

def is_palindrome(s):
    dq=deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
s='AdidA'
print("Palindrome : ", is_palindrome(s))