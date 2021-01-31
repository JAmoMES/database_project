import sqlite3
from sqlite3 import Error
import os

def unique(colum,split_by):
    set_colum = set()
    for row in colum:
        row = str(row)
        row = row.split(split_by)
        for it in row:
            it = it.strip()
            try :
                 int(it)
                 set_colum.add(it)
            except:     
                set_colum.add(str(it))
    set_colum = sorted(set_colum)
    return set_colum

def merge_list(colum1,colum2):
    merge = []
    for i in range(len(colum1)):
        merge.append((colum1[i],colum2[i]))
    return merge

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = "INSERT INTO tag_new(tagID,tag_name) VALUES (?, ?)"
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

#insert in new row

def insert_table(con,table_name,all_colum, all_value_colum):
    value = '(' + '?, '*len(all_colum)
    value = value[:len(value)-2] + ')'
    all_colum = ','.join(all_colum)
    sql = f"INSERT INTO {table_name}{all_colum}  VALUES {value}"
    cur = con.cursor()
    cur.executemany(sql, all_value_colum)
    con.commit()
    return cur.lastrowid

def update_task(conn, name,all_colum,condition,task):
    all_colum = ','.join(str(i)+'= ? ' for i in all_colum)
    print (all_colum)
    sql = f''' UPDATE {name}
              SET {all_colum}
              WHERE {condition} = ?'''
    print (sql)
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Steam_sql.db")
con = sqlite3.connect(db_path,timeout=10)
cur = con.cursor()
#select info
select = "SELECT tagname FROM tag"
colum_tag = con.execute(select)

'''                  INSERT                         '''
#create in sqlite before insert
'''              INPUT TO INSERT                    '''
# name of table(type : str)
name = 'tagname'
# all colum of name (type : list of str) 
all_colum = 'tag',
# all value in row (type : list of tuple of [str or int])
'''example to make list of tuble of (str or int)'''
# lst1 = [10,20,30]
# lst2 = [50,"Python","JournalDev"]
# lst_tuple = list(zip(lst1,lst2))
# print(lst_tuple)
# output: [(10, 50), (20, 'Python'), (30, 'JournalDev')]

colum_tag = unique(colum_tag,'')
'''            END INPUT TO INSERT                  '''
insert_table(con,name,all_colum,colum_tag)
'''                   END                           '''


'''                  UPDATE                         '''
'''              INPUT TO UPDATE                    '''
# name of table(type : str)
name = 'samples'
# all colum of name (type : tuple of (str or int)) 
all_colum = ('carry',)
# condition to update
condition = 'type'
# set new value and last element is condition
task = (100 ,'def')
'''            END INPUT TO UPDATE                  '''

update_task(con,name,all_colum,condition,task)
'''                   END                           '''


con.close()
