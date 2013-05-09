#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import hashlib
import hmac

def compute_signature(x, osterhagen_key, hmac_key):
	key = bytes(hmac_key, 'utf8')
	msg = bytes('{0}{1}'.format(x, osterhagen_key), 'utf8')
	return hmac.new(key, msg, hashlib.sha256).hexdigest()

def save_osterhagen_key(x, osterhagen_key, hmac_key):
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
	osterhagen_key_signature = osterhagen_key_signature.format(
			compute_signature(x, osterhagen_key, hmac_key))

	# Final file
	osterhagen_key_final = '{0}\n{1}'.format(osterhagen_key_content,
			osterhagen_key_signature)

	# We save the file, and close it
	osterhagen_key_file.write(osterhagen_key_final)
	osterhagen_key_file.close()

