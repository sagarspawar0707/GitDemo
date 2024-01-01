import configparser

import mysql.connector



def getconfig():
    try:
        # Load configuration here
        config = configparser.ConfigParser()
        config.read('C:/Users/Admin/PycharmProjects/pythonApitesting/utilites/properties.ini')
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None

connect_config = {
    'user' : getconfig()['SQL']['user'],
    'password':getconfig()['SQL']['password'],
     'host':getconfig()['SQL']['host'],
     'database':getconfig()['SQL']['database'],
}
def getpassword():
    return "Shaunak@11"



def getconnction():
    try:
       conn = mysql.connector.connect(**connect_config)
       return conn
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None




