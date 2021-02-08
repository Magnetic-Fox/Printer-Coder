#! /usr/bin/env python3

# ---------------------------------------------------------------------------- #
# Epson FX-80 control codes file creator.                                      #
# Version 0.5                                                                  #
#                                                                              #
# by Magnetic-Fox                                                              #
#                                                                              #
# Copyright (c) 2014-2021 Bartłomiej "Magnetic-Fox" Węgrzyn                    #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Import section.                                                              #
# ---------------------------------------------------------------------------- #

import json

# ---------------------------------------------------------------------------- #
# Dictionary section.                                                          #
# ---------------------------------------------------------------------------- #

Epson = dict()
Codes = dict()

# ---------------------------------------------------------------------------- #
# Control codes section.                                                       #
# ---------------------------------------------------------------------------- #

Codes["Italic"]           = "\x1B\x34"
Codes["NoItalic"]         = "\x1B\x35"
Codes["Bold"]             = "\x1B\x45"
Codes["NoBold"]           = "\x1B\x46"
Codes["Underline"]        = "\x1B\x2D\x01"
Codes["NoUnderline"]      = "\x1B\x2D\x00"

Codes["NLQ"]              = "\x1B\x78\x31"
Codes["UTL"]              = "\x1B\x78\x30"
Codes["HSD"]              = "\x1B\x28\x30"

Codes["10CPI"]            = "\x1B\x50"
Codes["12CPI"]            = "\x1B\x4D"
Codes["15CPI"]            = "\x1B\x67"
Codes["17CPI"]            = "\x1B\x0F"

Codes["NoCompressedMode"] = "\x12"

Codes["SubScript"]        = "\x1B\x53\x31"
Codes["SupScript"]        = "\x1B\x53\x30"
Codes["NoSubSupScript"]   = "\x1B\x54"

Codes["DoubleHeight"]     = "\x1B\x77\x31"
Codes["NoDoubleHeight"]   = "\x1B\x77\x30"
Codes["DoubleWidth"]      = "\x1B\x57\x31"
Codes["NoDoubleWidth"]    = "\x1B\x57\x30"

Codes["LineFeed"]         = "\x0A"
Codes["FormFeed"]         = "\x0C"
Codes["CarriageReturn"]   = "\x0D"

# ---------------------------------------------------------------------------- #
# Main dicrionary root section.                                                #
# ---------------------------------------------------------------------------- #

Epson["FileTitle"]        = "Epson FX-80 Control Codes"
Epson["FileAuthor"]       = "Bartłomiej \"Magnetic-Fox\" Węgrzyn"
Epson["FileCopyright"]    = "(C) 2014-2021 Magnetic-Fox"
Epson["FileDescription"]  = "This file provides simple (not all now)" \
                            " Epson FX-80 control codes."
Epson["FileCodes"]        = Codes

# ---------------------------------------------------------------------------- #
# Dictionary export (JSON) section.                                            #
# ---------------------------------------------------------------------------- #

configFile = open("EpsonFX80.json","w")
configData = json.dumps(Epson)
configFile.write(configData)
configFile.close()
