#!/usr/bin/env python
import hashlib
import os
import sys
sys.path.append(os.path.abspath('.') + "/../model")
from userdb import UserDB

class UserManager:
	def __init__(self, mail, password, name=None):
		self._name = name
		self._mail = mail
		self._password = password
		#self._userDB = UserDB()

	def encode_password(self):
		self._password = hashlib.md5(self._password).hexdigest()

	def create_new_user(self):
		if self.is_user_existed():
			return False
		self.encode_password()
		self._userDB.create_user(self._name, self._mail, self._password)
		return True

	def is_user_existed(self):
		return self._userDB.get_user_by_name(self._name)

	def is_validate(self):
		return True

    #def get_nickname(self):
    #    return self._userDB.get_user_by_mail()._name

	def is_active(self):
		return True

	def get_id(self):
		return self._mail

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

	@staticmethod
	def get(mail):
		#return self._userDB.get_user_by_mail(mail)
		return UserManager(mail=mail, name="1", password="1")
