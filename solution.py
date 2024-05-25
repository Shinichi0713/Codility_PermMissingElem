# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    return list(set(range(1, len(A)+2)) - set(A))[0]