# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi

map = {}
t ,n = input().split()
for case in range(int(t)):
  s = input().lower()
  for i in range(len(s)):
    if not s[i].isalnum():
      s = s.replace(s[i], ' ')
  for i in s.split():
    if i in map:
      map[i] += 1
    else:
      map[i] = 1
map = sorted(map.items(), key=lambda e: (-e[1], e[0]))
for i in map:
  if i[1] >= int(n):
    print(*i)