#  Printer Coder

A simple suite of Python scripts done for easier dot-matrix printer usage.

## The goal of project

The goal of project is to provide really simple command-line tools for dynamic text formatting (currently working on it) and sending control codes to dot-matrix printers.
I decided to write some tools, because there aren't any for controlling dot-matrix printers. I'm afraid so much people today forget, that real printing on such devices is raw printing by sending just plaintext with occasional control codes (usually called escape codes, because nearly all of them starts with escape character - 0x1B in hex) instead of "printing" from applications, which is, in fact, image printing, not text printing...
In fact, there aren't much solutions for classic use of dot-matrix printer, which is the best way to get high quality results and it seems nobody really needs them. Well, except me, of course. So, let's do some ultra simple code. :)

## Some boring history

I've started doing some simple tools for my dot-matrix printer already in 2014 year. Those were the days... "Turbo Pascal is the best programming language on the world!", "MS-DOS is beautiful operating system!", "Why aren't people using only dot-matrix printers today?! These devices deserve much more love!" ...hahaha :D
Well, I was a teenager loving old times and old computers, having troubles forcing my old Windows XP laptop to print the way I want on my beloved OKI. :)
I've started making some tool for dynamic printing with text parsing, but have not much knowledge to do this properly.
It ended with control codes board allowing me to send single codes and with preparing text files in hex editor to make some bold font or superscripts. :D

But this year I decided to come back to this really old idea and try to program some easy command line tool that will help with printing properly.
I hope it will finally be done in some days. ;) 

## So, what's included in here?

This repository contains some tools written in Python to make some basic operations on dot-matrix printer easier. It isn't something really special - just simple set of few tools to make it possible without typing control codes and part of lines manually. I'm tired of it. ;)
At now, there aren't much scripts, because it's beginning of this little project. However, there is already something.

`CodeOutput` is a tool for manual output of chosen escape codes from dictionary file. It can send as much codes as you need in one task. It's such a debug tool for testing new dictionary files and for manual printing line by line or even word by word. Well, but not so easy to use, because this program can get names of control codes **only**! There is still need to combine them with rest of the printing job.

`EpsonFX80Codes` (placed in Generators directory) is really simple Python code which goal is to create a dictionary file for use with tools. It's great as a tutorial for creating own dictionary files.

There will be at least one tool yet - some kind of a "compiler" or, I don't know, a word processor? No, the word processor is too much to say. Well, something, that will be able to dynamically set printer while sending text - a kind of hypertext parser.
There should be, of course, some kind of documentation, I think. And I think it will be someday. :)

## How to use it?

These tools (currently one) are created to output data into the standard output, to make it possible to send it directly to the printer.
Using these programs is really easy - you just have to provide printer codes file and some control codes (available in that file) and pipe the output to the printer.
That's all. :)

Here is a simple example done using LPR command:
```
./CodeOutput.py EpsonFX80.json NLQ 12CPI LineFeed | lpr -l
```

The above code creates bytestream of control codes for Epson FX-80 dot-matrix printer, which changes font settings to Near Letter Quality with 12 characters per inch and performs one line feed. The whole stream is piped to the LPR, which, because of -L option selected, sends it to the printer in unchanged form, which is necessary to work properly.

Well, I can't provide another examples at now, because I haven't written other tools yet.

I hope it'll change quickly. ;) Give me some patience.

## Author

All files included in this repository are mine.
I've programmed all the tools and prepared dictionary files (currently only for Epson FX-80) using official documentation found on the internet yet in 2014.

- Bartłomiej "Magnetic-Fox" Węgrzyn - idea, dictionary files, programming

## Disclaimer

I've made an effort to program and test these codes to make them working properly. However, they can still contain bugs I haven't noticed.
You must remember, that this software is provided here "AS IS" and comes with absolutely no warranty. It's useful for me, but may not be useful for you.
Use these codes on your own risk!

## Copyright

If you find any of these files useful and wish to use them in your own production, remember to give me some simple credits for it - please, respect my work. Thank You! :)

Epson and FX-80 model name are registered trademarks of Seiko Epson Corporation, they are used here informational and to provide control codes for specific printer model, which is usually emulated by other printers.
OKI is registered trademark of Oki Electric Industry Co., Ltd.

All files provided here are property of mine.

Copyright © 2014-2021 Bartłomiej "Magnetic-Fox" Węgrzyn
