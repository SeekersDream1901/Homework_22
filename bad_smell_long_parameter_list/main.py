# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, type_move, speed):
        self.x = 0
        self.y = 0
        self.type_move = type_move
        self.speed = speed

    def _get_speed(self):
        if self.type_move == 'fly':
            self.speed = self.speed * 1.2
            return self.speed
        elif self.type_move == 'crawl':
            self.speed = self.speed * 1.2
            return self.speed

    def move(self, field, direction):
        speed = self._get_speed()

        if direction == 'UP':
            field.set_unit(x=self.x, y=self.y + speed, unit=self)
        elif direction == 'DOWN':
            field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif direction == 'LEFT':
            field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif direction == 'RIGTH':
            field.set_unit(x=self.x + speed, y=self.y, unit=self)
