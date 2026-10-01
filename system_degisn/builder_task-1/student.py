from typing import List


class Student:
    def __init__(self, builder: "Student.Builder"):
        self.name = builder.name
        self.age = builder.age
        self.psp = builder.psp
        self.batch = builder.batch
        self.id = builder.id
        self.university_name = builder.university_name
        self.grad_year = builder.grad_year
        self.phone_number = builder.phone_number
        self.phone_numbers = list(builder.phone_numbers)

    @staticmethod
    def get_builder() -> "Student.Builder":
        return Student.Builder()

    class Builder:
        def __init__(self):
            self._name = ""
            self._age = 0
            self._psp = 0.0
            self._batch = ""
            self._id = 0
            self._university_name = ""
            self._grad_year = 0
            self._phone_number = ""
            self._phone_numbers = []

        @property
        def name(self) -> str:
            return self._name

        @property
        def age(self) -> int:
            return self._age

        @property
        def psp(self) -> float:
            return self._psp

        @property
        def batch(self) -> str:
            return self._batch

        @property
        def id(self) -> int:
            return self._id

        @property
        def university_name(self) -> str:
            return self._university_name

        @property
        def grad_year(self) -> int:
            return self._grad_year

        @property
        def phone_number(self) -> str:
            return self._phone_number

        @property
        def phone_numbers(self) -> List[str]:
            return self._phone_numbers

        def set_name(self, name: str) -> "Student.Builder":
            self._name = name
            return self

        def set_age(self, age: int) -> "Student.Builder":
            self._age = age
            return self

        def set_psp(self, psp: float) -> "Student.Builder":
            self._psp = psp
            return self

        def set_batch(self, batch: str) -> "Student.Builder":
            self._batch = batch
            return self

        def set_id(self, student_id: int) -> "Student.Builder":
            self._id = student_id
            return self

        def set_university_name(self, university_name: str) -> "Student.Builder":
            self._university_name = university_name
            return self

        def set_grad_year(self, grad_year: int) -> "Student.Builder":
            self._grad_year = grad_year
            return self

        def set_phone_number(self, phone_number: str) -> "Student.Builder":
            self._phone_number = phone_number
            return self

        def set_phone_numbers(self, phone_numbers: List[str]) -> "Student.Builder":
            self._phone_numbers = list(phone_numbers)
            return self

        def build(self) -> "Student":
            if not self._name.strip():
                raise ValueError("Name cannot be empty")

            if self._age < 18:
                raise ValueError("Age must be at least 18")

            if not 0 <= self._psp <= 100:
                raise ValueError("PSP must be between 0 and 100")

            if self._grad_year > 2022:
                raise ValueError("Grad year cannot be greater than 2022")

            return Student(self)
