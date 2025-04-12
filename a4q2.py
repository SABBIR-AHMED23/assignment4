from scipy.optimize import linprog
#Define the objective function
c=[45,40,85,65]
#Constraints
A=[[-3,-4,-8,-6], #Proteins
   [-2,-2,-7,-5], #Fats
   [-6,-4,-7,-4]  #Carbohydrates
   ]
b=[-800,-200,-700]
#Bounds 
x_bounds=[(0,None)]*4
#Solve using linprog
res=linprog(c,A_ub=A,b_ub=b,bounds=x_bounds,method='highs')

#Output result
if res.success:
    print('Food units to purchase',res.x)
    print(f'Minimum cost:, {res.fun} BDT')
