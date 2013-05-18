#!/usr/bin/env python

from pymongo import Connection

class UserDB:
	def __init__(self):
		con = Connection()
		db = con.teapot
		self._users = db.user

	def get_user_by_name(self, name):
		user = self._users.find_one({"name" : name})
		return user

	def create_user(self, name, mail, password):
		user = {
			'name'     : name,
			'mail'     : mail,
			'password' : password
		}
		self._users.insert(user)

	def get_all_users(self):
		users = self._users.find()
		return users


if __name__ == "__main__":
	db = UserDB()
