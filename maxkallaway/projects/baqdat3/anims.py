# maxkallaway — baqdat3, «ref» стилі (референс: Instagram reel Dfm6-Rfs0fZ). Уақыттар — бастапқы видео секундымен.
KEEP = set()
NOTE = dict(type='note', slot='note', sfx='pop')
ANIMS = {
 1: dict(cam=[(0.0, 66.5)], end=68.85, style='ref', items=[],
   # музыка жоқ (пайдаланушы алып тастауды сұрады); жаңбыр/топырақ — студиядағы үлкен медиа карточкада
   ref=dict(
     accent=(201, 161, 90), accent2=(236, 206, 150), bg=(17, 15, 12), sticker_shadow=(246, 236, 214),
     marquee='TAMSHI PERFUMES • ', logo='brand/logo.png', logo_icon='brand/logo.png',
     cam_sub_y=1580, logo_w=240,   # камерада субтитр құтының астында (үстел үсті)
     giant_front=True,              # алып сөздер бастың ҮСТІНДЕ (артында емес)
     # SFX — Mixkit (тегін лицензия): ауысуда кезектесетін «вжух», алып сөзге жылтыр, карточкаға поп
     # деңгейлер: пайдаланушы сұрауымен барлығы −30%, алып сөздегі жылтыр (0:03) −60%
     sfx_files=dict(t1=('sfx/1492.mp3', 0.315), t2=('sfx/166.mp3', 0.315), t3=('sfx/1490.mp3', 0.294),
                    sparkle=('sfx/2350.mp3', 0.152), pop=('sfx/3005.mp3', 0.35), pop2=('sfx/2356.mp3', 0.315),
                    click=('sfx/2568.mp3', 0.315), ding=('sfx/3109.mp3', 0.28)),
     trans_sfx=['t1', 't2', 't3'], giant_sfx='sparkle',
     scenes=[
       dict(kind='cam', src=(0.0, 9.55)),
       dict(kind='studio', src=(9.55, 16.0), layout='card', face=(470, 900)),
       dict(kind='cam', src=(16.0, 24.9)),
       dict(kind='studio', src=(24.9, 27.2), layout='circle', face=(470, 900)),
       dict(kind='cam', src=(27.2, 30.5)),
       dict(kind='studio', src=(30.5, 41.45), layout='card', face=(470, 900)),
       dict(kind='cam', src=(41.45, 49.85)),
       dict(kind='studio', src=(49.85, 54.05), layout='none', to_rect=(90, 330, 900, 760), face=(470, 900)),
       dict(kind='cam', src=(54.05, 58.85)),
       dict(kind='studio', src=(58.85, 64.4), layout='none', to_rect=(96, 560, 888, 380), face=(470, 900), sub_y=1385),
       dict(kind='cam', src=(64.4, 68.85)),
     ],
     gfx=[
       dict(type='tag', sfx='pop2', text='ноталар', at=9.7, pos=(500, 470)),
       dict(NOTE, at=12.0, head='НОТА', num='01 / 05', name='Тубероза', clip='broll/3728.mp4', clip_start=3.0, pos=(500, 560)),
       dict(type='chip', sfx='pop2', text='сүтті', at=13.2, pos=(110, 1050)),
       dict(type='chip', sfx='pop2', text='жұмсақ', at=14.1, pos=(390, 1050)),
       dict(type='chip', sfx='pop2', text='кремді', at=14.7, pos=(700, 1050)),
       dict(NOTE, at=25.1, head='НОТА', num='02 / 05', name='Паприка', clip='broll/28392.mp4', clip_start=2.8, pos=(500, 540)),
       dict(NOTE, at=30.7, head='НОТА', num='03 / 05', name='Мате', clip='broll/20824.mp4', clip_start=1.0, pos=(500, 560)),
       dict(NOTE, at=32.7, head='НОТА', num='04 / 05', name='Көк шай', clip='broll/49323.mp4', clip_start=1.0, pos=(500, 560)),
       # тонка: тегін нақты видео жоқ — миндаль макросы қою қоңыр түске боялған (тонка бұршағына ұқсас)
       dict(NOTE, at=36.4, head='НОТА', num='05 / 05', name='Тонка', clip='broll/18365.mp4', clip_start=2.0,
            clip_vf='eq=brightness=-0.20:saturation=0.40:contrast=1.18,colorbalance=rs=-0.04:gs=-0.07:bs=-0.10', pos=(500, 560)),
       dict(type='chip', sfx='pop2', text='ваниль', at=37.7, pos=(110, 1050)),
       dict(type='bars', at=38.8, rows=[dict(label='тәттілік', at=38.8, full=41.0)], pos=(400, 1030)),
       dict(type='media', at=49.95, until=52.25, clip='broll/48004.mp4', clip_start=4.0, label='жаңбырдан кейін', pos=(90, 330), size=(900, 760), sfx='pop'),
       dict(type='media', at=52.25, clip='broll/45263.mp4', clip_start=2.0, label='топырақ', pos=(90, 330), size=(900, 760), sfx='pop'),
       dict(type='hours', sfx='click', at=59.0, until=62.1, draw_at=59.3, draw_full=61.2, head='ЖҰМЫС УАҚЫТЫ', open='09:00', close='23:00', sub='КҮН САЙЫН', pos=(96, 560)),
       dict(type='photo', at=62.1, photo='brand2/photo.jpg', pos=(240, 300), size=(600, 1000), focus_y=0.4, sfx='ding'),
     ],
     giant=[
       dict(text='ИІС', src=(3.0, 5.6), y=470),
       dict(text='ALDEBARAN', src=(6.8, 8.25), y=470),
       dict(text='АҚ ГҮЛ', src=(16.1, 18.6), y=420),
       dict(text='МІНЕЗ', src=(27.3, 29.6), y=420),
       dict(text='UNISEX', src=(45.2, 47.6), y=420),
       dict(text='TAMSHI', src=(64.5, 66.8), y=420),
     ],
   )),
}
