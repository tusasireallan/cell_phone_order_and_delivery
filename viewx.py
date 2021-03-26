



2)Code /aquerry /function to manipulate our database to take us to pdt Catelog
6)means of receiving the purchased product and_period (either self_up,couriered,shipped,bicycle,motocyle)
7)Address and_delivery confirmation
9)confirmation of the selected product/ payment(successfully paid for_the product selected)
10)code for_delivery Address and_

QNS
1.Write the query for Registre/Login on the app by the User
2.Write Querry that will help_ the admin / to get end of day report
3.Display the most bought cellphone.
4.write afunction that will help the admin to update/delete/ and_ cancel the products that are nolonger available
5.The company company gives discount every year btn Dec to Jan.
(Write a querry that help mgt to display phone which are available on discount)


FRONT END
1)create form linked into the database
3)front end:-linked to HTML pictures for_phones
4)Search button linking us to a particular pdt
8)payment button linking us fnb or_any bank for_payment
5)After being linked we a functon to make us select / press order / exits











> show_table_query = "DESCRIBE movies"
>>> with connection.cursor() as cursor:
...     cursor.execute(show_table_query)
...     # Fetch rows from last executed query
...     result = cursor.fetchall()
...     for row in result:
...         print(row)



alter_table_query = """
... ALTER TABLE movies
... MODIFY COLUMN collection_in_mil DECIMAL(4,1)
... """
>>> show_table_query = "DESCRIBE movies"
>>> with connection.cursor() as cursor:
...     cursor.execute(alter_table_query)
...     cursor.execute(show_table_query)
...     # Fetch rows from last executed query
...     result = cursor.fetchall()
...     print("Movie Table Schema after alteration:")
...     for row in result:
...         print(row)



select_movies_query = "SELECT * FROM movies LIMIT 5"
>>> with connection.cursor() as cursor:
...     cursor.execute(select_movies_query)
...     result = cursor.fetchall()
...     for row in result:
...         print(row)

SELECT * FROM movies LIMIT 2,5;



select_movies_query = "SELECT title, release_year FROM movies LIMIT 5"
>>> with connection.cursor() as cursor:
...     cursor.execute(select_movies_query)
...     for row in cursor.fetchall():
...         print(row)





update_query = """
UPDATE
    reviewers
SET
    last_name = "Cooper"
WHERE
    first_name = "Amy"
"""
with connection.cursor() as cursor:
    cursor.execute(update_query)
    connection.commit()


UPDATE
    ratings
SET
    rating = 5.0
WHERE
    movie_id = 18 AND reviewer_id = 15;

SELECT *
FROM ratings
WHERE
    movie_id = 18 AND reviewer_id = 15;



    UPDATE
    ratings
SET
    rating = "%s"
WHERE
    movie_id = "%s" AND reviewer_id = "%s";

SELECT *
FROM ratings
WHERE
    movie_id = "%s" AND reviewer_id = "%s"
""" % (
    new_rating,
    movie_id,
    reviewer_id,
    movie_id,
    reviewer_id,
)

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="online_movie_rating",
    ) as connection:
        with connection.cursor() as cursor:
            for result in cursor.execute(update_query, multi=True):
                if result.with_rows:
                    print(result.fetchall())
            connection.commit()
except Error as e:
    print(e)



    >> select_query = """
... SELECT first_name, last_name
... FROM reviewers
... """
>>> with connection.cursor() as cursor:
...     cursor.execute(select_query)
...     for reviewer in cursor.fetchall():
...         print(reviewer)
...





<Ticket>
-Product id (foreign key)
-Quantity
-total
-Date
I´ve modified your Transaction table to have only ticket-customer relationship.

<Transaction>
-customer_id (foreign key)
-ticket id (foreign key)
-Date



Some SQL example

SELECT Tr.customer_id, MONTH(tr.Date), SUM(ti.total)
FROM Transaction tr, Ticket ti
WHERE tr.ticket_id = ti.id
GROUP BY MONTH(tr.Date)
WHERE Tr.customer_id = ? AND tr.Date BETWEEN ? AND



