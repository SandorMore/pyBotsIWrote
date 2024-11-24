import numpy as np
import matplotlib.pyplot as plt

# Define parameters and constants
k = 100  # You can vary 'k' as needed
x = np.linspace(-np.sqrt(3), np.sqrt(3), 100)  # Limit the range of x for sqrt(3-x^2)

# Define the equation
y = x**(3/2) + 0.9 * np.sin(k * x) * np.sqrt(3 - x**2)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$y = x^{3/2} + 0.9\sin(kx)\sqrt{3-x^2}$")

# Add labels, title, and grid
plt.title("Visualization of $y = x^{3/2} + 0.9\sin(kx)\sqrt{3-x^2}$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True)

# Add a legend
plt.legend(fontsize=12)

# Display the plot
plt.show()