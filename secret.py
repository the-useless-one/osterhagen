#!/usr/bin/env python3
#	-*- coding: utf8 -*-

def save_secret_part(x, secret_part):
	secret_part_file = open('secret_part_{0}.ohk'.format(x), 'w')

	secret_part_content = '-----BEGIN ABSCISSA-----\n{0}\n'
	secret_part_content += '-----END ABSCISSA-----\n'
	secret_part_content += '-----BEGIN ORDINATE-----\n{1}\n'
	secret_part_content += '-----END ORDINATE-----'
	secret_part_content = secret_part_content.format(x, secret_part)

	secret_part_signature = '-----BEGIN SIGNATURE-----\n'
	secret_part_signature += '-----END SIGNATURE-----'

	secret_part_final = '{0}\n{1}'.format(secret_part_content,
			secret_part_signature)

	secret_part_file.write(secret_part_final)
	secret_part_file.close()

