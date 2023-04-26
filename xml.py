import xml.etree.ElementTree as ET
import cur as cursor
import psycopg2


#1. Programm liest XML-Datei aus using Python ElementTree
#5. Programm übernimmt daten aus beliebig vielen Dateien (alle) in die SQL-Tabellen aus Aufgabe 3.

#datei = input("Bitte geben Sie Datei Name ein:")
#datei ='Inventory/'+datei
tree = ET.parse('Inventory/ADDIN-TEST.xml')
root = tree.getroot()
#print(ET.tostring(root))


#2. Programm zeigt Programme und Admin User einer Inventory XML-Datei auf der Konsole an
#Aus der Inventory/ADDIN-TEST.xml Datei: Zeige alle Admin User (member) und alle Programme (prog) mit deren Namen auf der Konsole an.

#print("Computer Name :",tree.find('.//os').text)
#for x in tree.findall('.//software/prog'):
 #   print(x.attrib['key'],x.attrib['name'])

#for x in tree.findall('.//localgroups/localgroup/member'):
    #print(x.attrib['name'])

#3. Übertrage XML Struktur in passende SQL Tabellen in der PostgreSQL (manuell)
#Für die Programme, Administratoren und Computer.
#4. Programm übernimmt Daten aus einer XML-Datei in die in Aufgabe 3. erstellten SQL Tabellen




conn = None
cursor = None

try:
    conn = psycopg2.connect(
         host='localhost',
         user='postgres',
         port=5432,
         password='Db123',
         dbname='postgres')
    cursor = conn.cursor()

    for x in tree.findall('.//localgroups/localgroup/member'):
         sql = 'INSERT INTO public."localgroups" ("computer" , name) VALUES (%s , %s)'
         val = (tree.find('.//os').text,x.attrib['name'])
         conn.commit()
         print(cursor.rowcount, "record inserted.")
    '''''
    for x in tree.findall('.//software/prog'):
        sql = 'INSERT INTO public."Software" ("key", name, computer) VALUES (%s, %s ,%s)'
        val = (x.attrib['key'],x.attrib['name'], tree.find('.//os').text)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "record inserted.")
'''''

# 6. Programm liest alle Computername aus den SQL-Tabellen von Aufgabe 3 aus

    #cursor.execute('SELECT distinct "Computer" FROM public."ADDIN_TEST"')
    #for Computer in cursor:
       # print(Computer)

    #cursor.execute('DELETE  FROM public."Software" where "Software"."Computer" =\'Windows_NT\'')
    #cursor.execute('DELETE  FROM public."localgroups" where "localgroups"."Computer" =\'Windows_NT\'')


#7. Programm erlaubt Eingabe eines Computernames und lese alle Programme und Adminbenutzer von den SQL-Tabellen aus den vorherigen Aufgaben aus.
    '''''

    programme = cursor.execute('SELECT "Computer" FROM public."Software"')
    adminbenutzer = cursor.execute('SELECT "Computer" FROM public."localgroups"')
    computerName = input("Geben Sie Computername ein:")
    for computer in cursor:
       if computerName == programme:
           '''''

except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
'''''
for name in cursor:
    if tree.find(x.attrib['name']) != name:
        cursor.execute(sql, val)
'''''






