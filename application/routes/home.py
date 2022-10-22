from flask import render_template
from utils.connect_bd import get_db_connection
from manage import app

from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from  datetime import date
from typing import Optional

import psycopg2



@app.route("/")
def index():
    month = ['janeiro', 'fevereiro','março', 'abril', 'maio', 'junho','julho','agosto','setembro','outubro','novembro','dezembro']
    conn = get_db_connection()
    cursor = conn.cursor()  
    
    sql = "select \
        name, \
        extract(day from birth) as dia, \
        extract (MONTH from birth) as mes, \
        extract (day from now()) as hoje \
        from intranet.user \
        where extract (MONTH from birth) = extract (MONTH from now()) \
        order by dia asc"
        
    cursor.execute(sql)
    birth_user = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    
    return render_template('index.html', birth_user=birth_user, month=month)