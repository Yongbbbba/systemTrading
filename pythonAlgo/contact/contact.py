# 간단한 주소록 만들기

# Contact 클래스 정의
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

# 주소록 입력


def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("e-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

# 주소록 출력


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# 주소록 삭제


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

# 주소록 프로그램 인터페이스


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

# 주소록 저장하기 - 프로그램 종료시


def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + "\n")
        f.write(contact.phone_number + "\n")
        f.wrtie(contact.e_mail + "\n")
        f.write(contact.addr + "\n")
    f.close()

# golang으로 보면 main함수 같은 기능


def run():
    contact_list = []
    while True:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("삭제하고자 하는 주소록의 이름을 입력해주세요 : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break
        else:
            continue


if __name__ == "__main__":
    run()
