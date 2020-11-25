DROP TABLE IF EXISTS `gestioncompras`;
CREATE TABLE IF NOT EXISTS `gestioncompras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipoEgreso` varchar(45) NOT NULL,
  `tipoElemento` varchar(45) NOT NULL,
  `proveedor` varchar(45) NOT NULL,
  `formaPago` varchar(45) NOT NULL,
  `aprobacion` int(11) NOT NULL DEFAULT 0,
  `realizarPago` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
COMMIT;