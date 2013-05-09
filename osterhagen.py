#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import sys
import arguments
import polynomials
import secret

def create_keys(args, arg_parser):
	# We check to see if every argument has a suitable value
	arguments.process_arguments_key_creation(args, arg_parser)

	# We build the polynomial used to hide the secret
	secret_polynomial = polynomials.create_polynomial(args)

	# For every party, we create a secret part,
	# and we save it in a file
	for x in range(1, args.total_parties + 1):
		osterhagen_key = polynomials.evaluate_polynomial(
				secret_polynomial, x)
		secret.save_osterhagen_key(x, osterhagen_key, args.hmac_key)

def recover_secret(args, arg_parser):
	raise NotImplementedError
	abscissa_list = []
	ordinate_list = []

	# For every file
	for osterhagen_key_file in args.key_files:
		osterhagen_key_content = []

		# We read each line
		for line in osterhagen_key_file.readlines():
			# If it's not a seperation line, we get the content
			if not line.startswith('-----'):
				osterhagen_key_content.append(line)
		# We retrieve the key's number, the key, and the signature
		x = int(osterhagen_key_content[0])
		osterhagen_key = int(osterhagen_key_content[1])
		signature = osterhagen_key_content[2].rstrip()

		# We compute the signature, to check if the file was tampered with
		check_signature = secret.compute_signature(x, osterhagen_key,
				args.hmac_key)
		# If the signatures don't match, we raise an error'
		if (signature != check_signature):
			raise ValueError(('signatures don\'t match in key number {0}\n'\
					+ 'expected value: {1}\n'\
					+ 'received: {2}').format(x, check_signature, signature))
		# Otherwise, we get the abscissa/ordinate needed to rebuild the
		# polynomial
		else:
			abscissa_list.append(x)
			ordinate_list.append(osterhagen_key)

	# We rebuild the polynomial by interpolation, and evaluate it in 0
	rebuilt_secret = int(polynomials.interpolate_evaluate_polynomial(
			0,
			abscissa_list,
			ordinate_list))

	# We print the secret
	print(rebuilt_secret)

def main():
	# We create an argument parser
	arg_parser = arguments.create_argument_parser()

	# We parse the argument
	args = arg_parser.parse_args(sys.argv[1:])

	args.func(args, arg_parser)

if __name__ == '__main__':
	main()

