#!/usr/bin/python3
import psycopg2


def part1():
    # This function display most popular three articles of all time

    # Connect to new database
    conn = psycopg2.connect("dbname=postgres user=postgres password=123456789")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute("""SELECT articles.title, COUNT(log.path) as count
                FROM articles,log WHERE REPLACE(path,'/article/','') = articles.slug
                GROUP by articles.title ORDER by count Desc LIMIT 3;""")
    # values are printed
    x = cur.fetchall()
    for item in range(len(x)):
        print("{} - {}".format(x[item][0],x[item][1]))
    # Close communication with the database
    cur.close()
    conn.close()


def part2():
    # This function display the most popular article authors of all time
    # Connect to new database
    conn = psycopg2.connect("dbname=postgres user=postgres password=123456789")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute("""SELECT authors.name, COUNT(articles.author)
                FROM log, articles, authors
                WHERE REPLACE(log.path, '/article/', '') = articles.slug
                AND articles.author = authors.id
                GROUP by authors.name ORDER BY count Desc;""")
    # values are printed
    y = cur.fetchall()
    for item in range(len(y)):
        print("{} - {}".format(y[item][0],y[item][1]))
    # Close communication with the database
    cur.close()
    conn.close()


def part3():
    # This function display the more than 1% of requests lead to errors
    # Connect to new database
    conn = psycopg2.connect("dbname=postgres user=postgres password=123456789")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute("""SELECT to_char(log.time::date, 'DD-MM-YYYY'),
           (new.total*100)/(COUNT(log.time::date)) as percen
           FROM (SELECT time::date, COUNT(time::date) as total
           FROM log WHERE  status != '200 OK'
           GROUP BY time::date ORDER BY total DESC) as new,
           log WHERE new.time::date = log.time::date
           GROUP BY to_char(log.time::date, 'DD-MM-YYYY'),
           new.total ORDER BY percen DESC;""")
    # values are printed
    z = cur.fetchall()
    print("On {} requests lead to {}% errors.".format(z[:1][0][0],z[:1][0][1]))
    # Close communication with the database
    cur.close()
    conn.close()


print("1.\n")
part1()
print("\n2.\n")
part2()
print("\n3.\n")
part3()
