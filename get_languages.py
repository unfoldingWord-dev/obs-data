from app import file_utils
from app import url_utils
import mysql.connector


# download the languages
rows = url_utils.get_languages()

settings = file_utils.load_json_object('./config/settings.json')

cnx = mysql.connector.connect(user=settings['user'], password=settings['password'],
                              host=settings['host'], database=settings['database'])
cursor = cnx.cursor()

# loop through the data rows
sql = '''
INSERT INTO phil.languages (language_name, language_code, anglicised_name, region) 
VALUES (%s, %s, %s, %s);
'''

sql2 = '''
INSERT INTO phil.language_countries (language_code, country_code)
VALUES (%s, %s)
'''

for row in rows:

    print('Processing %s (%s)' % (row['ln'], row['lc']))

    values = (row['ln'], row['lc'], row['ang'], row['lr'])
    cursor.execute(sql, values)

    for cc in row['cc']:
        values = (row['lc'], cc)
        cursor.execute(sql2, values)

    cnx.commit()

cnx.close()

print('Finished.')
