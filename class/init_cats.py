class Cat():
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def meow(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}, 야옹 야옹~')


nabi=Cat('나비','검정색')
nabi.meow()
nero=Cat('네로','흰색')
nero.meow()
mimi=Cat('미미','갈색')
mimi.meow()