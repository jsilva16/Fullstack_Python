-- Ejercicios
-- Base de Datos a usar
use world;

-- Respuesta 1 - 
select a.name, b.language, b.percentage from countries a join languages b on 
a.code = b.country_code where b.language = "Slovene" order by b.percentage desc;

-- Respuesta 2
select a.name as "País ", count(b.name) as "Ciudades por País" from countries a join cities b on a.code = b.country_code
group by b.country_code order by count(b.name) desc;

-- Respuesta 3
select b.name as "Ciudades de México", b.population as "Población Mayor a 500.000" from countries a join cities b 
on a.code = b.country_code and a.name = "Mexico" and b.population > 500000 order by b.population desc;

-- Respuesta 4
select a.name as "Pais", b.language as "Lenguaje", b.percentage as "Porcentaje Mayor a 89%" from countries a join languages b 
on a.code = b.country_code and b.percentage > 89 order by b.percentage desc;

-- Respuesta 5
select name, surface_area, population from countries where surface_area < 501 and population > 100000;

-- Respuesta 6
select name, government_form, capital, life_expectancy from countries where 
government_form ="Constitutional Monarchy" and capital > 200 and life_expectancy > 75;

-- Respuesta 7
select a.name as "País", b.name as "Ciudad", b.district as "Distrito", b.population as "Población" from countries a join cities b 
on a.code = b.country_code and a.name = "Argentina" and b.population > 500000;

-- Respuesta 8
select region as "Región", count(*) as "Países por Región" from countries group by region order by count(*) desc;













