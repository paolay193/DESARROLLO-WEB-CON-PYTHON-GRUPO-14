from flask import Flask,request,redirect,url_for,render_template
from flask_mysqldb import MySQL

app = Flask(__name__) 

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= "1234"
app.config["MYSQL_DB"]= "historia_clinica"
mysql= MySQL(app)



@app.route('/contenido')
def laboratorio():
    conn = mysql.connection.cursor()
    conn.execute("select cod_lab,cod_cons_lib,exa_lab from Laboratorio")
    labor = conn.fetchall()
    mysql.connection.commit()
    return render_template("f_laboratorio.html", laboratorios=labor)
     







if __name__ == "__main__":
    app.run(debug=True, port=3000)
