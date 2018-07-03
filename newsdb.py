#!/usr/bin/env python3
import psycopg2


# 3 most popular articles
query_1_desc = ("Three most popular articles:")
query_1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

# Most popular authors
query_2_desc = ("Most popular authors:")
query_2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

# Days with more than 1% errors
query_3_desc = ("Days where more than one percent of requests led to errors.")
query_3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def connect(database_name="news"):
    """Connect to the database."""

    db = psycopg2.connect("dbname={}".format(database_name))
    cursor = db.cursor()
    return db, cursor


def get_query_results(query):
    """Return query results """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_query_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print "\t", index+1, "-", results[0], "\t-", str(results[1]), "views"


def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print "\t", results[0], "-", str(results[1]) + "% errors"


if __name__ == '__main__':
    # store query results
    popular_articles_results = get_query_results(query_1), query_1_desc
    popular_authors_results = get_query_results(query_2), query_2_desc
    error_days = get_query_results(query_3), query_3_desc

    # print query results
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(error_days)
