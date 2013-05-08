#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import sys
import arguments
import polynomials
import secret

def main():
	# We create an argument parser
	arg_parser = arguments.create_argument_parser()

	# We parse the arguments
	args = arg_parser.parse_args(sys.argv[1:])
	arguments.process_arguments(args, arg_parser)

	secret_polynomial = polynomials.create_polynomial(args)

	for x in range(1, args.total_parties + 1):
		secret_part = polynomials.evaluate_polynomial(
				secret_polynomial, x)
		secret.save_secret_part(x, secret_part)

if __name__ == '__main__':
	main()
