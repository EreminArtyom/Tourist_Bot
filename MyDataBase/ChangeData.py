import sqlite3
connection = sqlite3.connect("C:\\Users\\Artem\\PyCharm\\MyDataBase\\TouristBotStatistics_new.db")
cursor = connection.cursor()
def CityCode(s):
    flag = True
    if s == 'klgd':
        return('Калининград ')
        flag = False
    if s == 'zel':
        return('Зеленоградск')
        flag = False
    if s == 'sve':
        return('Светлогорск ')
        flag = False
    if s == 'yant':
        return('Янтарный    ')
        flag = False
    if s == 'pol':
        return('Полесск     ')
        flag = False
    if s == 'cher':
        return('Черняховск  ')
        flag = False
    if flag:
        return('0')

def AntyCityCode(s):
    s = s.replace(" ", "")
    s = s.lower()
    if s == 'калининград':
        return 'klgd'
    if s == 'зеленоградск':
        return 'zel'
    if s == 'светлогорск':
        return 'sve'
    if s == 'янтарный':
        return 'yant'
    if s == 'полесск':
        return 'pol'
    if s == 'черняховск':
        return 'cher'
connection = sqlite3.connect('C:\\Users\\Artem\\PyCharm\\MyDataBase\\TouristBotStatistics_new.db')
cursor = connection.cursor()
def add_visit(s):
    cursor.execute('SELECT count FROM visit WHERE location = ?', (s, ))
    k = cursor.fetchone()
    cursor.execute('UPDATE visit SET count = ? WHERE location = ?', (int(k[0])+1, s))
    connection.commit()
def add_rating(i):
    cursor.execute('SELECT number FROM rating WHERE rtng = ?', (i, ))
    k = cursor.fetchone()
    cursor.execute('UPDATE rating SET number = ? WHERE rtng = ?', (k[0]+1, i))
    connection.commit()
def change_name(id, new):
    cursor.execute('SELECT Name FROM places WHERE id = ?', (id, ))
    name = cursor.fetchone()
    name = name[0]
    cursor.execute('SELECT City FROM places WHERE id = ?', (id, ))
    city = cursor.fetchone()
    city = city[0]
    cursor.execute('UPDATE places SET Name = ? WHERE id = ?', (new, id))
    connection.commit()
    cursor.execute('SELECT * FROM visit')
    res = cursor.fetchall()
    for r in res:
        s = r[0]
        if s[0: len(s)-13] == name and r[1] == city:
            snew = s.replace(name, new)
            cursor.execute('UPDATE visit SET location = ? WHERE location = ?', (snew, s))
            connection.commit()
def change_city(id, new):
    cursor.execute('SELECT Name FROM places WHERE id = ?', (id, ))
    name = cursor.fetchone()
    name = name[0]
    cursor.execute('SELECT City FROM places WHERE id = ?', (id, ))
    city = cursor.fetchone()
    city = city[0]
    cursor.execute('UPDATE places SET City = ? WHERE id = ?', (new, id))
    connection.commit()
    cursor.execute('SELECT * FROM visit')
    res = cursor.fetchall()
    for r in res:
        s = r[0]
        if s[0: len(s)-13] == name and r[1] == city:
            if CityCode(new) != '0':
                snew = s.replace(CityCode(city), CityCode(new))
                cursor.execute('UPDATE visit SET location = ? WHERE location = ?', (snew, s))
                connection.commit()
                cursor.execute('UPDATE visit SET city = ? WHERE location = ?', (new, snew))
                connection.commit()

def change_address(id, new):
    cursor.execute('UPDATE places SET Address = ? WHERE id = ?', (new, id))
    connection.commit()
    change_city(id, AntyCityCode(new[0: new.find(',')]))
def change_desc(id, new):
    cursor.execute('UPDATE places SET desc = ? WHERE id = ?', (new, id))
    connection.commit()
def change_link(id, new):
    cursor.execute('UPDATE places SET link = ? WHERE id = ?', (new, id))
    connection.commit()
def change_sale(id, new):
    cursor.execute('UPDATE places SET sale = ? WHERE id = ?', (new, id))
    connection.commit()
def change_type(id, new):
    cursor.execute('UPDATE places SET type = ? WHERE id = ?', (new, id))
    connection.commit()
def count_ariph_mean_rating():
    k = 0
    i = 0
    cursor.execute('SELECT * FROM rating')
    rat = cursor.fetchall()
    for m in rat:
        i += int(m[1])
        k += int(m[1])*int(m[0])
    if i > 0:
        return ((k*10)//i)/10
    else:
        return 0
