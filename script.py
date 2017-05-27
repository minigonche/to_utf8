# -*- coding: utf-8 -*-
import sys

def remove_accents(path_file_in, path_file_out):

	file_out = open(path_file_out, 'w')

	with open(path_file_in) as f:
	    for line in f:
			#Replaces all non-UTF-8 encoding
			#Special Characters
			line = line.replace('\xef','')
			line = line.replace('\xbb','')
			line = line.replace('\xbf','')
			line = line.replace('\r','')
			line = line.replace('\n','')
			line = line.replace("\xc3\xa8",'e')
			line = line.replace("\xc3\xa9",'e')
			line = line.replace("\xc3\xaa",'e')
			
				
			line = line.replace("\xc3\xa0",'a')
			line = line.replace("\xc3\xa1",'a')
			line = line.replace("\xc3\xa2",'a')
			line = line.replace("\xc3\xa3",'a')
			line = line.replace("\xc3\xa4",'a')
			line = line.replace("\xc3\xa5",'a')
			line = line.replace("\xc3\xa6",'a')
			
			
			
			

			#Gramatic Characters
			line = line.replace('á','a')
			line = line.replace('é','e')
			line = line.replace('í','i')
			line = line.replace('ó','o')
			line = line.replace('ú','u')
			line = line.replace('Á','A')
			line = line.replace('É','E')
			line = line.replace('Í','I')
			line = line.replace('Ó','O')
			line = line.replace('Ú','U')

			line = line.replace('ñ','n')

			file_out.write(line)
			file_out.write('\n')

	file_out.close()

#end of remove_accents

if __name__ == "__main__":
    
    remove_accents(sys.argv[1],sys.argv[2])

