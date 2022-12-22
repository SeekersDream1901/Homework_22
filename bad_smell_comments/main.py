

class Unit:

    def move(self, field, field_x, field_y, course, is_fly, is_crawl, speed=1):
        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if course == 'UP':
                new_y = field_y + speed
                new_x = field_x
            elif course == 'DOWN':
                new_y = field_y - speed
                new_x = field_x
            elif course == 'LEFT':
                new_y = field_y
                new_x = field_x - speed
            elif course == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed
        if is_crawl:
            speed *= 0.5
            if course == 'UP':
                new_y = field_y + speed
                new_x = field_x
            elif course == 'DOWN':
                new_y = field_y - speed
                new_x = field_x
            elif course == 'LEFT':
                new_y = field_y
                new_x = field_x - speed
            elif course == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
