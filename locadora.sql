CREATE DATABASE CineMengo;
USE CineMengo;
CREATE TABLE Genero (
    genero_id INT AUTO_INCREMENT PRIMARY KEY,      
    descricao VARCHAR(30) NOT NULL                 
);

CREATE TABLE Cliente (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,     
    nome VARCHAR(50) NOT NULL,                     
    endereco VARCHAR(100),                         
    email VARCHAR(50) UNIQUE NOT NULL,             
    forma_pagamento VARCHAR(20)                    
);

CREATE TABLE Filme (
    filme_id INT AUTO_INCREMENT PRIMARY KEY,       
    titulo VARCHAR(100) NOT NULL,               
    ano_lancamento INT,                          
    duracao INT,                                   
    preco_aluguel DECIMAL(5, 2) NOT NULL,          
    genero_id INT,                                 
    FOREIGN KEY (genero_id) REFERENCES Genero(genero_id)   
);


CREATE TABLE Serie (
    serie_id INT AUTO_INCREMENT PRIMARY KEY,      
    titulo VARCHAR(100) NOT NULL,                 
    ano_lancamento INT,                            
    duracao INT,                                   
    preco_aluguel DECIMAL(5, 2) NOT NULL,          
    genero_id INT,                                
    temporadas INT,                               
    FOREIGN KEY (genero_id) REFERENCES Genero(genero_id)   
);


CREATE TABLE Aluguel (
    aluguel_id INT AUTO_INCREMENT PRIMARY KEY,     
    cliente_id INT NOT NULL,                      
    filme_id INT,                                
    serie_id INT,                                  
    data_aluguel DATE NOT NULL,                   
    data_devolucao DATE,                           
    status VARCHAR(15) DEFAULT 'ativo',         
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),  
    FOREIGN KEY (filme_id) REFERENCES Filme(filme_id),         
    FOREIGN KEY (serie_id) REFERENCES Serie(serie_id)          
);
