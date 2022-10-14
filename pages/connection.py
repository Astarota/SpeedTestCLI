import io
import time
import openpyxl as O
import speedtest
import re
import sys
import psycopg2
from psycopg2 import Error
from datetime import datetime
import hashlib

class Connection():
	def connect_to_database(self,author,serialno,testId,download_number,upload_number,duration,current_date,current_time,port_number):
		try:
			connection = psycopg2.connect(user="dssadmin",
							password="dssadmin",
							host="10.10.2.180",
							port="5432",
							database="devices")

			cursor = connection.cursor()

			    		# log this to db
			postgres_insert_query = """ INSERT INTO testhistory (author, serialno, testid, download, upload, date, time, duration,port) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}') """
			cursor.execute(postgres_insert_query.format(author, serialno, testId, download_number, 
			upload_number, current_date, current_time, duration,port_number))
			connection.commit()

				
		except (Exception, Error) as error:
				print("Ошибка при работе с PostgreSQL", error)
		finally:
				if connection:
					cursor.close()
					connection.close()
					print("Соединение с PostgreSQL закрыто")
					print("-"*157)