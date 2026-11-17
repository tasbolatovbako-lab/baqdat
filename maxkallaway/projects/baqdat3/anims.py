# maxkallaway — baqdat3, «ref» стилі (референс: Instagram reel Dfm6-Rfs0fZ). Уақыттар — бастапқы видео секундымен.
KEEP = set()
NOTE = dict(type='note', slot='note', sfx='pop')
ANIMS = {
 1: dict(cam=[(0.0, 66.5)], end=68.85, style='ref', items=[],
   # жаңбыр/топырақ B-roll (Mixkit) — камера сахнасы ішінде, рамкалы
   broll=[(49.85, 52.25, 'broll/48004.mp4', 4.0), (52.25, 54.05, 'broll/45263.mp4', 2.0)], broll_layout='frame',
   music='music/track.mp3', music_db=12,
   ref=dict(
     accent=(201, 161, 90), accent2=(236, 206, 150), bg=(17, 15, 12), sticker_shadow=(246, 236, 214),
     marquee='TAMSHI • ALDEBARAN • ', logo='brand/logo.png', logo_icon='brand/logo.png',
     cam_sub_y=1580, logo_w=240,   # камерада субтитр құтының астында (үстел үсті)
     scenes=[
       dict(kind='cam', src=(0.0, 9.55)),
       dict(kind='studio', src=(9.55, 16.0), layout='card', face=(470, 900)),
       dict(kind='cam', src=(16.0, 24.9)),
       dict(kind='studio', src=(24.9, 27.2), layout='circle', face=(470, 900)),
       dict(kind='cam', src=(27.2, 30.5)),
       dict(kind='studio', src=(30.5, 41.45), layout='card', face=(470, 900)),
       dict(kind='cam', src=(41.45, 58.85)),
       dict(kind='studio', src=(58.85, 64.4), layout='circle', face=(470, 900), sub_y=1360),
       dict(kind='cam', src=(64.4, 68.85)),
     ],
     gfx=[
       dict(type='tag', text='ноталар', at=9.7, pos=(500, 470)),
       dict(NOTE, at=12.0, head='НОТА', num='01 / 05', name='Тубероза', clip='broll/3728.mp4', clip_start=3.0, pos=(500, 560)),
       dict(type='chip', text='сүтті', at=13.2, pos=(110, 1050)),
       dict(type='chip', text='жұмсақ', at=14.1, pos=(390, 1050)),
       dict(type='chip', text='кремді', at=14.7, pos=(700, 1050)),
       dict(NOTE, at=25.1, head='НОТА', num='02 / 05', name='Паприка', clip='broll/28392.mp4', clip_start=2.8, pos=(500, 540)),
       dict(NOTE, at=30.7, head='НОТА', num='03 / 05', name='Мате', clip='broll/20824.mp4', clip_start=1.0, pos=(500, 560)),
       dict(NOTE, at=32.7, head='НОТА', num='04 / 05', name='Көк шай', clip='broll/49323.mp4', clip_start=1.0, pos=(500, 560)),
       dict(NOTE, at=36.4, head='НОТА', num='05 / 05', name='Тонка', pos=(500, 560)),
       dict(type='chip', text='ваниль', at=37.7, pos=(110, 1050)),
       dict(type='bars', at=38.8, rows=[dict(label='тәттілік', at=38.8, full=41.0)], pos=(400, 1030)),
       dict(type='counter', at=59.0, count_until=61.2, head='ЖҰМЫС УАҚЫТЫ', **{'from': 9, 'to': 23}, fmt='{:02d}:00', sub='КҮН САЙЫН', pos=(500, 520)),
       dict(type='logo', at=62.1, pos=(360, 860), sfx='ding'),
     ],
     giant=[
       dict(text='ИІС', src=(3.0, 5.6), y=630),
       dict(text='ALDEBARAN', src=(6.8, 8.25), y=640),
       dict(text='АҚ ГҮЛ', src=(16.1, 18.6), y=640),
       dict(text='МІНЕЗ', src=(27.3, 29.6), y=640),
       dict(text='UNISEX', src=(45.2, 47.6), y=640),
       dict(text='TAMSHI', src=(64.5, 66.8), y=640),
     ],
   )),
}
