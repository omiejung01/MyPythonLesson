# This is a sample Python script.

class ABACStudent:
    def __init__(self,student_id,student_name,previous_institute):
        self.student_id = student_id
        self.student_name = student_name
        self.previous_institute = previous_institute

    def display_gpa(self):
       return 'current GPA'

    def display_credits_earned(self):
       return 'current credit'


class MSMEStudent(ABACStudent):
    def __init__(self, major,specialization, certification):
        self.major = major
        self.specialization = specialization
        self.certification = certification

    def display_major(self):
        return self.major

    def display_certification(self):
        return self.certification

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Inheritence')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
