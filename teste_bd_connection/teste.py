import mysql.connector
import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input('Mysql user: '),
        password=getpass.getpass('Mysql password: '),
        database="Teste"
    ) as connection:
        show_table_query = """DESCRIBE Movies"""
        alter_table_movies_collection = """
            ALTER TABLE Movies MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """
        with connection.cursor() as cursor:
            cursor.execute(alter_table_movies_collection)
            cursor.execute(show_table_query)
            print('\nShowing the Movies Table rows:\n')
            result = cursor.fetchall()
            for row in result:
                print(row)
        

except OSError as e:
    print(e)








# create_db_query = "CREATE DATABASE Teste"
        # show_db_query = "SHOW DATABASES"
        # with connection.cursor() as cursor:
        #     cursor.execute(show_db_query)
        #     for db in cursor:
        #         print(db)

        #Criando a tabela movies:
        # create_table_movies_query = """
        #     CREATE TABLE Movies(
        #         id INT AUTO_INCREMENT PRIMARY KEY,
        #         title VARCHAR(100),
        #         release_year YEAR(4),
        #         genre VARCHAR(100),
        #         collection_in_mil INT
        #     )
        # """
        # with connection.cursor() as cursor:
        #     cursor.execute(create_table_movies_query)
        #     connection.commit()

        #Criando a tabela reviewers:
        # create_reviewers_table_query = """
        #     CREATE TABLE Reviewers(
        #         id INT AUTO_INCREMENT PRIMARY KEY,
        #         first_name VARCHAR(100),
        #         last_name VARCHAR(100)
        #     )
        # """
        # with connection.cursor() as cursor:
        #     cursor.execute(create_reviewers_table_query)
        #     connection.commit()

        #Criando a tabela ratings:
        # create_ratings_table_query = """
        #     CREATE TABLE Ratings(
        #         movie_id INT NOT NULL,
        #         reviewer_id INT NOT NULL,
        #         rating DECIMAL(2,1),
        #         FOREIGN KEY(movie_id) REFERENCES Movies(id),
        #         FOREIGN KEY(reviewer_id) REFERENCES Reviewers(id),
        #         PRIMARY KEY(movie_id, reviewer_id)
        #     )
        # """
        # with connection.cursor() as cursor:
        #     cursor.execute(create_ratings_table_query)
        #     connection.commit()