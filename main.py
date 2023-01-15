from PyQt5 import uic, QtWidgets
import random
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

banco = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="localdb"
)
cursor = banco.cursor()

list = ["papel", "tesoura", "pedra"]
cpu = random.randint(0, 2)
print(cpu)

def funcao_p():
    if formulario.radioPapel.isChecked():
        if(cpu == 0):
            print(
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate")
            formulario.label.setText(
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate")
            QMessageBox.about(formulario, "alerta", (
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(1,1)"
            cursor.execute(comando_SQL)
            formulario.close()
        elif(cpu == 1):
            print(f"O adversário Ganhou, escolheu {list[cpu]} !!")
            formulario.label.setText(
                f"O adversário Ganhou, escolheu {list[cpu]} !!")
            QMessageBox.about(formulario, "alerta", (
                f"O adversário Ganhou, escolheu {list[cpu]} !!"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(0,1)"
            cursor.execute(comando_SQL)
            formulario.close()
        elif(cpu == 2):
            print(f"Você Ganhou, e a máquina escolheu {list[cpu]} !!")
            formulario.label.setText(
                f"Você Ganhou, e a máquina escolheu {list[cpu]} !!")
            QMessageBox.about(formulario, "alerta", (
                f"Você Ganhou, e a máquina escolheu {list[cpu]} !!"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(1,0)"
            cursor.execute(comando_SQL)
            formulario.close()
    if formulario.radioTesoura.isChecked():
        if(cpu == 0):
            print(f"Você Ganhou, e a máquina escolheu {list[cpu]} !!")
            formulario.label.setText(
                f"Você Ganhou, e a máquina escolheu {list[cpu]} !!")
            QMessageBox.about(formulario, "alert", (
                f"Você Ganhou, e a máquina escolheu {list[cpu]} !!"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(1,0)"
            cursor.execute(comando_SQL)
            formulario.close()
        elif(cpu == 1):
            print(
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate")
            formulario.label.setText(
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate")
            QMessageBox.about(formulario, "alert", (
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(1,1)"
            cursor.execute(comando_SQL)
            formulario.close()
        elif(cpu == 2):
            print(f"O adversário Ganhou, escolheu {list[cpu]} !!")
            formulario.label.setText(
                f"O adversário Ganhou, escolheu {list[cpu]} !!")
            QMessageBox.about(formulario, "alert", (
                f"O adversário Ganhou, escolheu {list[cpu]} !!"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(0,1)"
            cursor.execute(comando_SQL)
            formulario.close()
    if formulario.radioPedra.isChecked():
        if(cpu == 0):
            print(f"O adversário Ganhou, escolheu {list[cpu]} !!")
            formulario.label.setText(
                f"O adversário Ganhou, escolheu {list[cpu]} !!")
            QMessageBox.about(formulario, "alert", (
                f"O adversário Ganhou, escolheu {list[cpu]} !!"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(0,1)"
            cursor.execute(comando_SQL)
            formulario.close()
        elif(cpu == 1):
            print(f"Você Ganhou, e a máquina escolheu {list[cpu]} !!")
            formulario.label.setText(
                f"Você Ganhou, e a máquina escolheu {list[cpu]} !!")
            QMessageBox.about(formulario, "alert", (
                f"Você Ganhou, e a máquina escolheu {list[cpu]} !!"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(1,0)"
            cursor.execute(comando_SQL)
            formulario.close()
        elif(cpu == 2):
            print(
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate")
            formulario.label.setText(
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate")
            QMessageBox.about(formulario, "alert", (
                f"O adversário escolheu a mesma {list[cpu]} escolha, Deu empate"))
            comando_SQL = "INSERT INTO jokenpo (qt_vencidas,qt_derrotas)VALUES(1,1)"
            cursor.execute(comando_SQL)
            formulario.close()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("janela.ui")
formulario.pushButton.clicked.connect(funcao_p)


select_vitorias = "SELECT * FROM jokenpo WHERE qt_vencidas > 0 "
select_derrotas = "SELECT * FROM jokenpo WHERE qt_derrotas > 0"
cursor.execute(select_vitorias)
val = cursor.fetchall()
for valores in val:
    formulario.vitorias.setText(str(cursor.rowcount))
   

cursor.execute(select_derrotas)
vall = cursor.fetchall()
for valores_derrota in vall:
    formulario.derrotas.setText(str(cursor.rowcount))


formulario.show()
app.exec()
