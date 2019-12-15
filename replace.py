from __future__ import print_function
import sys
import os
#import getopt

def file_switch(file_, pairs, reverse):
	first = 1 if reverse else 0
	second = 0 if reverse else 1
	print(file_ , pairs, reverse ,first, second)
	file = open(file_ , "r")
	text = ""
	for line in file.readlines():
		for pair in pairs:
			line = line.replace(pair[first] , pair[second])
		text += line
	file = open(file_ , "w")
	file.write(text)
	
	
		
	
		
	
def file_parse(file): 
#key1:
#	listElm1
#	listElm2
#;
#key2:
#	listElm1
#	listElm2
#;
	changes_read = open(file, "r")
	
	dict = {}
	ch_file = ""
	ch_list = []
	for line in changes_read.readlines():
		line = line.strip('\n\t')
		if "file-:" in line:
			ch_file = line.split(':')[1]
			ch_list = []
		elif ';' in line:
			dict[ch_file]=ch_list
			ch_file = ""
		else:
			ch_list.append(line.split('-'))
			
	return dict
	

def main(args):
	reverse = False
	interactive = False
	changes_file = args[1]
	for arg in args[2:]:
		reverse += arg in ['-r', "reverse",  "back"]
		interactive += arg in ['-i', "inter", "interactive"]
	print(reverse, interactive)
	if not os.path.isfile(changes_file):
		print( changes_file + ": doesn't exist")
		return
		
	Pairs_dict = file_parse(changes_file)
	for key in Pairs_dict.keys():
		if not os.path.isfile(key):
			print(key + ": doesn't exist")
			continue
		if (interactive):
			print("Would you want to change " , key)
			engage = raw_input("y/n ?")
			if engage in ['n' , 'N' , "no" , "No" , "meh" , "pass" , "Hell no!"]:
				continue
		file_switch(key, Pairs_dict[key], reverse)


def test_switch(args):
	print(args)
	file_switch("file1" , [['a','A'],['r','R']], args[1])
	
	
if __name__ == "__main__":
	#test_switch(sys.argv)
	main(sys.argv)