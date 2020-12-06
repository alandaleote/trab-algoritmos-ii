from Person import Person 

class Student(Person):
    def __init__(self, id, name, country, module):
        super().__init__(self, id, name, country)
        self.module = module
        



query = 


CREATE TABLE IF NOT EXISTS students (
    student_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    module VARCHAR(50) NOT NULL,
    PRIMARY KEY (student_id);

CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    PRIMARY KEY (teacher_id);



cursor.execute(query)