from flask import Flask,request,redirect,url_for,render_template
from flask_mysqldb import MySQL

app = Flask(__name__) 

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= "1234"
app.config["MYSQL_DB"]= "historia_clinica"
mysql= MySQL(app)

@app.route('/')
def inicio():
    primer_usuario()
    return render_template("index.html")

def primer_usuario():
    conn = mysql.connection.cursor()
    conn.execute("select * from usuario where rol_usu={}".format(1))
    user = conn.fetchone()
    if user ==None:
        conn.execute(" insert into usuario values(%s,%s,%s,%s)",(111111,"Paola","4321",1))
    mysql.connection.commit()
      
@app.route("/login", methods=["POST"])
def login():
    if request.method=="POST":
        usuario = request.form["nomUsu"]
        contraseña = request.form["pasUsu"]
        conn = mysql.connection.cursor()
        conn.execute("""select cod_usu,nom_usu,pas_usu,rol_usu from Usuario 
        where nom_usu=%s and pas_usu=%s""",(usuario,contraseña))
        usu = conn.fetchone()
        mysql.connect.commit()
        if usu != None:
            if usu[3]==1:
                return redirect(url_for("administardor"))
            elif usu[3]==2:
                return redirect(url_for("medico"))
            elif usu[3]==3:
                return redirect(url_for("paciente"))
            else:
                return redirect(url_for("inicio"))
        

@app.route("/medico")
def medico():
    conn= mysql.connect.cursor()
    conn.execute("select * from Medico")
    medico = conn.fetchall()
    return render_template("f_medico.html", medicos = medico)

@app.route("/ingrear_medico", methods=["POST"])
def ingresar_medico():
    if request.method=="POST":
        iden_med = request.form["id_med"]
        nombre_med = request.form["name_med"]
        apellido_med = request.form["apel_med"]
        especialidad_med = request.form["esp_med"]
        telefono_med = request.form["tele_med"]
        correo_med = request.form["ema_med"]
        direccion_med = request.form["dir_med"]
        usuario = request.form["nomUsu"]
        contraseña = request.form["pasUsu"]
        conn = mysql.connection.cursor()
        conn.execute("""insert into Medico(id_med,nom_med,ape_med,esp_med,tel_med,cor_med,dir_med)
        values(%s,%s,%s,%s,%s,%s,%s)""",(iden_med,nombre_med,apellido_med,especialidad_med,telefono_med,correo_med,direccion_med))
        mysql.connection.commit()
        conn 
        return redirect(url_for("medico"))




@app.route("/administrador")
def administardor():
    return render_template("administrador.html")

@app.route("/laboratorio")
def laboratorio():
    return render_template("f_laboratorio.html")

@app.route("/consulta")
def consulta():
    return render_template("f_consulta.html")

@app.route("/remision")
def remision():
    return render_template("f_Remision.html")

@app.route("/paciente")
def paciente():
    return render_template("f_paciente.html")

 
    
  






if __name__ == "__main__":
   app.run(debug=True, port=3000)
