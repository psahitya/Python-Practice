Python-Practice
===============

This is a repository to practice my python skills 

My first python program
=========================

I have multiple files in a folder and the file names are saved as 1.sql, 2.sql… Each file has the SQLs for different OBIEE reports and the first line in the file contains the parameter SAW_SRC_PATH=’report path’. ‘report path’ is how it is saved in the catalog. I want to output the file name and just the report path together in a CSV fomat. 

Suppose your files are in /automated_scripts/sql-dir directory. I want the output file sql_report_path.csv under /automated_scripts.

I will use python here. I will save the below code as read_n_extract_sql_file.py
