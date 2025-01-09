class User:
    def __init__(self, db):
        self.db = db

    def add_user(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self.db.execute_query(query, (username, password))

    def authenticate_user(self, username, password):
        query = "SELECT * FROM users WHERE username=? AND password=?"
        result = self.db.fetchall(query, (username, password))
        return result
