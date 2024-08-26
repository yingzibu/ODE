e

### One compartment IV

[Code](https://github.com/yingzibu/ODE/blob/main/experiment/IV/one_compartment/clean_version.ipynb)

![](IV_1_comp.gif)


#### When multiple dosing, the ODE is the same, yet IC changes, $A(t = \tau * \lambda) += MD$, in which $\tau$ is the dosing interval, and $\lambda$ is the dosing times, $MD$ is the maintenance dose. How to incorporate this inside odeint? 
