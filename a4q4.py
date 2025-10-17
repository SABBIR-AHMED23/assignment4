import pulp
#Create LP problem
prob=pulp.LpProblem('Diet_problem_BigM',pulp.LpMinimize)
#Big M value
M=1e6
#Decision variables
x1=pulp.LpVariable('Food_A',lowBound=0)
x2=pulp.LpVariable('Food_B',lowBound=0)
#Slack,surplus and artificial variables
s1=pulp.LpVariable('Surplus1',lowBound=0)
a1=pulp.LpVariable('Artificial1',lowBound=0)

s2=pulp.LpVariable('Surplus2',lowBound=0)
a2=pulp.LpVariable('Artificial2',lowBound=0)

s3=pulp.LpVariable('Surplus3',lowBound=0)
a3=pulp.LpVariable('Artificial3',lowBound=0)
#Cost
prob+=4*x1+3*x2+M*a1+M*a2+M*a3,'Total_Cost_with_BigM'
#Constraints
prob+=200*x1+100*x2-s1+a1==4000,'Vitamins'
prob+=x1+2*x2-s2+a2==50,'Minerals'
prob+=40*x1+40*x2-s3+a3==1400,'Calories'

prob.solve()
#Output
print(f'Optimal quantity of food A:{x1.varValue}')
print(f'Optimal quantity of food B:{x2.varValue}')
print(f'Minimum total cost:{pulp.value(prob.objective)}')
