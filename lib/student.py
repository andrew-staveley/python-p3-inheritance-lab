#!/usr/bin/env python

from user import User

class Student(User):
    def learn(self, new_information):
        self.knowledge.append(new_information)