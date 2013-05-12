#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import Crypto
from Crypto.Hash import SHA256
import base64
import encoding

def save_osterhagen_key(x, osterhagen_key, signer):
	# File where the Osterhagen key will be saved
	osterhagen_key_file = open('osterhagen_key_{0}.ohk'.format(x), 'w')

	# Part of the file containing the Osterhagen key
	osterhagen_key_content = '-----BEGIN ABSCISSA-----\n{0}\n'
	osterhagen_key_content += '-----BEGIN ORDINATE-----\n{1}'
	osterhagen_key_content = osterhagen_key_content.format(x, osterhagen_key)

	# Part of the file containing the signature, in order
	# to prevent parties from tampering
	osterhagen_key_signature = '-----BEGIN SIGNATURE-----\n{0}\n'
	osterhagen_key_signature += '-----END SIGNATURE-----'
	# We compute the signature
	hashed_message = bytes('{0}{1}'.format(x, osterhagen_key), 'utf8')
	h = SHA256.new(hashed_message)
	signature = signer.sign(h)
	signature = base64.b64encode(signature)
	signature = encoding.bytes_to_string(signature)
	osterhagen_key_signature = osterhagen_key_signature.format(signature)

	# Final file
	osterhagen_key_final = '{0}\n{1}'.format(osterhagen_key_content,
			osterhagen_key_signature)

	# We save the file, and close it
	osterhagen_key_file.write(osterhagen_key_final)
	osterhagen_key_file.close()

