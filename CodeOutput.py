#! /usr/bin/env python3

# ---------------------------------------------------------------------------- #
# Control codes printer.                                                       #
# Version 0.5                                                                  #
#                                                                              #
# by Magnetic-Fox                                                              #
#                                                                              #
# Copyright (c) 2021 Bartłomiej "Magnetic-Fox" Węgrzyn                         #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Import section.                                                              #
# ---------------------------------------------------------------------------- #

import json
import sys

# ---------------------------------------------------------------------------- #
# Dictionary section.                                                          #
# ---------------------------------------------------------------------------- #

Data = dict()

# ---------------------------------------------------------------------------- #
# Main program section.                                                        #
# ---------------------------------------------------------------------------- #

if len(sys.argv) <= 1:
        print("Control Codes Printer")
        print("Version 0.5")
        print("by Magnetic-Fox")
        print("")
        print("Usage: CodeOutput.py <CodesFileName> [-I] [-L] " \
              "[[CodeName], ...]")
else:
        for x in range(1, len(sys.argv)):
                if(x == 1):
                        try:
                                file = open(sys.argv[1],"r")
                                fileData = file.read()
                                Data = json.loads(fileData)
                                file.close()
                        except FileNotFoundError:
                                print("File not found: "+sys.argv[x],
                                      file=sys.stderr)
                        except json.decoder.JSONDecodeError:
                                print("File not valid: "+sys.argv[x],
                                      file=sys.stderr)
                        except:
                                print("Unknown error occured.",file=sys.stderr)
                else:
                        try:
                                if(sys.argv[x][0] == '-'):
                                        if(sys.argv[x][1].upper() == 'I'):
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
                                        elif(sys.argv[x][1].upper() == "L"):
                                                print(Data["FileTitle"]+":")
                                                print("")
                                                for key in Data["FileCodes"] \
                                                           .keys():
                                                        print(" * "+key)
                                        else:
                                                raise NameError("Unknown " \
                                                      "option: "+sys.argv[x])
                                else:
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
