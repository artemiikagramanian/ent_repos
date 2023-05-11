
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

mark_freq = 30
fig, ax = plt.subplots(figsize = (10, 7))

with open("settings.txt", "r") as settings:
    freq, quan = map(float, settings.readlines())

with open("data.txt", "r") as data:
    dac_data = [i for i in map(int, data.readlines())]
    voltage = np.array(dac_data)*freq 

time_arr = np.arange(len(voltage))*quan

max_volt_ind = voltage.argmax()
charge_time = time_arr[max_volt_ind]

ax.plot(time_arr, voltage, 'o', ls="-", linewidth=1, color='red', markevery=30, label = "V(t)")

ax.set_xlabel("t, с")
ax.set_ylabel("V, В")

ax.set_title("Завсимость напряжения конденсатора от времени")

ax.legend()

ax.text(2, 1,   f"Время заряда t ={charge_time} c")
ax.text(2, 0.5, f"Время разряда t ={time_arr[-1] - charge_time} c")

ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0, 3.5)
ax.set_xlim(0, 11)

ax.grid( which='minor', linewidth=0.5, linestyle='dashed' )
ax.grid( which='major', linewidth=1 )

fig.savefig("plot.png")
plt.show()

