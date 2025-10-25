# Please Tayza include comments on each block of your code explaining the reason behind it.
# Indicate the topic or new development that is introduced based on the topic covered 
# I will choose the best ideas & then we'll work together  
import email
class Students:
    discount_amt = 200

    def __init__(self, first_name, last_name, tuition_fee, student_num):
        self.first_name = first_name
        self.last_name = last_name
        self.tuition_fee = tuition_fee
        self.student_num = student_num
        self.email_address = f"{first_name.lower()}.{last_name.lower()}@std.kyrenia.edu.tr"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_discount(self):
        self.tuition_fee = max(0, int(self.tuition_fee - self.discount_amt))

    def __repr__(self):
        return "Students({}, {}, {})".format(self.first_name, self.last_name, self.tuition_fee, str(self.student_num))
    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email_address)
    def __add__(self, other):
        return self.tuition_fee + other
    def display_info(self):
        return (
            f"Name: {self.full_name()}\n"
            f"Email: {self.email_address}\n"
            f"Student Number: {self.student_num}\n"
            f"Tuition Fee: €{self.tuition_fee}"
        )

k2023xxxx = Students('HTOO THANT', 'PAING', 16000, student_num="k20231314")
k2023xxxx.apply_discount()
student1 = Students("Tayza", "Htoo", 1200 , student_num="k20231310")
student1.apply_discount()
print(student1.display_info())
print(k2023xxxx.display_info())
print(student1.full_name())
print(k2023xxxx.full_name())
