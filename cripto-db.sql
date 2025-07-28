-- Posicao
CREATE TABLE posicao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carteira_id INT NOT NULL,
    abertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Aberta', 'Encerrada') DEFAULT 'Aberta',
    encerramento DATETIME,
    compra_dolar DECIMAL(10,2) NOT NULL,
    moeda_investida INT NOT NULL,
    total_compra_moeda_investida DECIMAL(20,10),
    FOREIGN KEY (carteira_id) REFERENCES carteira(id),
    FOREIGN KEY (moeda_investida) REFERENCES moedas(id)
);

-- Moedas
CREATE TABLE moedas (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	sigla VARCHAR(10) NOT NULL
);

-- Carteira
CREATE TABLE carteira (
	id INT AUTO_INCREMENT PRIMARY KEY,
	usuario_id INT NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);
-- Usuário
CREATE TABLE usuario (
	id INT AUTO_INCREMENT PRIMARY KEY,
	login VARCHAR(50) NOT NULL,
	senha CHAR(50) NOT NULL
);


INSERT INTO usuario(login, senha) VALUES ('ferman', 'esperanca');
INSERT INTO carteira(usuario_id) VALUES (1);

SELECT
	u.id,
	u.login,
	c.id
FROM carteira c
JOIN usuario u ON c.usuario_id = u.id;

DROP TABLE cotacao_moedas;

INSERT INTO moedas(nome, sigla) VALUES ('Bitcoin', 'BTC');
INSERT INTO cotacao_moedas(moeda_id, valor) VALUES (1, 118.00);

ALTER TABLE cotacao_moedas
MODIFY COLUMN valor DECIMAL(20,2) NOT NULL;

SELECT
	c.id AS 'ID Cotacao',
	m.sigla AS 'Moeda',
	c.valor,
	c.datahora_cotacao
FROM cotacao_moedas c
JOIN moedas m ON c.moeda_id = m.id;

INSERT INTO posicao (carteira_id, status, compra_dolar, moeda_investida, total_compra_moeda_investida)
VALUES (1, 'Aberta', 100, 1, 0.0008);

SELECT
    p.id AS 'ID Posição',
    u.login AS 'Usuário',
    m.nome AS 'Moeda',
    m.sigla AS 'Sigla',
    p.abertura,
    p.status,
    p.compra_dolar,
    p.total_compra_moeda_investida
FROM posicao p
JOIN carteira c ON p.carteira_id = c.id
JOIN usuario u ON c.usuario_id = u.id
JOIN moedas m ON p.moeda_investida = m.id;

ALTER TABLE cotacao_moedas
MODIFY COLUMN valor DECIMAL(10,2) NOT NULL;

ALTER TABLE posicao
MODIFY status ENUM('Aberta', 'Encerrada') DEFAULT 'Aberta';


