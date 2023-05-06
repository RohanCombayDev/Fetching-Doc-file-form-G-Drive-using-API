# Fetching-Doc-file-form-G-Drive-using-API

This repo contains python code to fetch data from particular google docs file using API and store it in .txt file.

First you have to go to console.developers.google.com and enable API service for gdrive and gdocs.

Then create a OAuth account and download the json file which has credentials and save that json file as "credentials.json".

In the code , replace the document name with the document name you want to fetch data from.

Also create one text file with name "file.txt" in the same folder which contains code.

main.py has the code to fetch data from gdrive and save it to .txt file

text to doc.py has the code to convert that text file to docx file and also change its encoding format to utf-8

# SETUP

install necerssary python libraries

pip install google-api-python-client

pip install PyDrive

pip install docx

pip install requests

