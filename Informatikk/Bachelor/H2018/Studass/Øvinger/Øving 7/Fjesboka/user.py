class User:
    given_name, last_name, age, gender, status = None, None, None, None, None




    def get_given_name(self):
        return self.given_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.get_given_name() + " " + self.get_last_name()

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_status(self):
        return self.status

    def set_info(self, liste):
        self.given_name, self.last_name, self.age, self.gender, self.status = liste[0], liste[1], int(liste[2]), liste[3], liste[4]

    def get_info(self):
        return [self.get_given_name(), self.last_name, self.get_age(), self.get_gender(), self.get_status()]

    def __str__(self):
        return self.given_name + " " + self.last_name + " is " + str(self.age) + " years old, his relationship status is " + self.status