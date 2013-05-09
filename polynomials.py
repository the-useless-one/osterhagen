#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import random

def create_polynomial(args):
	# The constant coefficient is the secret
	polynomial = [args.secret]

	# We create a random polynomial of degree k-1,
	# where k is the number of parties needed to recover the whole secret
	for d in range(args.needed_parties):
		polynomial.append(random.randint(0, args.bound))

	# We return it
	print(polynomial)
	return polynomial

def evaluate_polynomial(polynomial, x):
	result = 0

	# We evaluate the polynomial at abscissa x
	for d, c in enumerate(polynomial):
		result += c*(x**d)

	return result

def interpolate_evaluate_polynomial(x, x_list, y_list):
	def lagrange_polynomial(j):
		x_j = x_list[j]
		print('x_j', x_j)
		pol = 1
		for x_m in x_list:
			if x_m != x_j:
				print('x_m', x_m)
				pol *= (x - x_m)/(x_j - x_m)

		print(x_list[j], y_list[j], pol)
		return pol

	assert(len(x_list) == len(y_list))

	result = 0

	for j in range(len(x_list)):
		result += y_list[j]*lagrange_polynomial(j)

	return result

