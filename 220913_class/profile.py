from pprint import pprint


class Profile:
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-",
        }

    def set_profile(self, profile):
        self.profile = profile

    def get_name(self):
        return self.profile["name"]

    def get_gender(self):
        return self.profile["gender"]

    def get_birthday(self):
        return self.profile["birthday"]

    def get_age(self):
        return self.profile["age"]

    def get_phone(self):
        return self.profile["phone"]

    def get_email(self):
        return self.profile["email"]


profile = Profile()
profile.set_profile({
    "name": str(input('이름을 입력하세요 : ')),
    "gender": str(input('성별을 입력하세요 : ')),
    "birthday": str(input('생일을 입력하세요 : ')),
    "age": int(input('나이을 입력하세요 : ')),
    "phone": str(input('핸드폰 번호를 입력하세요 : ')),
    "email": str(input('email 주소를 입력하세요 : ')),
})


pprint(profile.get_name())  # 이름 출력
pprint(profile.get_gender())  # 성별 출력
pprint(profile.get_birthday())  # 생일 출력
pprint(profile.get_age())  # 나이 출력
pprint(profile.get_phone())  # 핸드폰번호 출력
pprint(profile.get_email())  # 이메일 출력