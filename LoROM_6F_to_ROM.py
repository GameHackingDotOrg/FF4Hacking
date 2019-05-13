# LoROM 6F to ROM Convertor
# v1.00
# By Lazy Bastard of GameHacking.org (thanks to b0ardface for providing most of the LoROM_to_ROM_6F function, and to MathOnNapkins for providing the last nudge in the right direction).

# This Python script takes an input file containing LoROM 6F addresses (00:8000 - 6F:FFFF) and prints a list of corresponding ROM addresses (binary offsets) in hex, to screen.

# Usage:
# 1. Create a text file named input.txt in the same directory as LoROM_6F_to_ROM.py, containing one LoROM 6F address per line with no $ or : characters (just use Replace All to remove these).
# ...then either:
# 2a. Run this script at the command line with no arguments ("LoROM_6F_to_ROM.py", without quotes), then copy and paste the output wherever you like.
# ...or:
# 2b. Output to a file by doing something like "LoROM_6F_to_ROM.py > output.txt" at the command line (without quotes).

def LoROM_6F_to_ROM(addr):
	return ((addr & 0x7F0000) >> 1) | (addr & 0x7FFF)

InputFile = open("input.txt", "r")
	
for i in InputFile:
	TempVariable = LoROM_6F_to_ROM(int(i, 16))
	print '0x{0:0{1}X}'.format(TempVariable,6)
