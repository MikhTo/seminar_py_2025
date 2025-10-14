import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.fft import fftfreq, fft, rfft, rfftfreq
"""
# Сегодня научимся рисовать графики при помощи matplotlib

# Создаем графики
t = np.arange(0, 10, 0.05)
y = np.sin(2*np.pi*t)

plt.figure()
plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("y")
plt.show()

y2 = np.sin(2*np.pi*2*t)
plt.figure()
plt.plot(t, y, label="f=1")
plt.plot(t, y2, label="f=2")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()

# Нарисовать фигуры Лиссажу в одном окошке:
fig, axes = plt.subplots(3,3, sharex=True, sharey=True)
colors = ["red", "#228b22", (0, 0, 128/255)]
for i in range(3):
    for j in range(3):
        axes[i][j].plot(y, np.sin(2*np.pi*(i+1)*t + np.pi/(j+1)),
                        color = colors[i])
        axes[i][0].set_ylabel(rf"$f_1/f_2 = 1/{i+1}$")
        axes[2][j].set_xlabel(rf"$\Delta\phi = \pi/{j+1}$")
plt.show()
"""

# Теперь рассмотрим работу с реальными данными
# Обычно они хранятся в файлах, в нашем случае в .csv
data = np.loadtxt('data.csv', delimiter=';')
t, U = data[:, 0], data[:, 1]
fig, axes = plt.subplots(2,1)
axes[0].plot(t, U)
axes[0].set_xlabel(r"$t, \mu s$")
axes[0].set_ylabel(r"$U, V$")

mask = (t > 130000) & (t < 160000)
t_cut = t[mask]
U_cut = U[mask]
U_cut -= U_cut.mean()
freq = rfftfreq(len(t_cut), t[1]-t[0])
ft = np.abs(rfft(U_cut))
axes[1].plot(freq, ft, label="real data")

#Аппроксимируем
f_mask = (freq>0.045)&(freq<0.075)
freq_cut = freq[f_mask]
ft_cut = ft[f_mask]
popt, _ = curve_fit(foo := lambda f, A, mu, sigma, y0: A*np.exp(-(f-mu)**2/(2*sigma**2))+y0,
                     freq_cut, ft_cut, maxfev = 100000)
axes[1].plot(freq_cut, foo(freq_cut, *popt), label="approx")
#axes[1].set_ylim([1, 5100])
print(popt)
axes[1].legend()
axes[1].set_xlabel(r"$f, MHz$")
axes[1].set_ylabel(r"$\hat{F}[U], a.u.$")

plt.show()