import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
x=np.linspace(-1.25*np.pi,1.25*np.pi,1000)
fig,ax=plt.subplots()
ax.plot(x/np.pi,np.cos(2*x),color="orange",label="y=cos(2x)")
ax.plot(x/np.pi,np.sin(2*x),color="blue",label="y=sin(2x)")
ax.set(title='Plot of trigonometric function'
      ,xlabel='x',
      ylabel='y')
ax.legend(loc='upper right')
ax.axis('tight')
plt.ylim(-1.25,1.25)
plt.xticks([-1, -1/2, 0, 1/2, 1], ['-π', '-π/2', '0', 'π/2', 'π'])

plt.show()









