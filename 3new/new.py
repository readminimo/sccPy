professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]
professor_wizaar = [
    {'name': '댐댐', 'age': 116},
    {'name': '맥맥', 'age': 85},
    {'name': '스', 'age': 60},
]

# 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# 마법사의 이름을 받으면, age를 리턴해주는 함수

def get_age(name,group):
    for v in group:
        if v['name'] == name:
            return v['age']

print(get_age('덤블도어', professor_wizards))