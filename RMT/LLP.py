import pulp
import matplotlib.pyplot as plt
import numpy as np

# Define the problem
lp_problem = pulp.LpProblem("Maximize_Z", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable("x1", lowBound=0)  # x1 >= 0
x2 = pulp.LpVariable("x2", lowBound=0)  # x2 >= 0

# Define the objective function
lp_problem += 3 * x1 + 2 * x2, "Z"

# Define the constraints
lp_problem += 2 * x1 + x2 <= 20
lp_problem += x1 + 2 * x2 <= 30

# Solve the problem
lp_problem.solve()

# Print the results
print(f"Status: {pulp.LpStatus[lp_problem.status]}")
print(f"x1 = {pulp.value(x1)}")
print(f"x2 = {pulp.value(x2)}")
print(f"Z = {pulp.value(lp_problem.objective)}")

# Graphical method - plot the constraints
x1_vals = np.linspace(0, 25, 400)
x2_vals1 = (20 - 2 * x1_vals)  # From constraint 2*x1 + x2 <= 20
x2_vals2 = (30 - x1_vals) / 2  # From constraint x1 + 2*x2 <= 30

plt.figure(figsize=(8, 6))
plt.plot(x1_vals, x2_vals1, label='2*x1 + x2 <= 20')
plt.plot(x1_vals, x2_vals2, label='x1 + 2*x2 <= 30')

# Fill feasible region
plt.fill_between(x1_vals, np.minimum(x2_vals1, x2_vals2), where=(x2_vals1 >= 0) & (x2_vals2 >= 0), color='gray', alpha=0.5)

plt.xlim(0, 25)
plt.ylim(0, 25)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Feasible Region')
plt.legend()
plt.grid(True)
