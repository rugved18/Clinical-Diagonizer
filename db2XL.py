import sqlite3
import pandas as pd
import os

class db2xl:
    
    def toExcel(self):
        conn = sqlite3.connect(self.filepath)
        c = conn.cursor()
        writer = pd.ExcelWriter("db2XL.xlsx", engine='xlsxwriter')  # Specify the engine explicitly
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
                df = pd.DataFrame(data, columns=columns)
                df.to_excel(writer, sheet_name=str(table), index=False)  # Avoid writing index
        writer.close()  # Close the writer to save the Excel file



    def flatten(self, llist):
        ret = []
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
        
if __name__ == "__main__":
    dbfile_path = r'CDDB.db'  # Specify the path to your SQLite database file
    db2xl(dbfile=dbfile_path).toExcel()
    os.startfile('db2XL.xlsx')
