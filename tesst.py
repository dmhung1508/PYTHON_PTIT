s,c= [str(i) for i in input().split()]
print(-1 if s.find(c) == -1 else (s.find(c) if s.find(c) == len(s) - s[::-1].find(c) else (s.find(c), s.rfind(c))))