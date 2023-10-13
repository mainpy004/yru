import sqlite3

con = sqlite3.connect('jokes.bd')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Jokes(
id INTEGER PRIMARY KEY,
joke TEXT
);''')

'''
con.execute('INSERT INTO Jokes(id, joke) VALUES(?,?)', (1, 'Как называется программист, который постоянно делает ошибки? - Глюк-принц.'))
con.execute('INSERT INTO Jokes(id, joke) VALUES(?,?)', (2, 'Почему программисты настолько хороши во время ужина? - У них всегда есть форк.'))
con.execute('INSERT INTO Jokes(id, joke) VALUES(?,?)', (3, 'Какой язык программирования самый быстрый? - Assembly, потому что он не тратит время на говорение, только на выполнение.'))
con.execute('INSERT INTO Jokes(id, joke) VALUES(?,?)', (4, ' Что говорит программист своим детям перед сном? - «sleep(0)».'))
con.execute('INSERT INTO Jokes(id, joke) VALUES(?,?)', (5, 'Зачем программисты одевают очки? - Потому что не хотят C#, только C++.'))
'''

con.commit()