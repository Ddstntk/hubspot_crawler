import openpyxl
from openpyxl import load_workbook


import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="clickray",
#   password="Binladen.11",
#   database="hubspot_search",
#   auth_plugin='mysql_native_password'
# )

# mycursor = mydb.cursor()


# mycursor.execute("SELECT lM.Location FROM sites s INNER JOIN locationMap lM ON s.Domain = lM.Domain;")

# domain_list = [item for t in mycursor.fetchall() for item in t]

# for x in myresult:
#   print(x)

# print(domain_list)

class DbHandler:
  mydb = mysql.connector.connect(
    host="localhost",
    user="clickray",
    password="Binladen.11",
    database="hubspot_search",
    auth_plugin='mysql_native_password'
  )

  mycursor = mydb.cursor()


  mycursor.execute("SELECT lM.Location FROM sites s INNER JOIN locationMap lM ON s.Domain=lM.Domain;")

  url_list = [item for t in mycursor.fetchall() for item in t]

  # print(domain_list)
  
  mycursor.execute("SELECT domain FROM sites")

  domain_list = [item for t in mycursor.fetchall() for item in t]

  def getUrls(self):
    return self.url_list

  def getDomains(self):
    return self.domain_list

  def putToDb(self, tablename, rows):


    values = ', '.join(map(str, rows))
    sql = "INSERT INTO " + tablename + "(URL, domain, subdomain, HubSpot, HubspotFormWrapper, start_coded_template, Start_of_HubSpot_Analytics_Code) VALUES {}".format(values)

    self.mycursor.execute(sql)
    self.mydb.commit()