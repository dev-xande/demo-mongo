from pymongo import MongoClient

def db_handle(db_name, username, password):
    client = MongoClient(
        host="localhost",
        port=27017,
        username=username,
        password=password
    )

    # Outra alternativa para conexão
    # client = MongoClient("mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority")
    # Ou porta host padrão para teste locais
    # client = MongoClient('localhost', 27017)
    # Ou
    # client = MongoClient('mongodb://localhost: 27017/')

    db = client[db_name]

    return db

# class DBHandle:
#     def __init__(self, db_name, username, password) -> None:
#         self.db_name = db_name
#         self.username = username
#         self.password = password

#     def connection(self):
#         client = MongoClient(
#             host="localhost",
#             port=27017,
#             username=self.username,
#             password=self.password
#         )

#         db = client[self.db_name]

#         return db