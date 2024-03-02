class Matrix:

    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt

    def __mul__(self):
        res = []
        for i in range(self.n):
            res += [[0] * self.n]
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j] += self.mt[i][k] * self.mt[j][k]
        return Matrix(self.n, self.m, res)

    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''

if __name__ == '__main__':
    t = int(input())
    l = []
    while True:
        try:
            l += list(map(int, input().split()))
        except: break
    k = 0
    for _ in range(t):
        n, m = l[k], l[k + 1]
        k += 2
        mt = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                mt[i][j] = l[k]; k += 1
        matrix = Matrix(n, m, mt)
        print(matrix.__mul__())