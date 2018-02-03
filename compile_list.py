import mysql.connector
from app import file_utils

settings = file_utils.load_json_object('./config/settings.json')

cnx = mysql.connector.connect(user=settings['user'], password=settings['password'],
                              host=settings['host'], database=settings['database'])
cursor = cnx.cursor()

sql = '''
SELECT
  CASE WHEN c.region IS NULL THEN CASE l.region WHEN 'Americas' THEN 'South America' ELSE l.region END
  ELSE CASE c.region WHEN 'Americas' THEN c.sub_region ELSE c.region END END AS language_region,
  l.language_code
FROM phil.languages AS l LEFT JOIN phil.language_countries AS lc ON l.language_code = lc.language_code
  LEFT JOIN phil.countries AS c ON lc.country_code = c.alpha2
GROUP BY language_code, language_region
HAVING language_region <> ''
ORDER BY language_region, language_code;
'''

results = {}
cursor.execute(sql)

for (language_region, language_code) in cursor:

    print('Processing %s' % language_code)

    if language_region not in results:
        results[language_region] = [language_code]
    else:
        results[language_region].append(language_code)

cursor.close()
cnx.close()

results['NorthAmerica'] = results.pop('Northern America')
results['SouthAmerica'] = results.pop('South America')

file_utils.write_file('./output/region_data.json', results)
