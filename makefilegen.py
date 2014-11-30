#This script generates makefiles

import sys
import subprocess


if len(sys.argv) > 1:
	file_name = " ".join(sys.argv[1:])
else: 
	file_name = "Makefile"	
	
	
print 'Generating a makefile called ' + file_name


CC = "g++"
CFLAGS= "-std=c++14"

ld_flags_input = raw_input("You don't want LDFLAGS do you? \n  Press 'n' for none \n Press 'f' for -lfltk and -lfltk_images \n Enter in all the LDFLAGS (with spaces and '-') ")
if (ld_flags_input.strip() == 'n' or ld_flags_input == 'N'):
	LDFLAGS=""
elif (ld_flags_input.strip() == 'f' or ld_flags_input == 'F'):	
	LDFLAGS= "-lfltk -lfltk_images"
else:
	LDFLAGS= ld_flags_input


sources_input = raw_input("Enter all the file names of your source code, separated by spaces:")
SOURCES = sources_input


OBJECTS= "$(SOURCES:.cpp=.o)"

executable_input = raw_input("If you don't give me an executable name, its going to be 'freak.out'")
if executable_input == "":
	EXECUTABLE = "freak.out"
else:
	EXECUTABLE = executable_input

	
file_object = open(file_name , "w")
	
file_object.write("CC=" + CC + "\n")
file_object.write("CFLAGS=" + CFLAGS+ "\n")
file_object.write("LDFLAGS=" + LDFLAGS+ "\n")
file_object.write("SOURCES=" + SOURCES+ "\n")
file_object.write("OBJECTS=" + OBJECTS+ "\n")
file_object.write("EXECUTABLE=" + EXECUTABLE+ "\n")

file_object.write("all: $(SOURCES) $(EXECUTABLE)"+ "\n")
file_object.write("$(EXECUTABLE): \n")			
file_object.write("	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDFLAGS)"+ "\n")	

