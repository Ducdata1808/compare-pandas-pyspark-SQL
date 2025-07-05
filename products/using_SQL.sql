SELECT quantity * price AS total FROM orders;

SELECT SUM(quantity * price) FROM orders;

SELECT order_date, COUNT(*) AS "number of orders" FROM orders GROUP BY order_date ORDER BY order_date;

SELECT order_date, SUM(quantity * price) FROM orders GROUP BY order_date ORDER BY order_date;

SELECT order_date, SUM(quantity * price) AS total
       FROM orders
       GROUP BY order_date
       ORDER BY total DESC
       LIMIT 1;

SELECT order_date, SUM(quantity * price) AS total
     FROM orders
     GROUP BY order_date
     HAVING total = (
      SELECT MAX(total_sum)
      FROM (
              SELECT SUM(quantity * price) as total_sum
              FROM orders
              GROUP BY order_date
              ) AS sub
     );

SELECT product, SUM(quantity) FROM orders GROUP BY product;