from flask import Flask,request,redirect,url_for,render_template
from flask_mysqldb import MySQL

app = Flask(__name__) 

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= "1234"
app.config["MYSQL_DB"]= "historia_clinica"
mysql= MySQL(app)


@app.route("/paciente")
def paciente():
    conn= mysql.connect.cursor()
    conn.execute("select * from Paciente")
    paciente = conn.fetchall()
    return render_template("f_paciente.html", pacientes = paciente)

@app.route("/ingresar_paciente", methods=["POST"])
def ingresar_paciente():
    if request.method=="POST":
        iden_pac = request.form["idPac"]
        nombre_pac = request.form["namPac"]
        apellido_pac = request.form["apellido"]
        tel_pac = request.form["telefono"]
        correo_pac = request.form["email"]
        direccion_pac = request.form["direccion"]
        rh_pac = request.form["grupoRh"]
        eps_pac = request.form["eps"]
        fam_pac = request.form["famlPac"]
        par_pac = request.form["parentesco"]
        id_med_pac = request.form["id_med_pac"]
        conn = mysql.connection.cursor()
        conn.execute("""insert into Medico(id_pac,nom_pac,ape_pac,tel_pac,cor_pac,dir_pac,rh_pac,eps_pac,fam_pac,par_pac,id_med_pac)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,(iden_pac,nombre_pac,apellido_pac,tel_pac,correo_pac,direccion_pac,rh_pac,eps_pac,fam_pac,par_pac,id_med_pac))
        mysql.connection.commit()
        return redirect(url_for("inicio"))