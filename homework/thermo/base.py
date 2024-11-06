import pyromat as pm

pm.config["unit_pressure"] = "kPa"

fluid = pm.get("mp.H2O")

## Analysis of the pump

p1 = 10
p2 = 2*1e3

#saturated liquid
v = 1/fluid.ds(p=p1)[0]
w_pump = v*(p2-p1)
print("work pump", w_pump)

h1 = fluid.hs(p=p1)[0]
h2 = h1 + w_pump
print("enthalpy at 2", h2)

## Analysis of the boiler

p3 = p2
h3 = fluid.hs(p=p3)[1]
s3 = fluid.ss(p=p3)[1]

q_boiler = h3 - h2

print("heat boiler", q_boiler)

## Analysis of the turbine

s4 = s3
p4 = p1
x4 = fluid.T_s(s=s4, p=p4, quality=True)[1]
print("quality at 4", x4)
h4 = fluid.h(x=x4, p=p4)
print("enthalpy at 4", h4)

w_turbine = h3 - h4
print("work done by turbine", w_turbine)

## Analysis of the condenser

q_condenser = h4 - h1
print("heat rejected by condenser", q_condenser)

w_net = w_turbine - w_pump
n = w_net/q_boiler

print("Efficiency :",n)