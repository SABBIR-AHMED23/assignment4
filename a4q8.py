import numpy as np
from scipy.optimize import linprog
# Payoff matrix for Player A (column player)
A=np.array([
    [-1,-2, 8],
    [ 7, 5,-1],
    [ 6, 0,12]
])
# Since linprog solves minimization problems,
# we will convert the game into a minimization problem for the column player.
# Step 1: Make the payoff matrix positive by adding a constant (if needed)
min_value=np.min(A)
if min_value<0:
    A=A-min_value  # shift matrix to make all elements non-negative
else:
    min_value=0  # no shift needed
# Step 2: Set up the LP
c=[1,1,1]   # Objective: minimize sum of probabilities (due to duality)
A_ub=-A.T     # Constraints: -A^T x <= -1 (because we maximize in original)
b_ub=-np.ones(3)
# Step 3: Solve
res=linprog(c, A_ub=A_ub, b_ub=b_ub, method='highs')
# Step 4: Get the probabilities
probabilities=res.x /np.sum(res.x)
# Step 5: Calculate the value of the game
value=1 /np.sum(res.x)
value=value+min_value  # Adjust back if shifted earlier
print("Optimal mixed strategy for Player A:")
print(f"Play Row 1 with probability {probabilities[0]:.4f}")
print(f"Play Row 2 with probability {probabilities[1]:.4f}")
print(f"Play Row 3 with probability {probabilities[2]:.4f}")

print(f"\nValue of the game: {value:.4f}")