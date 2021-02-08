#! /usr/bin/env python3

# ---------------------------------------------------------------------------- #
# Control Codes Printer.                                                       #
# Version 1.0                                                                  #
#                                                                              #
# by Magnetic-Fox                                                              #
#                                                                              #
# Copyright (c) 2021 Bartłomiej "Magnetic-Fox" Węgrzyn                         #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Information section.                                                         #
# ---------------------------------------------------------------------------- #

__title__     = "Control Codes Printer"
__author__    = "Bartłomiej \"Magnetic-Fox\" Węgrzyn"
__version__   = 1.0
__copyright__ = "Copyright (c) 2021 Bartłomiej \"Magnetic-Fox\" Węgrzyn"

# ---------------------------------------------------------------------------- #
# Import section.                                                              #
# ---------------------------------------------------------------------------- #

import json
import sys

# ---------------------------------------------------------------------------- #
# Functions section.                                                           #
# ---------------------------------------------------------------------------- #

def programInfo(showHelpTip=True):
        print("Control Codes Printer, version 1.0, by Magnetic-Fox, Feb 2021")
        print("Usage: CodeOutput.py <CodesFileName> [Options] " \
              "[[CodeName], ...]")
        if showHelpTip:
                print("Type --help to get more information.")
        else:
                print("")

# ---------------------------------------------------------------------------- #
# Global variables section.                                                    #
# ---------------------------------------------------------------------------- #

Data = dict()
fileLoaded = False

# ---------------------------------------------------------------------------- #
# Main program section.                                                        #
# ---------------------------------------------------------------------------- #

if len(sys.argv) <= 1:

        programInfo()

else:

        for x in range(1, len(sys.argv)):

                if(x == 1) and (sys.argv[x][0] != '-'):

                        try:

                                file = open(sys.argv[1],"r")
                                fileData = file.read()
                                Data = json.loads(fileData)
                                file.close()
                                fileLoaded = True

                        except FileNotFoundError:

                                print("File not found: "+sys.argv[x],
                                      file=sys.stderr)
                                break

                        except json.decoder.JSONDecodeError:

                                print("File not valid: "+sys.argv[x],
                                      file=sys.stderr)
                                break

                        except:

                                print("Unknown error occured.",file=sys.stderr)
                                break

                else:

                        try:

                                if(sys.argv[x][0] == '-'):

                                        if(sys.argv[x][1::].upper() == 'I') \
                                          or(sys.argv[x][1::].upper() == \
                                            "-INFORMATION"):
                                            
                                                if not fileLoaded:
                                                        raise \
                                                        NameError("File not " \
                                                                  "loaded.")

                                                print("Codes File " \
                                                      "Title:       " \
                                                      + Data["FileTitle"])

                                                print("Codes File " \
                                                      "Author:      " \
                                                      + Data["FileAuthor"])

                                                print("Codes File " \
                                                      "Copyright:   " \
                                                      + Data["FileCopyright"])

                                                print("Codes File " \
                                                      "Description:\n" \
                                                      + Data["FileDescription"])

                                        elif(sys.argv[x][1::].upper() == 'L') \
                                            or(sys.argv[x][1::].upper() == \
                                              "-LIST"):
                                              
                                                if not fileLoaded:
                                                        raise \
                                                        NameError("File not " \
                                                                  "loaded.")

                                                print(Data["FileTitle"]+":")
                                                print("")

                                                for key in Data["FileCodes"] \
                                                           .keys():

                                                        print(" * "+key)
                                        
                                        elif(sys.argv[x][1::].upper() == 'H') \
                                            or(sys.argv[x][1::].upper() == \
                                              "-HELP"):
                                              
                                                programInfo(showHelpTip = False)
                                              
                                                print("Short options:")
                                                print("  -i               Get "\
                                                      "codes file information")
                                                print("  -l               " \
                                                      "List codes available " \
                                                      "in selected file")
                                                print("  -h               " \
                                                      "Print this help")
                                                print("")
                                                print("Long options:")
                                                print("  --information    Get "\
                                                      "codes file information")
                                                print("  --list           " \
                                                      "List codes available " \
                                                      "in selected file")
                                                print("  --help           " \
                                                      "Print this help")
                                                    
                                                if not fileLoaded:
                                                
                                                        break

                                        else:

                                                raise NameError("Unknown " \
                                                      "option: "+sys.argv[x])

                                else:
                                
                                        if not fileLoaded:
                                                raise NameError("File not " \
                                                                "loaded.")

                                        print(Data["FileCodes"][sys.argv[x]],
                                              end="")

                        except NameError as err:

                                print(err,file=sys.stderr)

                        except KeyError:

                                print("Code not found: "+sys.argv[x],
                                      file=sys.stderr)

                        except:

                                print("Unknown error occured: "+sys.argv[x],
                                      file=sys.stderr)
