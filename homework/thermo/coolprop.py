import numpy as np
import matplotlib.pyplot as plt
import CoolProp.CoolProp as CP

density = CP.PropsSI('D', 'T', 300, 'P', 100e3, 'water')
print(density)


specific_vol = np.linspace(0.001, 3, 100)
density = 1/specific_vol

t1 = 400 + 273.15

p1 = CP.PropsSI('P', 'D', density, 'T', t1, 'water')
print(p1)

plt.loglog(specific_vol, p1)