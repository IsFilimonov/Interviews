/*
 * Что хотелось бы пояснить:
 * - Конструкция WITH cte (col1, col2,..,n) AS: принудительно именует столбцы в cte.
 * Сохраняется верхнеуровневая последовательность имен столбцов. Не самая удачная практика.
 * - "," в разделе cte FROM эквивалентно CROSS JOIN
 * 	  FROM employees e, employee_levels el 
 * -  FROM codewars.employees e, employee_levels e1
 *    WHERE e.manager_id = e1.id 
 * можно заменить на 
 * 		FROM codewars.employees t2 JOIN employee_levels t3
 * 		ON t2.manager_id = t3.id
 * */
DROP TABLE IF EXISTS CODEWARS.employees;
CREATE TABLE IF NOT EXISTS CODEWARS.employees
(
    id	int,
    first_name	varchar(300),
    last_name	varchar(300),
    manager_id	int
);


INSERT INTO CODEWARS.employees (id,first_name,last_name,manager_id)
VALUES
    (1, 'Berry', 'Abernathy', Null),
    (2, 'Archie', 'McCullough', 1),
    (3, 'Wilmer', 'Anderson', 2),
    (4, 'William', 'Turner', 1),
    (5, 'Miguelina', 'Lowe', 2),
    (6, 'Juliet', 'Murphy', 3),
    (7, 'Thanh', 'Runolfsdottir', 3),
    (8, 'Gabriel', 'Wilkinson', 4),
    (9, 'Curtis', 'Quigley', 8),
    (10, 'Kia', 'Koch', 6),
    (11, 'Leah', 'Lowe', 2),
    (12, 'Elissa', 'Muller', 3),
    (13, 'Robbie', 'Pfeffer', 3),
    (14, 'George', 'Stanton', 2),
    (15, 'Santiago', 'Walker', 7),
    (16, 'Stacy', 'Boyle', 1),
    (17, 'Willene', 'Padberg', 2),
    (18, 'Isela', 'Bailey', 14),
    (19, 'Georgette', 'Botsford', 8),
    (20, 'Melodee', 'Bailey', 5),
    (21, 'Siobhan', 'Schroeder', 12),
    (22, 'April', 'Kulas', 20),
    (23, 'Flor', 'Berge', 21),
    (24, 'Kirk', 'Howell', 8),
    (25, 'Normand', 'Hand', 16),
    (26, 'Luciano', 'Koelpin', 17),
    (27, 'Bernardo', 'Schimmel', 12),
    (28, 'Allen', 'Bernhard', 17),
    (29, 'Levi', 'Hills', 17),
    (30, 'Victoria', 'Conroy', 23),
    (31, 'Tillie', 'Botsford', 26),
    (32, 'Donita', 'Stroman', 3),
    (33, 'Jerome', 'Hilpert', 21),
    (34, 'Dee', 'Lemke', 21),
    (35, 'Marshall', 'Fadel', 18),
    (36, 'Jewel', 'Kilback', 8),
    (37, 'Sammy', 'Roberts', 19),
    (38, 'Richie', 'Jaskolski', 2),
    (39, 'Lachelle', 'Ullrich', 27),
    (40, 'Wilfredo', 'Zieme', 20),
    (41, 'Gavin', 'Krajcik', 26),
    (42, 'Rena', 'Jacobi', 20),
    (43, 'Rufus', 'Dicki', 25),
    (44, 'Trang', 'Renner', 33),
    (45, 'Oscar', 'McDermott', 31),
    (46, 'Simone', 'Breitenberg', 30),
    (47, 'Hee', 'Ondricka', 33),
    (48, 'Connie', 'Schulist', 41),
    (49, 'Malissa', 'Marks', 23),
    (50, 'Harriett', 'Keebler', 32),
    (51, 'Selene', 'Walker', 42),
    (52, 'Lino', 'Kuphal', 49),
    (53, 'Chandra', 'Erdman', 23),
    (54, 'Tamara', 'Stracke', 2),
    (55, 'Leigh', 'Grady', 5),
    (56, 'Lionel', 'Brakus', 33),
    (57, 'Iola', 'Kihn', 53),
    (58, 'Fernando', 'Cronin', 45),
    (59, 'Sook', 'Maggio', 12),
    (60, 'Earle', 'Ward', 36),
    (61, 'Saturnina', 'Wyman', 22),
    (62, 'Kali', 'Powlowski', 61),
    (63, 'Chester', 'Leuschke', 17),
    (64, 'Mohamed', 'Hahn', 28),
    (65, 'Corey', 'Walter', 58),
    (66, 'Juliette', 'Krajcik', 11),
    (67, 'Sam', 'Ferry', 55),
    (68, 'Rick', 'Gislason', 60),
    (69, 'Santos', 'Oberbrunner', 11),
    (70, 'Jamison', 'Aufderhar', 67),
    (71, 'Mimi', 'VonRueden', 2),
    (72, 'Victoria', 'O Connell', 45),
    (73, 'Austin', 'Rowe', 64),
    (74, 'Rory', 'Johns', 64),
    (75, 'Kenny', 'Schinner', 28),
    (76, 'Steve', 'Stracke', 68),
    (77, 'Leonel', 'Kohler', 55),
    (78, 'Chang', 'Kirlin', 51),
    (79, 'Irina', 'Collins', 20),
    (80, 'Ines', 'Spinka', 44),
    (81, 'Gracia', 'Paucek', 63),
    (82, 'Sharlene', 'Larson', 9),
    (83, 'Raymon', 'Ernser', 19),
    (84, 'Burl', 'Bergnaum', 26),
    (85, 'Edison', 'Beier', 46),
    (86, 'Dyan', 'Gibson', 70),
    (87, 'Gilberto', 'Ernser', 36),
    (88, 'Chantal', 'Will', 46),
    (89, 'Ivory', 'Hilll', 37),
    (90, 'Tyrone', 'Stark', 36),
    (91, 'Shannon', 'Morissette', 20),
    (92, 'Marlyn', 'Greenholt', 15),
    (93, 'Cyrus', 'Rath', 28),
    (94, 'Flora', 'Langosh', 90),
    (95, 'Bradley', 'Hackett', 67),
    (96, 'Phylis', 'Witting', 88),
    (97, 'Elvie', 'Flatley', 41),
    (98, 'Mariano', 'Rutherford', 20),
    (99, 'Rosendo', 'Witting', 50),
    (100, 'Cristin', 'Walter', 72);


WITH RECURSIVE employee_levels (
    level,
    id,
    first_name,
    last_name,
    manager_id
) AS (
    SELECT
        1 AS level,
        t1.id,
        t1.first_name,
        t1.last_name,
        t1.manager_id
    FROM
        employees t1
    WHERE
        manager_id IS NULL
  
    UNION ALL
  
    SELECT
        t3.level +1,
        t2.id,
        t2.first_name,
        t2.last_name,
        t2.manager_id
    FROM
        employees t2
        JOIN employee_levels t3 ON t2.manager_id = t3.id
)
SELECT
    level,
    id,
    first_name,
    last_name,
    manager_id
FROM
    employee_levels;

