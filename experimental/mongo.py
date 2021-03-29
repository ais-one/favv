from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")

db = client["school"]

students = db["students"] # collection

# students.insert_one({
#   'name': 'Isaac',
#   'address': '10 Downing Street',
#   'scores': {
#     'maths': 54,
#     'english': 74
#   },
#   'shirt-size': 'm'
#   }
# )

# students.insert_many([
# {
# 'name': 'Isaac',
# 'address': '10 Downing Street',
# 'scores': {
# 'maths': 54,
# 'english': 74
# },
# 'shirt-size': 'm'
# },
# {
# 'name': 'Mary',
# 'address': '10 Downing Street',
# 'scores': {
# 'chemistry': 43,
# 'english': 64
# },
# 'shirt-size': 's'
# }, {
# 'name': 'Felix',
# 'address': '221B Baker Street',
# 'scores': {
# 'sleuthing': 100
# },
# 'shirt-size': 'l'
# }, {
# 'name': 'Bob',
# 'address': '221B Baker Street',
# 'scores': {
# 'medicine': 88,
# 'english': 98
# },
# 'shirt-size': 'm'
# }
# ])

def show_results(results):
  for result in results:
    pprint(result)

# results = students.find({ 'name': 'Mary' })
# results = students.find({ 'shirt-size': { '$in': ['m', 'l'] } })
# results = students.find({ 'shirt-size': 'm', 'address': '10 Downing Street' }) # and
# results = students.find({ 'scores.english': { '$lt': 90 } }) # .sort({ 'score': -1 })
#results = students.find({ '$or': [{ 'scores.english': { '$lt': 90 } }, { 'shirt-size': 'm' }] }).sort('scores.english', -1) # or

# show_results(results)
# students.update_one({ 'name': 'Mary' }, { '$set': { 'scores.chemistry': 1 } })
# students.delete_one({ 'name': 'Mary' })

