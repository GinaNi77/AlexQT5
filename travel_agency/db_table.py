script = """
DROP SCHEMA IF EXISTS `travel_agency` ;

CREATE SCHEMA IF NOT EXISTS `travel_agency` DEFAULT CHARACTER SET utf8 ;
USE `travel_agency` ;

DROP TABLE IF EXISTS `travel_agency`.`Customer` ;

CREATE TABLE IF NOT EXISTS `travel_agency`.`Customer` (
  `idCustomer` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(11) NULL,
  PRIMARY KEY (`idCustomer`));

DROP TABLE IF EXISTS `travel_agency`.`Country` ;

CREATE TABLE IF NOT EXISTS `travel_agency`.`Country` (
  `idCountry` INT NOT NULL AUTO_INCREMENT,
  `nameCountry` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCountry`));

DROP TABLE IF EXISTS `travel_agency`.`Tour` ;

CREATE TABLE IF NOT EXISTS `travel_agency`.`Tour` (
  `idTour` INT NOT NULL AUTO_INCREMENT,
  `idCountry` INT NOT NULL,
  `nameTour` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTour`),
  CONSTRAINT `idCountryT`
    FOREIGN KEY (`idCountry`)
    REFERENCES `travel_agency`.`Country` (`idCountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

DROP TABLE IF EXISTS `travel_agency`.`Hotel` ;

CREATE TABLE IF NOT EXISTS `travel_agency`.`Hotel` (
  `idHotel` INT NOT NULL AUTO_INCREMENT,
  `nameHotel` VARCHAR(45) NOT NULL,
  `idCountry` INT NOT NULL,
  `costHotel` INT NOT NULL,
  PRIMARY KEY (`idHotel`),
  CONSTRAINT `idCountry`
    FOREIGN KEY (`idCountry`)
    REFERENCES `travel_agency`.`Country` (`idCountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


DROP TABLE IF EXISTS `travel_agency`.`Excursion` ;

CREATE TABLE IF NOT EXISTS `travel_agency`.`Excursion` (
  `idExcursion` INT NOT NULL AUTO_INCREMENT,
  `nameExcursion` VARCHAR(45) NOT NULL,
  `descriptionExcursion` VARCHAR(255) NULL,
  `dateOfExcursion` DATE NOT NULL,
  `cost` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idExcursion`));

DROP TABLE IF EXISTS `travel_agency`.`CustomerTour` ;

CREATE TABLE IF NOT EXISTS `travel_agency`.`CustomerTour` (
  `idCustomerTour` INT NOT NULL AUTO_INCREMENT,
  `idCustomer` INT NOT NULL,
  `beginDateOfTour` DATE NOT NULL,
  `endDateOfTour` DATE NOT NULL,
  `durationOfTour` INT NULL,
  `idTour` INT NOT NULL,
  `costTour` DECIMAL(10,2) NULL,
  `idHotel` INT NOT NULL,
  `idExcursion` INT NOT NULL,
  `sumSale` DECIMAL(10,2) NULL,
  PRIMARY KEY (`idCustomerTour`),
  CONSTRAINT `idTour`
    FOREIGN KEY (`idTour`)
    REFERENCES `travel_agency`.`Tour` (`idTour`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idCustomer`
    FOREIGN KEY (`idCustomer`)
    REFERENCES `travel_agency`.`Customer` (`idCustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idHotel`
    FOREIGN KEY (`idHotel`)
    REFERENCES `travel_agency`.`Hotel` (`idHotel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idExcursion`
    FOREIGN KEY (`idExcursion`)
    REFERENCES `travel_agency`.`Excursion` (`idExcursion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

DROP TABLE IF EXISTS `travel_agency`.`Passport` ;

CREATE TABLE IF NOT EXISTS `travel_agency`.`Passport` (
  `idPassport` INT NOT NULL AUTO_INCREMENT,
  `passportNo` VARCHAR(10) NOT NULL,
  `dateOfIssue` DATE NOT NULL,
  `dateOfExpiry` DATE NOT NULL,
  `idCustomer` INT NOT NULL,
  PRIMARY KEY (`idPassport`),
  CONSTRAINT `idCustomerP`
    FOREIGN KEY (`idCustomer`)
    REFERENCES `travel_agency`.`Customer` (`idCustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""