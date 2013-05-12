#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import Crypto
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64
import encoding
import arguments
import polynomials
import secret

def create_keys(args, arg_parser):
	# We check to see if every argument has a suitable value
	arguments.process_arguments_key_creation(args, arg_parser)

	# We build the polynomial used to hide the secret
	secret_polynomial = polynomials.create_polynomial(args)

	# We build the public/private keys used to sign/verify the Osterhagen keys
	pub_priv_keys = RSA.generate(2048)

	# We save the public key
	public_key_file = open('public_key.pem', 'w')
	pub_key = encoding.bytes_to_string(pub_priv_keys.publickey().exportKey())
	public_key_file.write(pub_key)
	public_key_file.close()

	# We create the signer
	signer = PKCS1_v1_5.new(pub_priv_keys)

	# For every party, we create a secret part,
	# and we save it in a file
	for x in range(1, args.total_parties + 1):
		osterhagen_key = polynomials.evaluate_polynomial(
				secret_polynomial, x)
		secret.save_osterhagen_key(x, osterhagen_key, signer)

def recover_secret(args, arg_parser):
	abscissa_list = []
	ordinate_list = []

	# We open the public key file
	publickey = RSA.importKey(args.public_key.read())
	signature_verifier = PKCS1_v1_5.new(publickey)

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
		signature = base64.b64decode(osterhagen_key_content[2].rstrip())

		# We compute the signature, to check if the file was tampered with
		hashed_message = bytes('{0}{1}'.format(x, osterhagen_key), 'utf8')
		h = SHA256.new(hashed_message)

		# If the signatures don't match, we raise an error'
		if (not signature_verifier.verify(h, signature)):
			error_msg = 'signatures don\'t match in key number {0}\n'.format(x)
			raise ValueError(error_msg)
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
	args = arg_parser.parse_args()

	# We call the suitable function
	args.func(args, arg_parser)

if __name__ == '__main__':
	main()

