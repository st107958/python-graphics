import graphics as gr

window = gr.GraphWin("Recursive", 500, 500)


def fractal(A, B, C, D, deep=100):
    # if alpha > 1:
    #     print('unable to draw fractal')
    #     return
    alpha = 0.1
    if deep < 1:
        return
    else:
        for M, N in (A, B), (B, C), (C, D), (D, A):
            gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

        A1 = [(B[0] - A[0]) * (alpha) + A[0], (B[1] - A[1]) * (alpha) + A[1]]
        B1 = [(C[0] - B[0]) * (alpha) + B[0], (C[1] - B[1]) * (alpha) + B[1]]
        C1 = [(D[0] - C[0]) * (alpha) + C[0], (D[1] - C[1]) * (alpha) + C[1]]
        D1 = [(A[0] - D[0]) * (alpha) + D[0], (A[1] - D[1]) * (alpha) + D[1]]

        deep = deep - 1
        fractal(A1, B1, C1, D1, deep)


A = [100, 100]
B = [400, 100]
C = [400, 400]
D = [100, 400]


fractal(A, B, C, D)
x = int(input())