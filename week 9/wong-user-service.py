# 
# ============================================
# ; Title:  Exercise 9.2
# ; Author: Devan Wong
# ; Date:   9 December 2020
# ; Description: – Querying and Creating Documents
# ;===========================================
# 

from pymongo import MongoClient

import pprint
import datetime 

client = MongoClient('localhost', 27017)
db = client.web335

user = {
    "first_name": "Michael",
    "last_name": "Scott",
    "email": "michaelbscott@theoffice.com",
    "employee_id": "7654321",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "7654321"}))
