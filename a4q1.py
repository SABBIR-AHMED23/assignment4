import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
#Define the objective function
c=[-2,-1] #Negated for maximization
#Constraints
A=[[1,2],[1,1],[1,-1],[1,-2]]
b=[10,6,2,1]
#Bounds 
x0_bounds=(0,None)
x1_bounds=(0,None)
#Solve using linprog
res=linprog(c,A_ub=A,b_ub=b,bounds=[x0_bounds,x1_bounds],method='highs')

print('Optimal Solution:')
print(f'x1={res.x[0]}')
print(f'x2={res.x[1]}')
print(f'Maximum Z={-res.fun}')
#plotting
x=np.linspace(0,10,400)
plt.figure(figsize=(8,6))
#Plot each constraint line
plt.plot(x,(10-x)/2,label=r'$x_1+2x_2\leq 10$')
plt.plot(x,6-x,label=r'$x_1+x_2\leq 6$')
plt.plot(x,x-2,label=r'$x_1-x_2\leq 2$')
plt.plot(x,(x-1)/2,label=r'$x_1-2x_2\leq 1$')
#Fill feasible region
x1=np.linspace(0,10,400)
x2=np.linspace(0,10,400)
X1,X2=np.meshgrid(x1,x2)

ineq1=(X1+2*X2<=10)
ineq2=(X1+X2<=6)
ineq3=(X1-X2<=2)
ineq4=(X1-2*X2<=1)
ineq5=(X1>=0)&(X2>=0)
feasible=ineq1&ineq2&ineq3&ineq4&ineq5
plt.contourf(X1,X2,feasible,levels=[0.5,1],alpha=0.5)
#Plot optimal point
if res.success:
    plt.plot(res.x[0],res.x[1],'ro',label='Optimal solution')
    plt.text(res.x[0]+0.1,res.x[1],f'Z={round(-res.fun,2)}')
#Labeling
plt.xlim(0,10)
plt.ylim(0,10)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Feasible region and optimal solution')
plt.legend()
plt.grid()
plt.show()
