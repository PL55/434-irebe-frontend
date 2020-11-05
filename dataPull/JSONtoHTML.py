import json

# This code is to add HTML table tags to a json file data and write it into a text

f = open('faculty.json')

data = json.load(f)


def convertJSONtoHMTL(data):
    table = ""
    for i in data:
        name = i["Name"]
        title = i["Title"]
        email = i["Email"]
        phone = i["Phone"]
        office = i["Office"]

        name = "<td>" + name[:-2] + "</td>"
        title = "<td>" + title + "</td>"
        email = "<td>" + email + "</td>"
        phone = "<td>" + phone + "</td>"
        office = "<td>" + office + "</td>"

        tableData = "\n\t" + name + "\n\t" + title + "\n\t" + email + "\n\t" + phone + "\n\t" + office + "\n"
        tableRow = "<tr>" + tableData + "</tr>" + "\n"
        table = table + tableRow

    return table

f.close()
rtn = convertJSONtoHMTL(data)
x = open("data.txt","w")
x.write(rtn)


