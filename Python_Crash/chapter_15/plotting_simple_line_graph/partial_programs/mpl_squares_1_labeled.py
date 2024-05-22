import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)             # x범례
ax.set_ylabel("Square of Value", fontsize=14)             # y범례

# Set size of tick labels.
ax.tick_params(labelsize=14)            #tick_params : 눈금

plt.show()