from app import file_utils
from app import url_utils
import csv
import mysql.connector


# download the file
url = 'https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv'
data = url_utils.get_url(url)

# split into rows
rows = data.split('\n')

# remove the first row, and blank rows
header = rows.pop(0)
rows = list(filter(None, rows))

settings = file_utils.load_json_object('./config/settings.json')

cnx = mysql.connector.connect(user=settings['user'], password=settings['password'],
                              host=settings['host'], database=settings['database'])
cursor = cnx.cursor()

# clear the table
# sql = 'DELETE FROM phil.countries WHERE id >= 0'
# cursor.execute(sql)

# loop through the data rows
sql = '''
INSERT INTO phil.countries (country_name, alpha2, alpha3, country_code, iso_3166_2, region, sub_region, region_code, sub_region_code) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

reader = csv.reader(rows, delimiter=',')
for row in reader:

    # name, alpha-2, alpha-3, country-code, iso_3166-2, region, sub-region, region-code, sub-region-code
    values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    cursor.execute(sql, values)

cnx.commit()

sql = '''
UPDATE phil.countries SET sub_region = 'Northern America'
WHERE region = 'Americas' AND sub_region IN ('Caribbean', 'Central America');
'''

cursor.execute(sql)
cnx.commit()

cnx.close()

print('Finished.')
