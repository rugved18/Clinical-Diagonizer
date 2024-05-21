# Developed by SBS5
# Last Modified - 21-01-2020

# MAKES AN EXCEL DATABASE OF ALL THE TABLES IN A SQL DATABASE. 
# DB2xl - INPUT - filepath of .db file
# DB2xl - OUTPUT - Excel file with tablenames as sheet names.

import sqlite3
import pandas as pd
import os

class db2xl:
    
    def toExcel(self):
         conn = sqlite3.connect(self.filepath)
         c = conn.cursor()
         writer = pd.ExcelWriter("db2XL.xlsx")
         with conn:
             c.execute("SELECT name FROM sqlite_master WHERE type='table';")
             tables = c.fetchall()
             tables = self.flatten(tables)
             
             for table in tables:
                 columns = []
                 
                 query = "SELECT * FROM " + str(table)
                 
                 cols = c.execute(query)
                 cols = cols.description
                 columns = self.get_cols(cols)
                 data = c.fetchall()
                 df = pd.DataFrame(data, columns = columns)
                 df.to_excel(writer, sheet_name = str(table))
                 
             writer.save()
    
    def flatten(self, llist):
        ret = [ ]
        for sublist in llist:
            for subelement in sublist:
                ret.append(subelement)
        return ret
    
    def get_cols(self, cols):
        columns = []
        for col in cols:
            columns.append(col[0])
        return columns
        
        
        
    def __init__(self, dbfile):
        self.filepath = dbfile
        self.toExcel()
        
        
#  UNCOMMENT THE FOLLOWING CODE TO RUN.
        
db2xl(dbfile = r'CDDB.db')
os.startfile('db2XL.xlsx')
