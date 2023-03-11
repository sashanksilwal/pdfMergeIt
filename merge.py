'''
    Script to merge multiple pdf files into one pdf file.
    Usage: python merge.py <directory> <output_file> 
    Example: python merge.py /home/user/Downloads/ /home/user/Downloads/merged.pdf

    flags:
    -h, --help: show help message and exit
    -d, --directory: directory containing pdf files to be merged
    -o, --output: output file name
    -n, --number: number of pages in the output file
    -s, --sort: sort the pdf files in the directory by name before merging them 
'''

import os
import sys
import argparse
import PyPDF2

# parse the command line arguments

parser = argparse.ArgumentParser(description='Merge multiple pdf files into one pdf file.')
parser.add_argument('-d', '--directory', help='directory containing pdf files to be merged', required=True)
parser.add_argument('-o', '--output', help='output file name', required=True)
parser.add_argument('-n', '--number', help='number of pages in the output file', required=True)
parser.add_argument('-s', '--sort', help='sort the pdf files in the directory by name before merging them', action='store_true')
args = parser.parse_args()

#  validate the command line arguments

# variable to count the number of files merged
count = 0

# get the directory containing pdf files to be merged
directory = args.directory

# get the output file name
output_file = args.output

# get the number of pages in the output file
number = args.number

animation = ["[■***********]","[■■**********]", "[■■■*********]", "[■■■■********]", "[■■■■■*******]", "[■■■■■■******]", "[■■■■■■■*****]", "[■■■■■■■■****]", "[■■■■■■■■■***]", "[■■■■■■■■■■**]","[■■■■■■■■■■■*]","[■■■■■■■■■■■■]"]

# get all the pdf files in the directory and sort them by name if the sort flag is set
fileNames = os.listdir(directory)

if args.sort:
    fileNames.sort()

# create a pdf writer object for writing the output pdf file
pdfWriter = PyPDF2.PdfWriter()

# loop through all the pdf files
for i in range(len(fileNames)):

    # CHECK IF THE FILE IS A PDF FILE
    if not fileNames[i].endswith('.pdf'):
        continue

    # increment the count
    count += 1
     
    # create a pdf file object for reading the pdf files
    pdfFileObj = open(directory + "/"+ fileNames[i], 'rb')

    # create a pdf reader object for reading the pdf files
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # loop through all the pages (except the first) and add them
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]  
        pdfWriter.add_page(pageObj)

    # close the pdf file object
    pdfFileObj.close()

    # print the progress
    print(animation[i % len(animation)], end="\r")
    

# write the merged pdf file
pdfOutput = open(output_file, 'wb')
pdfWriter.write(pdfOutput)

# close the pdf writer object
pdfOutput.close()

# print the number of pages in the output file
print('Number of pages in the output file: ' + str(number))

# print the output file name
print('Output file: ' + output_file)

# print the directory containing the output file
print('Directory: ' + directory)


# print the number of files merged
print('Number of files merged: ' + str(count))

# TO DO:
# 1. Get the number of pages in the output file from the user and mege the pdf files accordingly
# 2. Debug the script to work with all pdf files
 
