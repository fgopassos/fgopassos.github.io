from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("db_web.db")
    # Permite recuperar retorno de fetchall como dicionário
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM utilizadores")
    dado=cur.fetchall()
    return render_template("index.html", dados=dado)

@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        nome=request.form['uname']
        email=request.form['contact']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("INSERT INTO utilizadores(Nome,Email) VALUES (?,?)", (nome, email))
        con.commit()
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<int:uid>",methods=['POST','GET'])
def edit_user(uid):
    if request.method=='POST':
        nome=request.form['uname']
        email=request.form['contact']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("UPDATE utilizadores SET Nome=?,Email=? WHERE Id=?",(nome, email, uid))
        con.commit()
        return redirect(url_for("index"))
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM utilizadores WHERE Id=?",(uid,))
    dado=cur.fetchone()
    return render_template("edit_user.html",datas=dado)
    
@app.route("/delete_user/<int:uid>",methods=['GET'])
def delete_user(uid):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("DELETE FROM utilizadores WHERE Id=?",(uid,))
    con.commit()
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.secret_key='#admin123!'
    app.run(debug=True)