
import mysql
import mysql.connector

from . import file_io



def read_socios(file):
    df = file_io.get_dataframe(file)
    yield df


