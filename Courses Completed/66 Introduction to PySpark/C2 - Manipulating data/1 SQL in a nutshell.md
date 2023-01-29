# SQL in a nutshell 

As you move forward, it will help to have a basic understanding of SQL. A more in depth look can be found [here](https://www.datacamp.com/courses/intro-to-sql-for-data-science).

A SQL query returns a table derived from one or more tables contained in a database.

Every SQL query is made up of commands that tell the database what you want to do with the data. The two commands that every query has to contain are SELECT and FROM.

The SELECT command is followed by the columns you want in the resulting table.

The FROM command is followed by the name of the table that contains those columns. The minimal SQL query is:

SELECT * FROM my_table;
The * selects all columns, so this returns the entire table named my_table.

Similar to .withColumn(), you can do column-wise computations within a SELECT statement. For example,

SELECT origin, dest, air_time / 60 FROM flights;
returns a table with the origin, destination, and duration in hours for each flight.

Another commonly used command is WHERE. This command filters the rows of the table based on some logical condition you specify. The resulting table contains the rows where your condition is true. For example, if you had a table of students and grades you could do:

SELECT * FROM students
WHERE grade = 'A';
to select all the columns and the rows containing information about students who got As.

