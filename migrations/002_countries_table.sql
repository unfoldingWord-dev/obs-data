CREATE TABLE countries
(
  id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  country_name VARCHAR(255) DEFAULT '' NOT NULL,
  alpha2 VARCHAR(5) DEFAULT '' NOT NULL,
  alpha3 VARCHAR(5) DEFAULT '' NOT NULL,
  country_code VARCHAR(20) DEFAULT '' NOT NULL,
  iso_3166_2 VARCHAR(50) DEFAULT '' NOT NULL,
  region VARCHAR(50) DEFAULT '' NOT NULL,
  sub_region VARCHAR(50) DEFAULT '' NOT NULL,
  region_code VARCHAR(5) DEFAULT '' NOT NULL,
  sub_region_code VARCHAR(5) DEFAULT '' NOT NULL,
  KEY `idx_country_code` (`country_code`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8mb4 COLLATE=utf8mb4_unicode_ci;
