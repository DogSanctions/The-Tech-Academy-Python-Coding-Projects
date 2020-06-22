import sqlite3

conn = sqlite3.connect('Assignment_Database.db')
fileList = ('Hello.txt', 'myImage.png', 'data.pdf', 'myMovie.mpg', 'World.txt', 'information.docx')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_ftype TEXT \
        )")
    conn.commit()

conn = sqlite3.connect('Assignment_Database.db')

for items in fileList:
    if items.endswith('txt'):
        cur.execute('INSERT INTO tbl_files(col_fname) VALUES (?)', (items,))
    conn.commit()

cur.execute('SELECT col_fname FROM tbl_files')
msg = cur.fetchall()
print("These files end with .txt"+str(msg))
conn.commit()
conn.close()
