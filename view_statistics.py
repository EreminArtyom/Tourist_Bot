import matplotlib.pyplot as plt
import sqlite3
from MyDataBase.ChangeData import count_ariph_mean_rating
connection = sqlite3.connect("C:\\Users\\Artem\\PyCharm\\MyDataBase\\TouristBotStatistics_new.db")
cursor = connection.cursor()
cursor.execute('SELECT * FROM visit')
Visiting = cursor.fetchall()
cursor.execute('SELECT * FROM rating')
Rating = cursor.fetchall()
def last_elem(p):
    return p[len(p)-1]
Visiting.sort(key=last_elem, reverse=True)
TopVisitCount = []
AntyTopVisitCount = []
TopVisitName = []
AntyTopVisitName = []
RatingRating = [1, 2, 3, 4, 5]
RatingNumber = []
s =''
n = ''
path = plt.bar([0], [0])
for j in range(5):
    AntyTopVisitCount.append(Visiting[len(Visiting)-5+j][2])
    AntyTopVisitName.append(Visiting[len(Visiting)-5+j][0])
    n = n + '\n' + Visiting[len(Visiting) - 5 + j][0] + ' - ' + str(Visiting[len(Visiting) - 5 + j][2])
    RatingNumber.append(Rating[j][1])
for i in range(5):
    TopVisitCount.append(Visiting[i][2])
    TopVisitName.append(Visiting[i][0])
    s = s + '\n' + str(i+1) + ' ' + Visiting[i][0] + ' - ' + str(Visiting[i][2])
def ShowTopVisiting():
    global path
    path.remove()
    path = plt.bar([1, 2, 3, 4, 5], TopVisitCount, label=s)
    plt.legend(fontsize=6, loc='upper right')
    plt.savefig('visit_diagram.png')
def  ShowAntyTopVisiting():
    global path
    path.remove()
    path = plt.bar([1, 2, 3, 4, 5], AntyTopVisitCount, label=n)
    plt.legend(loc='upper right', fontsize=6)
    plt.savefig('visit_diagram.png')
def ShowRating():
    global path
    path.remove()
    path = plt.bar(RatingRating, RatingNumber, label=f'Средний рэйтиг {count_ariph_mean_rating()}')
    plt.legend()
    plt.savefig('visit_diagram.png')
