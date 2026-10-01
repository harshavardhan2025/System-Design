from datetime import datetime


class Student:

    def __init__(self, builder):
        self._name = builder._name
        self._age = builder._age
        self._grad_year = builder._grad_year
        self._college = builder._college
        self._branch = builder._branch
        self._email = builder._email

    # Getters

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def grad_year(self):
        return self._grad_year

    @property
    def college(self):
        return self._college

    @property
    def branch(self):
        return self._branch

    @property
    def email(self):
        return self._email

    # Display

    def __str__(self):
        return (
            f"Student(\n"
            f"  Name      = {self.name}\n"
            f"  Age       = {self.age}\n"
            f"  Grad Year = {self.grad_year}\n"
            f"  College   = {self.college}\n"
            f"  Branch    = {self.branch}\n"
            f"  Email     = {self.email}\n"
            f")"
        )

    # Builder 

    class Builder:

        def __init__(self):
            self._name = None
            self._age = None
            self._grad_year = None
            self._college = None
            self._branch = None
            self._email = None

        def set_name(self, name):
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name cannot be empty")

            self._name = name.strip()
            return self

        def set_age(self, age):
            if not isinstance(age, int):
                raise TypeError("Age must be an integer")

            if age <= 0:
                raise ValueError("Age must be greater than 0")

            self._age = age
            return self

        def set_grad_year(self, grad_year):
            if not isinstance(grad_year, int):
                raise TypeError("Graduation year must be an integer")

            current_year = datetime.now().year

            if grad_year < current_year:
                raise ValueError(
                    f"Graduation year cannot be before {current_year}"
                )

            self._grad_year = grad_year
            return self

        def set_college(self, college):
            if not isinstance(college, str) or not college.strip():
                raise ValueError("College cannot be empty")

            self._college = college.strip()
            return self

        def set_branch(self, branch):
            if not isinstance(branch, str) or not branch.strip():
                raise ValueError("Branch cannot be empty")

            self._branch = branch.strip()
            return self

        def set_email(self, email):
            if not isinstance(email, str) or "@" not in email:
                raise ValueError("Invalid email")

            self._email = email.strip()
            return self

        def build(self):
            # Required fields
            if self._name is None:
                raise ValueError("Name is required")

            if self._age is None:
                raise ValueError("Age is required")

            if self._grad_year is None:
                raise ValueError("Graduation year is required")

            return Student(self)




student1 = (
    Student.Builder()
    .set_name("Harsha")
    .set_age(20)
    .set_grad_year(2028)
    .set_college("KL University")
    .set_branch("CSE")
    .set_email("harsha@example.com")
    .build()
)

print(student1)
print(student1.name)