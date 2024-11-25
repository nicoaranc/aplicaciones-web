-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema tarea2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tarea2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tarea2` DEFAULT CHARACTER SET utf8 ;
USE `tarea2` ;

-- -----------------------------------------------------
-- Table `tarea2`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`comuna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`comuna` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comuna_region1_idx` (`region_id` ASC),
  CONSTRAINT `fk_comuna_region1`
    FOREIGN KEY (`region_id`)
    REFERENCES `tarea2`.`region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`producto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo` ENUM('fruta', 'verdura') NOT NULL,
  `descripcion` VARCHAR(300) NULL,
  `comuna_id` INT NOT NULL,
  `nombre_productor` VARCHAR(80) NOT NULL,
  `email_productor` VARCHAR(30) NOT NULL,
  `celular_productor` VARCHAR(15) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_producto_comuna1_idx` (`comuna_id` ASC),
  CONSTRAINT `fk_producto_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `tarea2`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`foto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ruta_archivo` VARCHAR(300) NOT NULL,
  `nombre_archivo` VARCHAR(300) NOT NULL,
  `producto_id` INT NOT NULL,
  PRIMARY KEY (`id`, `producto_id`),
  INDEX `fk_foto_producto1_idx` (`producto_id` ASC),
  CONSTRAINT `fk_foto_producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `tarea2`.`producto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`tipo_verdura_fruta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`tipo_verdura_fruta` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`producto_verdura_fruta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`producto_verdura_fruta` (
  `producto_id` INT NOT NULL,
  `tipo_verdura_fruta_id` INT NOT NULL,
  INDEX `fk_artesano_tipo_producto1_idx` (`producto_id` ASC),
  INDEX `fk_artesano_tipo_tipo_frutaverdura1_idx` (`tipo_verdura_fruta_id` ASC),
  PRIMARY KEY (`tipo_verdura_fruta_id`, `producto_id`),
  CONSTRAINT `fk_producto_tipo_fruta_verdura1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `tarea2`.`producto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_producto_tipo_fruta_verdura_1`
    FOREIGN KEY (`tipo_verdura_fruta_id`)
    REFERENCES `tarea2`.`tipo_verdura_fruta` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`pedido` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo` ENUM('fruta', 'verdura') NOT NULL,
  `descripcion` VARCHAR(300) NULL,
  `comuna_id` INT NOT NULL,
  `nombre_comprador` VARCHAR(80) NOT NULL,
  `email_comprador` VARCHAR(30) NOT NULL,
  `celular_comprador` VARCHAR(15) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pedido_comuna1_idx` (`comuna_id` ASC),
  CONSTRAINT `fk_pedido_comuna10`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `tarea2`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`pedido_verdura_fruta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`pedido_verdura_fruta` (
  `tipo_verdura_fruta_id` INT NOT NULL,
  `pedido_id` INT NOT NULL,
  INDEX `fk_pedido_tipo_frutaverdura1_idx` (`tipo_verdura_fruta_id` ASC),
  PRIMARY KEY (`tipo_verdura_fruta_id`, `pedido_id`),
  INDEX `fk_pedido_verdurafruta_idx` (`pedido_id` ASC),
  CONSTRAINT `fk_pedido_tipo_fruta_verdura_10`
    FOREIGN KEY (`tipo_verdura_fruta_id`)
    REFERENCES `tarea2`.`tipo_verdura_fruta` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pedido_verdurafruta`
    FOREIGN KEY (`pedido_id`)
    REFERENCES `tarea2`.`pedido` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE USER 'cc5002'@'%' IDENTIFIED BY 'programacionweb';
GRANT ALL PRIVILEGES ON tarea2.* TO 'cc5002'@'%';
FLUSH PRIVILEGES;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

COMMIT;

