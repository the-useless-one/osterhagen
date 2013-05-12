# Osterhagen

						  MMM                                         
						MMMMMMM:                                      
						MMMMMMM:                                      
						MMMMMMM:                                      
						MMMMMMM:                                      
					   .M     M:                                      

					  MMM=   MM                                       
				   MMMMMMM   MMMMM                                    
				MMMMMMMMMM   MMMMMMM                                  
			 MMMMMMMMMMMMM   MMMMMMM  MM.                             
		  =MMMMMMMMMMMMMMM   MMMMMMM  MMMMM=                          
	   .MMMMMMMMMMMMMMMMMM   MMMMMMM  MMMMMM MM                       
	 MMMMMMMMMMMMMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	MMMMMMMMMMMMMMMMMMMMMM   MMMMMMM  MMMMMM MMMMM$                   
	 MMMMMMMMMMMMMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMMMMMMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMMMMMMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM  MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM. MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM. MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM, MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM, MMMMMM MMMMM                    
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM: MMMMMM MMMMM       ____      _            _                             
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM: MMMMMM MMMMM      / __ \    | |          | |                            
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM~ MMMMMM MMMMM     | |  | |___| |_ ___ _ __| |__   __ _  __ _  ___ _ __   
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM~ MMMMMM MMMMM     | |  | / __| __/ _ \ '__| '_ \ / _` |/ _` |/ _ \ '_ \  
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMM+ MMMMMM MMMMM     | |__| \__ \ ||  __/ |  | | | | (_| | (_| |  __/ | | | 
	 MMMMMMMMD  MMMMMMMMMM   MMMMMMMZ MMMMMMMMMMMM      \____/|___/\__\___|_|  |_| |_|\__,_|\__, |\___|_| |_| 
	 MMMMMMMMMMMMMMMMMMMMM   MMMMMMMM MMMMMMMMMMMM                                           __/ |            
	 MMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMM                                          |___/                                
	 MMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMM                    
	$MMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMMZ                   
	MMMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMM=                   
	  MMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMM                      
		 NMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMM                         
			IMMMMMMMMMMMMM   MMMMMMMMMMMMM                            
				MMMMMMMMMM   MMMMMMMMMM                               
				   MMMMMMM   MMMMMMM                                  
					   MMM    MMMM                                     

To be used if the suffering of the human race is so great, so without hope,
that this becomes the final option. 

Fork me on [GitHub](https://github.com/the-useless-one/osterhagen).

## HISTORY

In the Doctor Who double episode "The Stolen Earth/Journey's End", UNIT has
created Osterhagen keys and distributed it among its agents. If three agens
got together and combined their keys, they could explode the Earth. This
measure was to be used only as a last recourse.

Since I love math/cryptography/secret sharing , I decided to implement a
version of the Osterhagen keys using Shamir's secret sharing (by polynomial
interpolation). This script can be used to share a secret number between
several parties. The secret can be recovered only if a sufficient number of
parties wants to.

## DISCLAIMER

I cannot be held responsible if someone blows up the Earth using this script.
And it goes without saying that I'm not affiliated in any way with the BBC,
Doctor Who, David Tennant etc.

## REQUIREMENTS

All you need is Python 3, and the Python3 Crypt library.

## USAGE

The `osterhagen` script has two functions:

    ./osterhagen.py -h
	usage: osterhagen [-h] {create-keys,recover-secret} ...

	To be used if the suffering of the human race is so great, so without hope,
	that this becomes the final option.

	optional arguments:
	  -h, --help            show this help message and exit

	subcommands:
	  available actions

	  {create-keys,recover-secret}
		                    choose the proper action to create the Osterhagen
							keys, or to recover the secret from Osterhagen keys

As you can see, there's a function to create Osterhagen keys, and a function
to recover the secret from a sufficient number of Osterhagen keys. The two
modes will be detailed further down.

Don't forget to make the script executable with:

    chmod +x osterhagen.py

### Key creation

To see a list of options, just issue:

    ./osterhagen.py create-keys -h
	usage: osterhagen create-keys [-h] -s SECRET [-n TOTAL_PARTIES]
								  [-k NEEDED_PARTIES]

	To be used if the suffering of the human race is so great, so without hope,
	that this becomes the final option.

	optional arguments:
	  -h, --help         show this help message and exit
	  -s SECRET          secret being shared by the Osterhagen keys
	  -n TOTAL_PARTIES   how many Osterhagen keys should be generated (default: 5)
	  -k NEEDED_PARTIES  how many Osterhagen keys should be necessary to recover
						 the whole secret (default: 3)

#### Secret

This parameter holds the secret number being shared by the parties.

#### Total parties

This parameter tells the script how many Osterhagen keys should be created.
Of course, at least two parties must share the secret (the Earth destruction
code is too much responsability for only one person).

#### Needed parties

This parameters determines how many parties must gather to recover the
whole secret. It must be between two and the total number of parties.

**NB:** every key is signed using an on-the-fly RSA private key. Therefore,
the script creates an RSA public key, which must be given to every party.

### Secret recovery

To see a list of options, just issue:

	usage: osterhagen recover-secret [-h] -f KEY_FILES [KEY_FILES ...]
									 --public-key PUBLIC_KEY

	To be used if the suffering of the human race is so great, so without hope,
	that this becomes the final option.

	optional arguments:
	  -h, --help            show this help message and exit
	  -f KEY_FILES [KEY_FILES ...]
							list of files containing the Osterhagen keys
	  --public-key PUBLIC_KEY
							RSA public key used to verify the Osterhagen keys'
							signature
#### Key files

This parameter is a list of the Osterhagen keys used to recover the secret:

#### Public key

In order to prevent the parties from mofidying their keys, they are all signed
using a private key created on the fly and destroyed immediately after use.
However, the public key used to verify the signature is given to each party.

#### Example

	./osterhagen recover-secret -f osterhagen_key_{1,3,4}.ohk --public-key pubkey.pem

## COPYRIGHT

Osterhagen
To be used if the suffering of the human race is so great, so without hope,
that this becomes the final option. 

Yannick Méheut [useless (at) utouch (dot) fr] - Copyright © 2013

This program is free software: you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the 
Free Software Foundation, either version 3 of the License, or (at your 
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
Public License for more details.

You should have received a copy of the GNU General Public License along 
with this program. If not, see
[http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).
