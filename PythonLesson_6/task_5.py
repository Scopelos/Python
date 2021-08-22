class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationary):
    def draw(self):
        print("Отрисовка ручкой.")


class Pencil(Stationary):
    def draw(self):
        print("Отрисовка карандашом.")


class Handle(Stationary):
    def draw(self):
        print("Отрисовка маркером.")


a = Stationary("Papeleria_1")
print(a.title)
a.draw()
b = Pen("Papeleria_2")
print(b.title)
b.draw()
c = Pencil("Papeleria_3")
print(c.title)
c.draw()
d = Handle("Papeleria_4")
print(d.title)
d.draw()


