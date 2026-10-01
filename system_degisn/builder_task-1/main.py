from student import Student


student = (
    Student.get_builder().set_name("Naman")
    .set_age(21)
    .set_psp(89.21)
    .set_batch("April 21")
    .set_id(123)
    .set_university_name("ABC University")
    .set_grad_year(2021)
    .set_phone_number("9999999999")
    .set_phone_numbers(["9999999999", "8888888888"])
    .build()
)

print("Student createdsuccessfully")
