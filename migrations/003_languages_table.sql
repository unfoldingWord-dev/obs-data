CREATE TABLE languages
(
  id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  language_name VARCHAR(255) DEFAULT '' NOT NULL,
  language_code VARCHAR(25) DEFAULT '' NOT NULL,
  anglicised_name VARCHAR(255) DEFAULT '' NOT NULL,
  region VARCHAR(50) DEFAULT '' NOT NULL,
  KEY `idx_lang_code` (`language_code`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8mb4 COLLATE=utf8mb4_unicode_ci;
