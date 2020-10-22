CREATE DATABASE IF NOT EXISTS EverGreen;
USE EverGreen;
CREATE TABLE IF NOT EXISTS pedidos(
	id_pedido INT AUTO_INCREMENT,
    producto VARCHAR(50) NOT NULL,
    url_imagen VARCHAR(200),
    fecha_pedido DATE,
    fecha_entrega DATE,
    PRIMARY KEY(id_pedido)
)ENGINE=INNODB;