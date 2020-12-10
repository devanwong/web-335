# 
# ============================================
# ; Title:  Exercise 9.3
# ; Author: Devan Wong
# ; Date:   9 December 2020
# ; Description: – Updating and Deleting Documents
# ;===========================================
# 

from pymongo import MongoClient

import pprint 
import datetime 

client = MongoClient('localhost', 27017)

db = client.web335
db.users.update_one( 
   { "employee_id": "7654321" },
   {
       "$set": {
           "email": "dwong@my365.bellevue.edu"
       }
   }
)

pprint.pprint(db.users.find_one({"employee_id": "7654321"}))