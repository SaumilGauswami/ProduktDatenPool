CREATE TABLE `manufacturers` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `data_sources` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `url` VARCHAR(255) NOT NULL,
  `wholesaler_name` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255),
  `postal_code` VARCHAR(20)
);

CREATE TABLE `products` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL,
  `model_number` VARCHAR(255),
  `power_output` DECIMAL(10, 2),
  `efficiency` DECIMAL(5, 2),
  `dimensions` VARCHAR(255),
  `weight` DECIMAL(10, 2),
  `cell_type` ENUM('Monocrystalline', 'Polycrystalline', 'Thin Film', 'Other'),
  `warranty` VARCHAR(255),
  `price` DECIMAL(10, 2),
  `manufacturer_id` INT,
  `data_source_id` INT,
  `last_updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id),
  FOREIGN KEY (data_source_id) REFERENCES data_sources(id)
);
