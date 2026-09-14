# Generating random numbers from specific distribution

import numpy as np
from numpy.random import PCG64, Generator, SeedSequence

# 1. Create a parent SeedSequence
parent_sq = SeedSequence(987654321)

# 2. Spawn child SeedSequence(s) to guarantee non-overlapping random streams
child_sqs = parent_sq.spawn(1)
child_sq = child_sqs[0]

# 3. Initialize Generator using PCG64 BitGenerator with child seed
rng = Generator(PCG64(child_sq))

# 4. Define Poisson process parameters
rate_lambda = 2.0  # Average rate of events per time unit
num_events = 100   # Number of arrival events

# Inter-arrival times for rate lambda follow Exponential(scale = 1 / lambda)
inter_arrival_times = rng.exponential(scale=1.0 / rate_lambda, size=num_events)

# Calculate continuous event arrival timestamps T_i = sum(X_1...X_i)
arrival_times = np.cumsum(inter_arrival_times)

print("First 5 Inter-arrival times:", np.round(inter_arrival_times[:5], 4))
print("First 5 Event Arrival times:", np.round(arrival_times[:5], 4))
