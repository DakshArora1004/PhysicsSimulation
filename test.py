import numpy as np

A = 10
F = 50                     # Reduced external force for less dominance
omega = 2        # Increased angular frequency for faster oscillation
b = 0.1                      # Increased damping coefficient for more pronounced damping
m = 1
k = 1
def Ao():
    return F / np.sqrt((k - m * omega**2)**2 + (b * omega)**2)
def delta():
    return np.arctan((m*omega*omega - k)/b*omega)
print(Ao())
print(delta())

def oss(t):
         return Ao() * np.cos(omega * t - delta())

print(oss(0))
print(oss(1))
print(oss(2))