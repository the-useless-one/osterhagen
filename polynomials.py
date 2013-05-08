#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import random

def create_polynomial(args):
	polynomial = [args.secret]

	for d in range(args.needed_parties):
		polynomial.append(random.randint(0, args.bound))

	return polynomial

def evaluate_polynomial(polynomial, x):
	result = 0

	for d, c in enumerate(polynomial):
		result += c*(x**d)

	return result

