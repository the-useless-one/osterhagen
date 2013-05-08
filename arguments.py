#!/usr/bin/env python3
#	-*- coding: utf8 -*-

import argparse

def create_argument_parser():
	arg_parser = argparse.ArgumentParser(
			prog='osterhagen',
			description='To be used if the suffering of the human race is so\
					great, so without hope, that this becomes the final\
					option.')

	arg_parser.add_argument('-s', required=True, dest='secret', type=int,
			help='secret being shared by the Osterhagen keys')

	arg_parser.add_argument('-n', default=5, dest='total_parties', type=int,
			help='how many Osterhagen keys should be generated\
					(default: %(default)s)')

	arg_parser.add_argument('-k', default=3, dest='needed_parties', type=int,
			help='how many Osterhagen keys should be necessary to recover\
					the whole secret (default: %(default)s)')

	arg_parser.add_argument('-p', default=100, dest='size', type=int,
			help='size in bits of the secret\'s parts\
					(default: %(default)s)')

	return arg_parser

def process_arguments(args, arg_parser):
	if args.secret <= 0:
		error_msg = 'argument {0}: invalid value '\
				+ '(the secret must be a strictly positive value): {1}'
		error_msg = error_msg.format('-s', args.secret)
		arg_parser.error(error_msg)

	if args.total_parties <= 1:
		error_msg = 'argument {0}: invalid value '\
				+ '(at least two parties must share the secret): {1}'
		error_msg = error_msg.format('-n', args.total_parties)
		arg_parser.error(error_msg)

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

	args.bound = 2**args.size
	if (args.secret >= args.bound or
			args.total_parties >= args.bound or
			args.needed_parties >= args.bound):
		error_msg = 'every parameter should be less than '\
				+ '{0} bits'
		error_msg = error_msg.format(args.bound)
		arg_parser.error(error_msg)

