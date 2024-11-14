
SELECT A.aluguel_id, C.nome AS cliente, F.titulo AS filme, S.titulo AS serie, A.data_aluguel, A.data_devolucao
FROM Aluguel A
LEFT JOIN Cliente C ON A.cliente_id = C.cliente_id
LEFT JOIN Filme F ON A.filme_id = F.filme_id
LEFT JOIN Serie S ON A.serie_id = S.serie_id
WHERE A.status = 'ativo';

SELECT F.titulo AS filme, COUNT(A.aluguel_id) AS total_alugado
FROM Aluguel A
JOIN Filme F ON A.filme_id = F.filme_id
GROUP BY F.titulo
ORDER BY total_alugado DESC;


SELECT S.titulo AS serie, COUNT(A.aluguel_id) AS total_alugado
FROM Aluguel A
JOIN Serie S ON A.serie_id = S.serie_id
GROUP BY S.titulo
ORDER BY total_alugado DESC;


SELECT A.aluguel_id, F.titulo AS filme, S.titulo AS serie, A.data_aluguel, A.data_devolucao, A.status
FROM Aluguel A
LEFT JOIN Filme F ON A.filme_id = F.filme_id
LEFT JOIN Serie S ON A.serie_id = S.serie_id
WHERE A.cliente_id = 1;

SELECT DISTINCT C.cliente_id, C.nome, C.email
FROM Aluguel A
JOIN Cliente C ON A.cliente_id = C.cliente_id
WHERE A.status = 'expirado';

SELECT 
    SUM(F.preco_aluguel) AS receita_filmes, 
    SUM(S.preco_aluguel) AS receita_series,
    (SUM(F.preco_aluguel) + SUM(S.preco_aluguel)) AS receita_total
FROM Aluguel A
LEFT JOIN Filme F ON A.filme_id = F.filme_id
LEFT JOIN Serie S ON A.serie_id = S.serie_id;

SELECT 'Filme' AS tipo, F.titulo AS titulo, G.descricao AS genero
FROM Filme F
JOIN Genero G ON F.genero_id = G.genero_id
UNION
SELECT 'Serie' AS tipo, S.titulo AS titulo, G.descricao AS genero
FROM Serie S
JOIN Genero G ON S.genero_id = G.genero_id;


SELECT C.nome AS cliente, COUNT(A.aluguel_id) AS total_alugueis
FROM Cliente C
LEFT JOIN Aluguel A ON C.cliente_id = A.cliente_id
GROUP BY C.nome
ORDER BY total_alugueis DESC;

SELECT A.aluguel_id, C.nome AS cliente, F.titulo AS filme, S.titulo AS serie, A.data_aluguel
FROM Aluguel A
LEFT JOIN Cliente C ON A.cliente_id = C.cliente_id
LEFT JOIN Filme F ON A.filme_id = F.filme_id
LEFT JOIN Serie S ON A.serie_id = S.serie_id
WHERE A.data_aluguel = '2024-11-12';

SELECT G.descricao AS genero, 
       COUNT(F.filme_id) AS total_filmes_alugados, 
       COUNT(S.serie_id) AS total_series_alugadas
FROM Genero G
LEFT JOIN Filme F ON G.genero_id = F.genero_id
LEFT JOIN Aluguel AF ON F.filme_id = AF.filme_id
LEFT JOIN Serie S ON G.genero_id = S.genero_id
LEFT JOIN Aluguel ASR ON S.serie_id = ASR.serie_id
GROUP BY G.descricao;
