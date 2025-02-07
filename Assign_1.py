import math
import matplotlib as plt
import numpy as np
u1 = 5
var1 = 1.5
u2 = 8 
var2 = 2.0
pw1 = 0.6 
pw2 = 0.4
# computing Likelihood
def likelihood(i  , wj):
    if wj == 'w1':
        return (1/( math.sqrt(2*math.pi)*var1 ))*math.exp( -(i-u1)**2 / (2*var1**2) )
    else:
        return (1/( math.sqrt(2*math.pi)*var2 ))*math.exp( -(i-u2)**2 / (2*var2**2) ) 


for i in range (0 , 16):
    print("For x = " + str(i))
    likelihood_1 = likelihood(i , "w1")
    likelihood_2 = likelihood(i , "w2")
    evidence = pw1*likelihood_1 + pw2*likelihood_2
    print("The posterior for w1 is " + str( round(  (likelihood_1*pw1) / evidence , 3) ) )
    print("The posterior for w2 is " + str( round( (likelihood_2*pw2) / evidence , 3) ) )

# 2. Plotting 
x_values =  np.linspace(0 , 15 , 100)
posterior_w1 = []
posterior_w2 = []
for i in x_values:
    likelihood_1 = likelihood(i , "w1")
    likelihood_2 = likelihood(i , "w2")
    evidence = pw1*likelihood_1 + pw2*likelihood_2
    posterior_w1.append(likelihood_1*pw1/evidence)
    posterior_w2.append(likelihood_2*pw2/evidence)

plt.figure(figsize = (8 , 5))
plt.plot(x_values , posterior_w1 , label = "P(W1|x)" , color = "blue" ,linewidth = 2)
plt.plot(x_values , posterior_w2 , label = "P(W2|x)" , color = "red" ,linewidth = 2)

plt.xlabel("x")
plt.ylabel("Posteriror Probability")
plt.legend()
plt.grid()
plt.show()