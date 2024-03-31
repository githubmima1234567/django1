import os
import pymysql
pymysql.install_as_MySQLdb()
import django
os.environ.setdefault('DJANGO_SETTING_MODULE', 'MyDjango.settings')
django.setup()