#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import argparse
import osterhagen

def create_argument_parser():
	program_description = 'To be used if the suffering of the human race is so\
					great, so without hope, that this becomes the final\
					option.' 
	arg_parser = argparse.ArgumentParser(
			prog='osterhagen',
			description=program_description)

	subparsers = arg_parser.add_subparsers(title='subcommands',
			description='available actions',
			help='choose the proper action to create the Osterhagen keys,\
					or to recover the secret from Osterhagen keys')

	# We create the subparser for the key creation
	arg_parser_key_creation = subparsers.add_parser('create-keys',
			description=program_description)
	arg_parser_key_creation.set_defaults(func=osterhagen.create_keys)

	# The user must specify a secret
	arg_parser_key_creation.add_argument('-s', required=True, dest='secret',
			type=int,
			help='secret being shared by the Osterhagen keys')

	# The user can specify the number of secret parts that
	# will be generated
	arg_parser_key_creation.add_argument('-n', default=5, dest='total_parties',
			type=int,
			help='how many Osterhagen keys should be generated\
					(default: %(default)s)')

	# The user can specify the number of secret parts
	# needed to recover the whole secret
	arg_parser_key_creation.add_argument('-k', default=3,
			dest='needed_parties', type=int,
			help='how many Osterhagen keys should be necessary to recover\
					the whole secret (default: %(default)s)')

	# We create the subparser for the secret recovery
	arg_parser_secret_recovery = subparsers.add_parser('recover-secret',
			description=program_description)
	arg_parser_secret_recovery.set_defaults(func=osterhagen.recover_secret)

	# The user must specify the files containing the Osterhagen keys
	arg_parser_secret_recovery.add_argument('-f', required=True,
			dest='key_files',
			nargs='+',
			type=argparse.FileType('r'),
			help='list of files containing the Osterhagen keys')

	# The user must specify a HMAC key
	arg_parser_secret_recovery.add_argument('--public-key', required=True,
			dest='public_key',
			type=argparse.FileType('r'),
			help='RSA public key used to verify the Osterhagen keys\'\
					signature')

	return arg_parser

def process_arguments_key_creation(args, arg_parser):
	# The secret must be a strictly positive integer
	if args.secret <= 0:
		error_msg = 'argument {0}: invalid value '\
				+ '(the secret must be a strictly positive value): {1}'
		error_msg = error_msg.format('-s', args.secret)
		arg_parser.error(error_msg)

	# There must be at least two parties sharing the secret
	if args.total_parties <= 1:
		error_msg = 'argument {0}: invalid value '\
				+ '(at least two parties must share the secret): {1}'
		error_msg = error_msg.format('-n', args.total_parties)
		arg_parser.error(error_msg)

	# There must be at least two needed parties, and less than the total
	# number of parties to recover the secret
	if args.needed_parties > args.total_parties:
		error_msg = 'argument {0}: invalid value '\
				+ '(more needed parties than total parties): {1}'
		error_msg = error_msg.format('-k', args.needed_parties)
		arg_parser.error(error_msg)
	elif args.needed_parties <= 1:
		error_msg = 'argument {0}: invalid value '\
				+ '(at least two parties required to recover '\
				+ 'the secret): {1}'
		error_msg = error_msg.format('-k', args.needed_parties)
		arg_parser.error(error_msg)

