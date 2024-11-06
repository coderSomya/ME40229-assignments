import pyromat as pm
import numpy as np

pm.config["unit_pressure"] = "kPa"
pm.config["def_p"] = 100

fluid = pm.get("mp.H2O")

## Analysis of the pump

p1 = 10
p2 = 4000

v = 1/fluid.ds(p=p1)[0]
w_pump = v*(p2-p1)

print("work done by pump", w_pump)
h1 = fluid.hs(p=p1)[0]
h2 = h1 + w_pump

## Analysis of the high pressure turbine

p3 = p2
t3 = 400 + 273.15
h3 = fluid.h(p=p3, T=t3)
s3 = fluid.s(p=p3,T=t3)

p4 = 400
s4 = s3
x4 = fluid.T_s(s=s4, p=p4, quality = True)[1]
print("entropy at 3", s3)
print("quality at 4", x4)

h4 = fluid.h(x=x4, p=p4)

w_hpt = h3 - h4

print("work done by high pressure steam", w_hpt)


p5 = p4
t5 = 400 + 273.15
h5 = fluid.h(p=p5, T=t5)
s5 = fluid.s(p=p5, T=t5)

p6 = p1
s6 = s5

x6 = fluid.T_s(s=s6, p=p6, quality=True)[1]

h6 = fluid.h(p=p6, x=x6)
w_lpt = h5 - h6
print("work done by low pressure steam", w_lpt)

w_turbine = w_hpt + w_lpt

## Analysis of the boiler

q_H = (h3-h2) + (h5-h4)
print("heat input by boiler", q_H)

## Analysis of the condenser

q_L = h6 - h1
print("heat rejected by the condenser", q_L)

w_net = w_turbine - w_pump
n = w_net/q_H

print("thermal efficiency", n)