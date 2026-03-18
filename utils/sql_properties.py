sql_query = """
SELECT
    c.customer_id AS Customer,
    c.age AS Age,
    i.item_name AS Item,
    SUM(o.quantity) AS Quantity
FROM
    Orders o
    INNER JOIN Sales s ON (s.sales_id = o.sales_id)
    INNER JOIN Items i ON (i.item_id = o.item_id)
    INNER JOIN Customer c ON (c.customer_id = s.customer_id)
WHERE
    c.age BETWEEN 18 AND 35
    AND o.quantity IS NOT NULL
GROUP BY
    c.customer_id, c.age, i.item_name
HAVING
    SUM(o.quantity) > 0
ORDER BY
    Customer, Age, Item, Quantity
"""