-- Query: Create 3 new dojos
INSERT INTO dojos_and_ninjas_schema.dojos (name)
VALUES('Burbank,CA'),('Glendale,CA'),('Pasadena,CA')

-- Query: Delete the 3 dojos you just created
-- DELETE FROM table_name WHERE condition(s)

DELETE FROM dojos_and_ninjas_schema.dojos WHERE id=1;
DELETE FROM dojos_and_ninjas_schema.dojos WHERE id=2;
DELETE FROM dojos_and_ninjas_schema.dojos WHERE id=3;
-- Query: Create 3 more dojos

INSERT INTO dojos_and_ninjas_schema.dojos (name)
VALUES('Burbank,CA'),('Glendale,CA'),('Pasadena,CA')


-- Query: Create 3 ninjas that belong to the first dojo
-- INSERT INTO table_name (column_name1, column_name2) 
-- VALUES('column1_value', 'column2_value');

INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Armen', 'Garayan', 27, 19), ('Maral', 'Kurdian', 24, 18), ('Arky', 'Boy', 1, 17);

-- Query: Create 3 ninjas that belong to the second dojo

INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES('Elvis', 'Jones' 23, 5), ('Alex', 'Dabby' 14, 5). ('Hoso', 'Bobby' 1, 5)

-- Query: Create 3 ninjas that belong to the third dojo

INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES('Luke', 'Hall' 10, 56), ('Duke', 'Diibsy' 13, 3). ('Kara', 'lee' 53, 9)

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM dojos_and_ninjas_schema.dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id

-- Query: Retrieve the last ninja's dojo
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT); 
