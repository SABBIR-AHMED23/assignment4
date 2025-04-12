from scipy.optimize import linprog
#Define the objective function
c=[-12,-15,-14] #Negated for maximization
#Constraints
A=[[1,1,1], 
   [0.02,0.04,0.03], 
   [3,2,5]  
   ]
b=[100,3,300]
#Bounds 
x_bounds=[(0,None)]*3
#Solve using simplex
res=linprog(c,A_ub=A,b_ub=b,bounds=x_bounds,method='highs')

#Output result
if res.success:
    print('Optimal proportinos',res.x)
    print(f'Maximum profit:, {-res.fun} BDT')
