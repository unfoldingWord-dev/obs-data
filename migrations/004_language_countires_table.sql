CREATE TABLE language_countries
(
  id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  language_code VARCHAR(25) DEFAULT '' NOT NULL,
  country_code VARCHAR(20) DEFAULT '' NOT NULL,
  KEY `idx_lang_code` (`language_code`),
  KEY `idx_country_code` (`country_code`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8mb4 COLLATE=utf8mb4_unicode_ci;
