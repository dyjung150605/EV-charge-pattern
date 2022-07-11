# Requirements
import pyomo.environ as pe
!pip install - q pyomo
!apt-get install - y - qq glpk-utils
glpk = pe.SolverFactory('glpk', executable='/usr/bin/glpsol')
# Model
m = pe.ConcreteModel()
# Variables
m.x1 = pe.Var(within=pe.NonNegativeReals, bounds=(0, 4))
m.x2 = pe.Var(within=pe.NonNegativeReals, bounds=(0, 6))
# Objective function
m.obj = pe.Objective(expr=3*m.x1 + 5*m.x2, sense=pe.maximize)
# Constraints
m.con = pe.Constraint(expr=3*m.x1 + 2*m.x2 <= 18)
# Solve problem using GLPK solver
glpk.solve(m).write()
# Print results
print('x1 =', m.x1.value)
print('x2 =', m.x2.value)
print('Optimal value =', m.obj())
