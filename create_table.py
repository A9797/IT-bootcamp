import json

# open the jason file and load the data into dictionary
with open ('fields.json') as jsonfile:
    data = json.load(jsonfile)

#extract the field names and types from the dictionary
field_names =[field["name"] for field in data["fields"]]
field_types =[field["type"] for field in data["fields"]]
print(field_names)
# format the field name
def format_name(text):
    text = text.replace("%", "")
    text = text.replace(",", "_")
    text = text.replace(" ", "_")
    text = text.lower()
    return text

# select the data type
def select_type(type_name):
    type_name = type_name.lower()
    if type_name == "code" or type_name == "text":
        return "VARCHAR"
    else:
        return type_name.upper()

#generate a SQL script to creat a table with the same fields and types
sql_script = "CREAT TABLE Products (\n"
for i in range(len(field_names)):
    field_name = format_name(field_names[i])
    field_type = select_type(field_types[i])
    sql_script += f" {field_name}   {field_type},\n"
sql_script = sql_script.rstrip(",\n") + "\n);"

#write the SQL script to a file
with open('creat_table.sql','w') as sqlfile:
    sqlfile.write(sql_script)

    #print the sql script for reference
print(sql_script)