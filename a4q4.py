from scipy.optimize import linprog
#Define the objective function
c=[4,3] 
#Constraints
A=[[-200,-100], #Vitamins
   [-1,-2], #Minerals
   [-40,-40]  #Calories
   ]
b=[-4000,-50,-1400]
#Bounds 
x_bounds=[(0,None)]*2
#Solve using linprog(Big-M is internally handled via 'highs' solver)
res=linprog(c,A_ub=A,b_ub=b,bounds=x_bounds,method='highs')

#Output result
if res.success:
    print('Optimal food units:',res.x)
    print(f'Minimum cost:, {res.fun} BDT')