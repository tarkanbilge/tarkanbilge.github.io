"""Script to estimate a function using a Fourier Series"""

# ====================================================================================
# Import
# ====================================================================================

import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ====================================================================================
# Functions
# ====================================================================================

def fourier_series(f, interval, N):
	"""
	Calculates the Fourier Series to approximate a function f.

	Parameters
	----------
	f : function
		Arbitrary function to be estimated by Fourier Series. 
	interval : list of float
		The start and end points of the interval of analysis.
	N : int
		Number of harmonics to estimate the function f with.
		
	Returns
	-------
	F : function
		The Fourier Series approximation of f with N harmonics. 
	"""
	
	P = interval[1] - interval[0]
	coefficient_list = []
	# The cooefficient sum should be zero if N = 0, but still a function of t
	coefficient_sum = lambda t: 0 * t
	
	# The coefficient for n = 0 is written separately to simplify the sum
	a0 = (2.0/P) * scipy.integrate.quad(f, interval[0], interval[1])[0]

	if N > 0:
		for n in range(1, N + 1):
			cos_term = lambda t, n=n: np.cos((2.0 * np.pi * n * t)/P)
			sin_term = lambda t, n=n: np.sin((2.0 * np.pi * n * t)/P)
			f_cos = lambda t, n=n : f(t) * cos_term(t)
			f_sin = lambda t, n=n : f(t) * sin_term(t)

			an = (2.0/P) * scipy.integrate.quad(f_cos, interval[0], interval[1])[0]
			bn = (2.0/P) * scipy.integrate.quad(f_sin, interval[0], interval[1])[0]
			coefficient = lambda t, n=n, an=an, bn=bn: (an * np.cos((2.0 * np.pi * n * t)/P)) + (bn * np.sin((2.0 * np.pi * n * t)/P))
			coefficient_list.append(coefficient)
			
		coefficient_sum = lambda t: sum([x(t) for x in coefficient_list])
		
	F = lambda t: a0/2.0 + coefficient_sum(t)
	return(F)
		
# ====================================================================================
# Main
# ====================================================================================
 
if __name__ == '__main__':

	# Input function
	f = lambda t: signal.sawtooth(2 * np.pi * t)
	
	# Fourier Series estimate
	F = fourier_series(f, interval=[0.0, 1.0], N=3)

	# Plotting
	t = np.linspace(0, 2, 1000) 
	plt.plot(t, f(t))
	plt.plot(t, F(t))
	plt.ylim(-1.5, 1.5)
	plt.show()


