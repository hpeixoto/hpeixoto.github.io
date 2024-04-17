-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ubers
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ubers
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ubers` DEFAULT CHARACTER SET utf8 ;
USE `ubers` ;

-- -----------------------------------------------------
-- Table `ubers`.`carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ubers`.`carro` (
  `id_carro` INT NOT NULL,
  `marca` VARCHAR(45) NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  `combustivel` VARCHAR(45) NOT NULL,
  `horas` VARCHAR(45) NULL,
  PRIMARY KEY (`id_carro`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ubers`.`manutencao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ubers`.`manutencao` (
  `id_manutencao` INT NOT NULL,
  `id_carro` INT NOT NULL,
  `custo` DECIMAL(5,2) NOT NULL,
  `data_manutencao` DATE NOT NULL,
  `tipo_manutencao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_manutencao`),
  INDEX `~manutencao_fk1_idx` (`id_carro` ASC) VISIBLE,
  CONSTRAINT `~manutencao_fk1`
    FOREIGN KEY (`id_carro`)
    REFERENCES `ubers`.`carro` (`id_carro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ubers`.`condutor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ubers`.`condutor` (
  `cc` INT NOT NULL,
  `nome` VARCHAR(50) NOT NULL,
  `nr_carta` VARCHAR(45) NOT NULL,
  `data_nascimento` DATE NOT NULL,
  PRIMARY KEY (`cc`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ubers`.`viagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ubers`.`viagem` (
  `id_viagem` INT NOT NULL,
  `id_carro` INT NOT NULL,
  `id_condutor` INT NULL,
  `data_inicio` DATE NOT NULL,
  `data_fim` DATE NOT NULL,
  `numero_km` VARCHAR(7) NOT NULL,
  PRIMARY KEY (`id_viagem`),
  INDEX `viagem_fk1_idx` (`id_carro` ASC) VISIBLE,
  INDEX `viagem_fk2_idx` (`id_condutor` ASC) VISIBLE,
  CONSTRAINT `viagem_fk1`
    FOREIGN KEY (`id_carro`)
    REFERENCES `ubers`.`carro` (`id_carro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `viagem_fk2`
    FOREIGN KEY (`id_condutor`)
    REFERENCES `ubers`.`condutor` (`cc`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
