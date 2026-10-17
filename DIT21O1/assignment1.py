class Vaccine:
    total = 0

    def __init__(self, id, name, doses):
        self.id = id
        self.name = name
        self.doses = doses
        Vaccine.total = Vaccine.total + 1

    def show(self):
        print("Vaccine ID:", self.id)
        print("Name:", self.name)
        print("Doses needed:", self.doses)

    @classmethod
    def how_many(cls):
        return cls.total

    @staticmethod
    def check_name(name):
        if len(name) > 2:
            return True
        else:
            return False


class Patient:
    def __init__(self, pid, age_group):
        self.pid = pid
        self.age_group = age_group
        self.vaccines = []
        self.status = "Not Vaccinated"

    def give_vaccine(self, vaccine):
        self.vaccines.append(vaccine)
        self.status = "Vaccinated"

    def show(self):
        print("Patient ID:", self.pid)
        print("Age Group:", self.age_group)
        print("Status:", self.status)
        print("Vaccines:")
        if len(self.vaccines) == 0:
            print("None")
        else:
            for v in self.vaccines:
                print("-", v.name)

    def change_status(self, new_status):
        self.status = new_status


class Tracker:
    def __init__(self):
        self.patients = {}

    def add(self, patient):
        self.patients[patient.pid] = patient
        print("Added patient", patient.pid)

    def show_all(self):
        print("\nAll Patients:")
        for p in self.patients.values():
            p.show()
            print("------------------")

    def find(self, pid):
        if pid in self.patients:
            return self.patients[pid]
        else:
            return None


tracker = Tracker()

v1 = Vaccine("V001", "Pfizer", 2)
v2 = Vaccine("V002", "Moderna", 2)
v3 = Vaccine("V003", "Johnson", 1)

p1 = Patient("P1001", "18-25")
p2 = Patient("P1002", "26-40")
p3 = Patient("P1003", "41-60")

p1.give_vaccine(v1)
p2.give_vaccine(v2)
p2.give_vaccine(v3)
p3.give_vaccine(v1)

tracker.add(p1)
tracker.add(p2)
tracker.add(p3)

tracker.show_all()

print("\nTotal vaccines made:", Vaccine.how_many())
print("Is Pfizer ok?", Vaccine.check_name("Pfizer"))

found = tracker.find("P1002")
if found != None:
    print("\nFound this patient:")
    found.show()