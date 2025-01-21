# %%
pip install mysql.connector

# %%
pip install pymysql

# %%
import pymysql

# Establishing the connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root"
)
print(connection)
# Creating a cursor object
mycursor= connection.cursor()


# %%
pip install tabulate

# %%
mycursor.execute(''' select * from crime.chicago limit 10;
''')
out=mycursor.fetchall()
from tabulate import tabulate
print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

# %%
mycursor.execute('''
    select `Location Description`from crime.chicago 
where year(Date) = 2023 and `Primary Type` = 'THEFT'

''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))


# %%
mycursor.execute('''
    select `District`, count(*) as `Total Crimes` from crime.chicago
group by `District`;
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))


# %%
mycursor.execute('''
    select count(*) as `Total Crimes` FROM crime.chicago
where Date between '2022-01-01' and '2022-12-31';
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))


# %%
mycursor.execute('''
    select `Primary Type`,count(*) as Frequency from crime.chicago group by `Primary Type`
order by Frequency DESC LIMIT 5;
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))


# %%
mycursor.execute('''
    select Beat, District, count(*) as Total_Crimes
from crime.chicago group by Beat, District order by Total_Crimes desc;
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))

# %%
mycursor.execute('''
    select * from crime.chicago where Arrest = TRUE and Domestic = False;
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))

# %%
mycursor.execute('''
    select * from crime.chicago where Block = '027XX N NARRAGANSETT AVE';
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))

# %%
mycursor.execute('''
    select District, count(*) as Total_Crimes from crime.chicago
group by District order by Total_Crimes desc;
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))

# %%

mycursor.execute('''
    select Year, count(*) as Total_Crimes from crime.chicago
group by Year order by Total_Crimes desc;
''')
out = mycursor.fetchall()

from tabulate import tabulate
print(tabulate(out, headers=[i[0] for i in mycursor.description], tablefmt='psql'))


