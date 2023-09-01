import sqlite3

Connection = sqlite3.connect('lib/dogs.db')
CURSOR = Connection.cursor()

class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(self):
        sql = """ 
            CREATE TABLE IF NOT EXISTS dogs(
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(self):
        sql = """
            DROP TABLE IF EXISTS dogs
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (? , ?)
        """
        CURSOR.execute(sql, (self.name, self.breed))
    
    @classmethod
    def create (cls, name, breed):
        dog = Dog(name, breed)
        dog.save()
        return dog




    @classmethod
    def select_all(cls):
        sql = """
            SELECT * FROM dogs
        """
        CURSOR.execute(sql)
        data = CURSOR.fetchall()
        return data
    

Dog.create("Tess", "Maltese")

# dog1 = Dog("Tess", "Maltese")
# dog1.save()
# dog2 = Dog ("Bulldog", "Bulldog")
# dog2.save()

all_dogs = Dog.select_all()
for dog in all_dogs:
    print (dog)