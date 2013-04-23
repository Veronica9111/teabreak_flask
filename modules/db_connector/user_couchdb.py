#!/usr/bin/env python

from couchdb import *

class UserDB():
	def __init__(self):
		con = Server("http://127.0.0.1:5984")
		if con["user"] is not None:
			self._users = con["user"]
		else:
			self._users = con.create("user")

	def create_user(self, name, mail, password):
		self._users.save({'name' : name, 'mail' : mail, 'password' : password})

	def get_user_by_name(self, name):
		print self._users
		query = "function(doc) { if(doc.name == \"" + name + "\") emit(doc.name, doc.mail); }"
		results = self._users.query(query)
		for result in results:
			print result

if __name__ == "__main__":
	db = UserDB()
	print db.get_user_by_name("Veronica")
	#db.create_user("Veronica", "test@localhost.com", "111111")
