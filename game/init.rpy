# Определение персонажей

define t = Character('Тарас', color="#5b9cc2")
define o = Character('Ольга UA', color="#4d9058ff", image='olga')
define p = Character('Пес Патрон', color="#7d8602ff", image='patron')

# До того, как бот представится
define a = Character('???', color="#000000ff", image='olga')



# Оператор "Послать Ольгу при знакомстве"

define screw_olga = False




# Вибори для хтівок Патрона у главі 1

define choice_specify = False
define choice_eat_strawberry = False
define choice_yes = False








# Расположение по бокам (на 2 людей)

init:
    $ left2 = Position(xalign=0.2)
    $ right2 = Position(xalign=0.8)


# Музыка и звуки

define audio.door = "audio/door_open.mp3"
define audio.notification = "audio/notification.mp3"