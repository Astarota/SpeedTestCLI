from pages.speed_page import SpeedPage
import time
import pytest

def test_speed_test():
  j=0
  page=SpeedPage()
  print()
  name=page.asking_name()
  serialno=page.asking_serial_number()
  pretty_serialno=page.pretty_file_format(serialno)
  tid=page.id_of_test()
  page.create_excel_file(pretty_serialno)
  port=page.port_number()
  j+=1
  page.speedtest_database(name,serialno,tid,pretty_serialno,port,j)
  port=page.port_number()
  j+=1
  page.speedtest_database(name,serialno,tid,pretty_serialno,port,j)
  port=page.port_number()
  j+=1
  page.speedtest_database(name,serialno,tid,pretty_serialno,port,j)
  port=page.port_number()
  j+=1
  page.speedtest_database(name,serialno,tid,pretty_serialno,port,j)
