import sys
from PyQt5 import QtWidgets, QtSql
from getpass import getpass
from mysql.connector import connect, Error
from PyQt5.QtWidgets import QDialog, QApplication
import menu, tour_menu, customer_menu, customer_info, passport_info, excursion_info, customer_tour_info, tour_info, country_info, hotel_info
import config, db_table, db_procedures, db_triggers, create_db
from datetime import date

class Main(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def tour_menu(self):
        self.tour_menu = TourMenu()
        self.tour_menu.show()
        self.hide()

    def excursion_info(self):
        self.excursion_info = ExcursionInfo()
        self.excursion_info.show()
        self.hide()

    def customer_menu(self):
        self.customer_menu = CustomerMenu()
        self.customer_menu.show()
        self.hide()   

    def country_info(self):
        self.country_info = CountryInfo()
        self.country_info.show()
        self.hide()

    def hotel_info(self):
        self.hotel__info = HotelInfo()
        self.hotel__info.show()
        self.hide()

    def create_db(self):
        self.create_db = CreateDB()
        self.create_db.show()
        self.hide()

    def init(self):
        self.pushButton.clicked.connect(self.customer_menu)
        self.pushButton_3.clicked.connect(self.tour_menu)
        self.pushButton_2.clicked.connect(self.excursion_info)
        self.pushButton_5.clicked.connect(self.hotel_info)
        self.pushButton_4.clicked.connect(self.country_info)
        self.pushButton_6.clicked.connect(self.create_db)

class TourMenu(QtWidgets.QMainWindow, tour_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.tour_info)
        self.pushButton_2.clicked.connect(self.customer_tour_info)

    def tour_info(self):
        self.tour_info = TourInfo()
        self.tour_info.show()
        self.hide()

    def customer_tour_info(self):
        self.customer_tour_info = CustomerTourInfo()
        self.customer_tour_info.show()
        self.hide() 

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()
        self.init()

class CustomerMenu(QtWidgets.QMainWindow, customer_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.customer_info)
        self.pushButton_2.clicked.connect(self.customer_passport_info) 

    def customer_info(self):
        self.customer_info = CustomerInfo()
        self.customer_info.show()
        self.hide()

    def customer_passport_info(self):
        self.customer_passport_info = CustomerPassportInfo()
        self.customer_passport_info.show()
        self.hide()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()        
        
class CustomerInfo(QtWidgets.QMainWindow, customer_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
    
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from customer"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 4):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO customer (name, surname, phone) VALUES (%s, %s, %s)"
                insert_tuple = [(name, surname, phone)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from customer where idCustomer = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()
    
    def back(self):
        self.createDB = CustomerMenu()
        self.createDB.show()
        self.hide()

class CustomerPassportInfo(QtWidgets.QMainWindow, passport_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from passport"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        pasportNo = self.lineEdit.text()
        dateOfIssue = self.lineEdit_3.text()
        dateOfExpiry = self.lineEdit_4.text()
        idCustomer = self.lineEdit_5.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO passport (pasportNo, dateOfIssue, dateOfExpiry, idCustomer) VALUES (%s, %s, %s, %s)"
                insert_tuple = [(pasportNo, dateOfIssue, dateOfExpiry, idCustomer)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from passport where idPassport = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = CustomerMenu()
        self.createDB.show()
        self.hide()

class ExcursionInfo(QtWidgets.QMainWindow, excursion_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete) 

    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from excursion"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        nameExcursion = self.lineEdit.text()
        descriptionExcursion = self.lineEdit_3.text()
        dateOfExcursion = self.lineEdit_4.text()
        cost = self.lineEdit_5.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO excursion (nameExcursion, descriptionExcursion, dateOfExcursion, cost) VALUES (%s, %s, %s, %s)"
                insert_tuple = [(nameExcursion, descriptionExcursion, dateOfExcursion, cost)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from excursion where idExcursion = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb() 

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class TourInfo(QtWidgets.QMainWindow, tour_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from tour"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 3):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        idCountry = self.lineEdit_3.text()
        nameTour = self.lineEdit.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO tour (idCountry, nameTour) VALUES (%s, %s)"
                insert_tuple = [(idCountry, nameTour)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from tour where idTour = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = TourMenu()
        self.createDB.show()
        self.hide()

class CustomerTourInfo(QtWidgets.QMainWindow, customer_tour_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.tour_sum) 
        self.pushButton_6.clicked.connect(self.sum_sale)  

    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from customertour"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 10):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        idCustomer = self.lineEdit.text()
        beginDateOfTour = self.lineEdit_3.text()
        endDateOfTour = self.lineEdit_4.text()
        idTour = self.lineEdit_5.text()
        idHotel = self.lineEdit_6.text()
        idExcursion = self.lineEdit_7.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO customertour (idCustomer, beginDateOfTour, endDateOfTour, idTour, idHotel, idExcursion) VALUES (%s, %s, %s, %s, %s, %s)"
                insert_tuple = [(idCustomer, beginDateOfTour, endDateOfTour, idTour, idHotel, idExcursion)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_7.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from customertour where idCustomerTour = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb() 

    def tour_sum(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            query = "call calculate_tour_cost()"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                self.showdb() 

    def sum_sale(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            query = "call calculate_tour_discount()"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                self.showdb() 

    def back(self):
        self.createDB = TourMenu()
        self.createDB.show()
        self.hide()

class HotelInfo(QtWidgets.QMainWindow, hotel_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from hotel"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 4):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        nameHotel = self.lineEdit.text()
        idCountry = self.lineEdit_3.text()
        costHotel = self.lineEdit_5.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO hotel (nameHotel, idCountry, costHotel) VALUES (%s, %s, %s)"
                insert_tuple = [(nameHotel, idCountry, costHotel)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from hotel where idHotel = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class CountryInfo(QtWidgets.QMainWindow, country_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from country"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 2):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        nameCountry = self.lineEdit.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO country (nameCountry) VALUES (%s)"
                insert_tuple = [(nameCountry,)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from country where idCountry = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class CreateDB(QtWidgets.QMainWindow, create_db.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        #назначаем действия по кнопкам
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.create_table)
        self.pushButton_2.clicked.connect(self.create_triggers)
        self.pushButton_3.clicked.connect(self.create_procedures)

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

    def create_table(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
        ) as connection:
            query = db_table.script
            with connection.cursor() as cursor:
                cursor.execute(query)

    def create_procedures(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database = config.db,
        ) as connection:
            query = db_procedures.procedures
            with connection.cursor() as cursor:
                cursor.execute(query)

    def create_triggers(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database = config.db,
        ) as connection:
            query = db_triggers.triggers
            with connection.cursor() as cursor:
                cursor.execute(query)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()

if __name__ == '__main__':
    main()
