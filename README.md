# Computational-Science
Computational Techniques for Evaluations

Write a program to perform a Metropolis Monte Carlo simulation of the 2D Ising model
in zero field (H = 0) and on a square L × L lattice. The Hamiltonian of this model is given
by
H = −J ∑ s i s j
(s i, j = ±1)
hi, ji
where the sum is over all distinct nearest-neigbor pairs and s i and s j are the values of the
spins at the lattice sites i and j. Set J = 1. Use periodic boundary conditions and spin-flip
updates. Temperatures are expressed in energy units. Time is expressed in units of Monte
Carlo steps (MCS) (1 MCS = 1 update per spin on average, i.e. total of L × L random
updates).
(a) Check that the ground state energy is calculated correctly. (Use all-spins-up or all-
spins-down as your initial configuration and calculate the energy of this configuration.)
For the following, the task is to study the 32 × 32 Ising model at three different temper-
atures: T = 2.1, 2.265 and 3.5. Note: the middle temperature T = 2.265 is difficult and
the results will look different than for the other two cases.
(b) Estimate a suitable equilibration time for T = 2.1 and 3.5. Perform several short runs
and plot the magnetization m and the internal energy u per spin as a function of time (in
MCS). Use a random spin configuration as your initial state. Remember to use different
random number sequences for the separate runs.
(c) For T = 2.265, perform a long simulation run of at least 50 000 MCS and plot the
resulting magnetization curve. Can you explain what is happening? How will the behavior
affect the time needed to perform measurements at this temperature?
(d) Show a snapshot of a typical equilibrium configuration for each temperature. (You
can plot the lattice for example using the commands surf() and view(2) in Matlab.)
(e) Compute hmi and h|m|i for each temperature. Calculate the averages over several inde-
pendent runs starting each run with a random spin configuration (remember to equilibrate
the system in the beginning of each run). Explain the results.
