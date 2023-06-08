import os, sys, platform

bit = platform.architecture()[0]

if bit == '64bit':

	import Loader_enc

else:

	import Loader_enc

elif bit == '32bit':

	import Loader32

else:

	import Loader32
