'''
PuLP is an LP modeler written in python. 
PuLP can generate MPS or LP files and call GLPK, COIN CLP/CBC, CPLEX, GUROBI to solve linear problems.
'''
import pulp

Lp = pulp.LpProblem("Sample of Linear Programming", pulp.LpMaximize)

#Assignment of range in unknown variables x, y
x = pulp.LpVariable('x', lowBound=100, upBound=200)
y = pulp.LpVariable('y', lowBound=80, upBound=170)

Lp += -2000*x + 5000*y                                 #Objective Function
Lp += x + y >= 200                                     #Constraint assignment                      
Lp.solve()                                             #Solve the expression
print(Lp)                                              #Display details of problem

print("Total Model A & B cars required respectively: ")
for i in Lp.variables():
    print(i.varValue)
print("Maximum Profit: $", int(pulp.value(Lp.objective)))
