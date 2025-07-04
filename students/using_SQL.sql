SELECT * FROM students LIMIT 5;

SELECT AVG(score) AS "average score" FROM students;

SELECT * FROM students WHERE score = ( SELECT MAX(score) FROM students);

SELECT major, COUNT(*) AS students
    FROM students
    GROUP BY major
    ORDER BY students DESC;

SELECT * FROM students WHERE score >= 3.5;

SELECT major, AVG(score) FROM students GROUP BY major;