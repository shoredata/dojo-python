import datetime
import bcrypt
import random
import string
from decimal import *

from .models import User, Account, Delivery, Truck, Location, DataImport

def importSDRecord(sRecord, lRecordNumber, sSDFile):
    return False