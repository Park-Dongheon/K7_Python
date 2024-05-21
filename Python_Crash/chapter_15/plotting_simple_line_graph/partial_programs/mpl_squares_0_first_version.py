#!pip install matplotlib
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()            # plt--객체, subplots() 메서드-return값으로 figureBox창과 ax는 그래프 하나를 말함, fig--박스 그리기,
ax.plot(squares)

plt.show()