from tkinter import *
import mysql.connector
from tkinter import messagebox
from geopy import Nominatim
from geopy import distance
from matplotlib import pyplot as plt
import requests

mydb = mysql.connector.connect(
			host = "localhost",
			user = "username",
			passwd = "passwd",
			database = "dbname"
		)

mycursor = mydb.cursor()
