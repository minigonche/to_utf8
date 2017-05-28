# -*- coding: utf-8 -*-
import sys

def remove_accents(path_file_in, path_file_out):

	file_out = open(path_file_out, 'w')

	with open(path_file_in) as f:
	    for line in f:
			line = str(line)	
			#Replaces all non-UTF-8 encoding
			#Special Characters
			line = line.replace('\xef','')
			line = line.replace('\xbb','')
			line = line.replace('\xbf','')
			line = line.replace('\r','')
			line = line.replace('\n','')

			#a
			line = line.replace("\\xc3\\xa0",'a')			
			line = line.replace("\\xc3\\xa1",'a')
			line = line.replace("\\xc3\\xa2",'a')
			line = line.replace("\\xc3\\xa3",'a')
			line = line.replace("\\xc3\\xa4",'a')
			line = line.replace("\\xc3\\xa5",'a')
			line = line.replace("\\xc3\\xa6",'a')
			line = line.replace("\\xc2\\xaa",'a')

			#A
			line = line.replace("\\xc3\\x80",'A')
			line = line.replace("\\xc3\\x81",'A')
			line = line.replace("\\xc3\\x82",'A')
			line = line.replace("\\xc3\\x83",'A')
			line = line.replace("\\xc3\\x84",'A')
			line = line.replace("\\xc3\\x85",'A')
			line = line.replace("\\xc3\\x86",'A')


			#e
			line = line.replace("\\xc3\\xa8",'e')			
			line = line.replace("\\xc3\\xa9",'e')
			line = line.replace("\\xc3\\xaa",'e')
			line = line.replace("\\xc3\\xab",'e')
			#E
			line = line.replace("\\xc3\\x88",'E')
			line = line.replace("\\xc3\\x89",'E')
			line = line.replace("\\xc3\\x8a",'E')
			line = line.replace("\\xc3\\x8b",'E')

			
			#i
			line = line.replace("\\xc3\\xac",'i')
			line = line.replace("\\xc3\\xad",'i')
			line = line.replace("\\xc3\\xae",'i')
			line = line.replace("\\xc3\\xaf",'i')
			#I
			line = line.replace("\\xc3\\x8c",'I')
			line = line.replace("\\xc3\\x8d",'I')
			line = line.replace("\\xc3\\x8e",'I')
			line = line.replace("\\xc3\\x8f",'I')
			
			#o
			line = line.replace("\\xc3\\xb2",'o')
			line = line.replace("\\xc3\\xb3",'o')
			line = line.replace("\\xc3\\xb4",'o')
			line = line.replace("\\xc3\\xb5",'o')
			line = line.replace("\\xc3\\xb6",'o')
			line = line.replace("\\xc3\\xb7",'o')
			line = line.replace("\\xc3\\xb8",'o')
			#O
			line = line.replace("\\xc3\\x92",'O')
			line = line.replace("\\xc3\\x93",'O')
			line = line.replace("\\xc3\\x94",'O')
			line = line.replace("\\xc3\\x95",'O')
			line = line.replace("\\xc3\\x96",'O')
			line = line.replace("\\xc3\\x98",'O')
			line = line.replace("\\xc3\\xb0",'O')

			#u
			line = line.replace("\\xc3\\xb9",'u')
			line = line.replace("\\xc3\\xba",'u')	
			line = line.replace("\\xc3\\xbb",'u')	
			line = line.replace("\\xc3\\xbc",'u')	

			line = line.replace("\\xc3\\x99",'u')	
			line = line.replace("\\xc3\\x9a",'u')	
			line = line.replace("\\xc3\\x9b",'u')	
			line = line.replace("\\xc3\\x9c",'u')	

			#c
			line = line.replace("\\xc3\\xa7",'c')	
			line = line.replace("\\xc3\\x87",'c')	
			line = line.replace("\\xc2\\xa2",'c')

			#n
			line = line.replace("\\xc3\\xb1",'n')
			line = line.replace("\\xc3\\x91",'N')
																
			#y
			line = line.replace("\\xc3\\xbd",'y')	
			line = line.replace("\\xc3\\xbf",'y')
			line = line.replace("\\xc2\\xa5",'Y')
					
			#B
			line = line.replace("\\xc3\\x9f",'B')		

			#p
			line = line.replace("\\xc3\\x9e",'p')
			line = line.replace("\\xc3\\xbe",'p')

			#R
			line = line.replace("\\xc2\\xae",'R')
			
			#L
			line = line.replace("\\xc2\\xa3",'L')

			#x
			line = line.replace("\\xc3\\x97",'x')
			
			#numbers	
			line = line.replace("\\xc2\\xb9",'1')
			line = line.replace("\\xc2\\xbd",'2')
			line = line.replace("\\xc2\\xbc",'4')
			line = line.replace("\\xc2\\xbe",'3')
			line = line.replace("\\xc2\\xb2",'2')
			line = line.replace("\\xc2\\xb3",'3')

			#Weird shit
			line = line.replace("\\xc2\\xb7",'')
			line = line.replace("\\xc2\\xb0",'')
			line = line.replace("\\xc2\\xba",'')
			line = line.replace("\\xc2\\xab",'')
			line = line.replace("\\xc2\\xbb",'')
			line = line.replace("\\xc2\\xad",'')
			line = line.replace("\\xc2\\x96",'')

			
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

if __name__ == '__main__':
    
    remove_accents(sys.argv[1],sys.argv[2])

