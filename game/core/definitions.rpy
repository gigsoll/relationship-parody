# Shared game definitions.
# Keep characters, persistent story flags, shared positions, and audio aliases
# here so every story chapter can use them without cross-chapter dependencies.

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

# The choice screen uses this only when a single portrait occupies the center.
default menu_avoids_center_portrait = False








# Расположение по бокам (на 2 людей)

init:
    $ left2 = Position(xalign=0.2)
    $ right2 = Position(xalign=0.8)


# Character portraits use the height established by ``three bots.png`` (about
# 860px on the 1920x1080 stage). ``fit \"contain\"`` keeps the source aspect
# ratio, so a larger source file cannot make its character larger on screen.
transform character_portrait:
    xalign 0.5
    yalign 1.0
    ysize 860
    fit "contain"


# Explicit definitions override Ren'Py's automatic image discovery and apply
# the shared portrait transform to every expression. Keep new character
# portraits in this section and use ``character_portrait`` as well.
image olga = At("images/Olga/olga.png", character_portrait)
image olga angry = At("images/Olga/olga angry.png", character_portrait)
image olga angry say = At("images/Olga/olga angry say.png", character_portrait)
image olga gloomy say = At("images/Olga/olga gloomy say.png", character_portrait)
image olga say = At("images/Olga/olga say.png", character_portrait)
image olga surprised = At("images/Olga/olga surprised.png", character_portrait)
image patron = At("images/patron/patron.png", character_portrait)
image natalia = At("images/natalia/natalia.png", character_portrait)


# Bot-selection layout inside the black browser-content panel of
# ``bg site scary.png`` (x=220–1490, y=152–718). All portraits share the
# panel's bottom edge; Natalia is slightly taller than Olga, while Patron is
# shorter. The explicit positions leave a small visual gap between them.
transform bot_selection_olga:
    xpos 510
    xanchor 0.5
    ypos 718
    yanchor 1.0
    ysize 520
    fit "contain"

transform bot_selection_patron:
    xpos 850
    xanchor 0.5
    ypos 718
    yanchor 1.0
    ysize 490
    fit "contain"

transform bot_selection_natalia:
    xpos 1190
    xanchor 0.5
    ypos 718
    yanchor 1.0
    ysize 555
    fit "contain"


# Hover/focus panels sit behind the portraits in the browser selection screen.
transform bot_selection_highlight_olga:
    xpos 510
    xanchor 0.5
    ypos 718
    yanchor 1.0
    xysize (315, 540)

transform bot_selection_highlight_patron:
    xpos 850
    xanchor 0.5
    ypos 718
    yanchor 1.0
    xysize (325, 510)

transform bot_selection_highlight_natalia:
    xpos 1190
    xanchor 0.5
    ypos 718
    yanchor 1.0
    xysize (400, 565)


# Музыка и звуки

define audio.door = "audio/door_open.mp3"
define audio.notification = "audio/notification.mp3"
