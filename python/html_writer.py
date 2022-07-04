# FastDup Software, (C) copyright 2022 Dr. Amir Alush and Dr. Danny Bickson.
# This software is free for non-commercial and academic usage under the Creative Common Attribution-NonCommercial-NoDerivatives
# 4.0 International license. Please reach out to info@databasevisual.com for licensing options.

#https://stackoverflow.com/questions/47704441/applying-styling-to-pandas-dataframe-saved-to-html-file
import pandas as pd 

def write_to_html_file(df, title='', filename='out.html'): 
    ''' Write an entire dataframe to an HTML file with nice formatting. ''' 
    result = ''' 
<html> <head> <style>
html{ 
font-family: Tahoma, Geneva, sans-serif;
}
table { 
border-collapse: collapse; 
font-family: Tahoma, Geneva, sans-serif;
}
table, th, tr, td 
{ 
border: 0px !important; 
border-collapse: collapse !important; 
border:none !important; 
outline:none !important; 
text-align: left;
}
table td { 
padding: 15px;
}
table thead td { 
background-color: #54585d; 
color: #ffffff; 
font-weight: bold; 
font-size: 13px;
}
table tbody td { 
color: #636363;
}
table tbody tr 
{ 
background-color: #f9fafb;
}
                                    
table tbody tr:nth-child(odd) { 
background-color: #ffffff;
}
    </style> </head> <body> ''' 
    result += '<center><h2> %s </h2></center>\n' % title 
    result += df.to_html(classes='wide', escape=False) 
    result += ''' </body> 
        </html> '''
    with open(filename, 'w') as f: 
        f.write(result)
