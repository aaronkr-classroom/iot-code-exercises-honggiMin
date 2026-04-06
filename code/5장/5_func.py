# 5_func.py

def return_info(name, phone, address, email) :
    contact_info = f"연락처\t: {phone}\n이메일\t: {email}"
    return f"이름\t: {name}\n{contact_info}\n주소\t: {address}"

def print_info(name, phone, address, email = "") :
    contact_info = f"연락처\t: {phone}\n이메일\t: {email}"
    print(f"이름\t: {name}\n{contact_info}\n주소\t: {address}")

print_info("honggi", "010-5555-5555", "청주")
person = return_info(email="hi@ut.ac.kr", phone="010-3333-3333", address="교통대학교", name="honggi")
print()
print(person)
