#!/usr/bin/env python3
#	-*- coding: utf8 -*-

def bytes_to_string(b):
	result = ''

	for char in b:
		result += chr(char)

	return result

