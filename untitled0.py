import numpy as np
import random, math

N = 100        # Size of the problem is N x N
steps = 3000   # Total number of iterations
tracks = 50    # Number of parallel tracks

# Generate a landscape with multiple local optima
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N - x0) * np.pi) + np.sin((y/N - y0) * np.pi) + \
           0.07 * np.cos(12 * (x/N - x0) * np.pi) + 0.07 * np.cos(12 * (y/N - y0) * np.pi)

# Random shifts to create a complex landscape
x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)  # Coordinates of global peak

# Starting points for each of the tracks
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

# Safeguard: Minimum temperature to avoid division by zero
T_min = 1e-6

def accept_prob(S_old, S_new, T):
    delta_E = S_old - S_new
    if delta_E > 0:
        return 1.0  # Always accept if the new solution is better
    elif T > T_min:
        return math.exp(delta_E / T)  # Accept with a probability if the new solution is worse
    else:
        return 0.0  # If T is too small, do not accept worse solutions

def simulated_annealing():
    global x, y

    for step in range(steps):
        # Cooling schedule: cubic decay of temperature
        T = max(T_min, ((steps - step) / steps) ** 3 - 0.005)

        success_count = 0  # Tracks that found the global peak

        for i in range(tracks):
            # Random neighboring move
            x_new = np.random.randint(max(0, x[i] - 3), min(N, x[i] + 3 + 1))
            y_new = np.random.randint(max(0, y[i] - 3), min(N, y[i] + 3 + 1))

            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # Accept the new solution based on the acceptance probability
            if random.random() < accept_prob(S_old, S_new, T):
                x[i], y[i] = x_new, y_new  # Move to new solution

            # Check if the current track has found the global peak
            if x[i] == peak_x and y[i] == peak_y:
                success_count += 1

        # If 30 or more tracks have found the peak, stop
        if success_count >= 30:
            break

    print(f"Tracks that found the peak: {success_count}")

# Run the simulated annealing algorithm
simulated_annealing()
