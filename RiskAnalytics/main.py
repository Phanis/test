from sqlalchemy import create_engine

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('mysql+mysqldb://root:Omonoia123-123-@localhost:3306/riskanalytics')

#some_engine.execute('INSERT INTO users (username, email, password) VALUES ("sdfsd","asdfsdfsd@gmail.com","Omonoia");')

result = some_engine.execute('SELECT * FROM users')
for _r in result:
   print(_r)

