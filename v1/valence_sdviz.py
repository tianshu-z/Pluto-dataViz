import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# We use normal distribution to visualize valence, as std = abs(1/valence) & mu = 0

# valence is updated based on user's word-evaluating submission on TODAY page
# All 3 emotion dimension values, including valence, is reset every midnight at 00:00.
valence = -0.7
mu = 0


# When the user is pretty happy intuitively, their valence is above 0:
# 1. the diagram is above the x-axis.
# 2. the color is a happy color
# 3. the happier the user, the higher the top of the diagram should be


if valence > 0:
    std = 1/valence
    variance = np.square(std)
    x = np.linspace(mu - 4*std, mu + 4*std, 100)  # 做图横轴取值根据std(也就是valence)做适当规范, 前端工程师可根据实际情况进行调节
    y = np.sqrt(2*np.pi)*stats.norm.pdf(x, mu, std)  # y is standardized so that the actual y value is equal to valence
    plt.plot(x, y, color='#FA7690')  # line color - refer to the UI file for the actual color used in the app
    plt.fill_between(x, y, color='#FA7690')  # fill color - refer to the UI file for the actual color used in the app


# When the user is pretty sad intuitively, their valence is below 0:
# 1. the diagram is below the x-axis, mirroring the happy situation
# 2. the color is a sad color
# 3. the sadder the user, the lower the top of the diagram should be


elif valence < 0:
    std = - 1/valence
    variance = np.square(std)
    x = np.linspace(mu - 4 * std, mu + 4 * std, 100)
    y = - np.sqrt(2*np.pi)*stats.norm.pdf(x, mu, std)
    plt.plot(x, y, color='#42BACF')
    plt.fill_between(x, y, color='#42BACF')

# When valence = 0:
# there is a 0 line in the middle
# the color should be neutral

else:
    x, y = [-4, 4], [0, 0]
    plt.plot(x, y, color='grey')

# the axises should be removed in the actual visualization in the interface
# the labels should be kept (or removed) as indicated in the UI files
plt.ylim(-1, 1)
# plt.axis('off')

plt.show()
