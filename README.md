# pdfMergeIt
The script that simplifies the process of merging multiple PDF files into a single document. The script has been developed to eliminate the need for users to struggle with complicated online tools and software that can often be confusing and difficult to use.

### Requirements:

Python 3.x or higher installed on your device
PyPDF2 library installed (you can install it using pip install PyPDF2)

### Using: 

```python
   python merge.py <directory> <output_file>  
   Example: python merge.py /home/user/Downloads/ /home/user/Downloads/merged.pdf
```
   
```
   flags:
    -h, --help: show help message and exit
    -d, --directory: directory containing pdf files to be merged
    -o, --output: output file name
    -n, --number: number of pages in the output file
    -s, --sort: sort the pdf files in the directory by name before merging them
```
