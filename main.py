@namespace
class SpriteKind:
    bullet = SpriteKind.create()
    a1 = SpriteKind.create()
    a2 = SpriteKind.create()
    Food2_0 = SpriteKind.create()
    enemy2 = SpriteKind.create()
    ing = SpriteKind.create()
    ita = SpriteKind.create()
    shadow = SpriteKind.create()
    explo = SpriteKind.create()
    impstazioni = SpriteKind.create()
    plus = SpriteKind.create()
    minus = SpriteKind.create()
    undo = SpriteKind.create()
    credits_button = SpriteKind.create()
    black = SpriteKind.create()
@namespace
class StatusBarKind:
    volume = StatusBarKind.create()

def on_on_overlap(sprite11, otherSprite7):
    global meno_tempo, linguage, _1, frequenza, frequenza20, kill, ombra, copristatus2, statusbar2, life_brain, difficulty, fade, limit
    if controller.A.is_pressed() or controller.B.is_pressed():
        meno_tempo = game.runtime() / 1000
        italian.destroy()
        English.destroy()
        game.set_dialog_frame(assets.image("""
            text
            """))
        game.show_long_text("Usa i tasti \"WASD\" per muovere il proiettile e colpisci tutti i mostri",
            DialogLayout.FULL)
        game.set_dialog_frame(assets.image("""
            text trasparent
            """))
        linguage = 1
        music.stop_all_sounds()
        music.set_volume(volu)
        _1 = sprites.create(assets.image("""
            Black
            """), SpriteKind.a1)
        _1.set_flag(SpriteFlag.INVISIBLE, True)
        frequenza = 3000
        frequenza20 = 3000
        kill = 0
        ombra = sprites.create(img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffff....................................................................................................................ffffffffffffffffffffff
                ffffffffffffffff................................................................................................................................ffffffffffffffff
                fffffffffffff......................................................................................................................................fffffffffffff
                ffffffffff............................................................................................................................................ffffffffff
                ffffffff................................................................................................................................................ffffffff
                ffffff....................................................................................................................................................ffffff
                fffff......................................................................................................................................................fffff
                ffff........................................................................................................................................................ffff
                ffff........................................................................................................................................................ffff
                fff..........................................................................................................................................................fff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff...........................................................................................................................................................fff
                ff..........................................................................................................................................................ffff
                ff..........................................................................................................................................................ffff
                ff.........................................................................................................................................................fffff
                ff........................................................................................................................................................ffffff
                ff......................................................................................................................................................ffffffff
                ff....................................................................................................................................................ffffffffff
                ff.................................................................................................................................................fffffffffffff
                ff..............................................................................................................................................ffffffffffffffff
                ff..............ffffff....................................................................................................................ffffffffffffffffffffff
                ff..............ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fff............fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffff..........ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            SpriteKind.shadow)
        ombra.set_position(80, 60)
        ombra.z = 99999999
        copristatus2 = sprites.create(img("""
                fffff...........ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            SpriteKind.shadow)
        copristatus2.z = 100000009
        copristatus2.set_position(80, 117)
        statusbar2 = statusbars.create(160, 4, StatusBarKind.magic)
        statusbar2.set_color(6, 0, 0)
        statusbar2.max = 40
        statusbar2.value = 0
        statusbar2.set_position(80, 117)
        statusbar2.z = 100000000
        color.set_color(7, color.rgb(220, 70, 0))
        if story.check_last_answer("          EASY"):
            life_brain = 8
            difficulty = 1
        elif story.check_last_answer("         MEDIUM"):
            life_brain = 5
            difficulty = 2
        elif story.check_last_answer("         HARDER"):
            life_brain = 3
            difficulty = 3
        elif story.check_last_answer("       IMPOSSIBLE"):
            life_brain = 0.5
            difficulty = 4
        color.set_color(3, color.rgb(255, 153, 204))
        color.fade_to_black.start_screen_effect(500)
        music.spooky.play()
        fade = 1
        scene.set_background_image(assets.image("""
            Background trasparent
            """))
        color.set_color(5, color.rgb(255, 200, 0))
        color.set_color(3, color.rgb(255, 153, 204))
        color.set_color(6, color.rgb(120, 120, 120))
        color.set_color(7, color.rgb(0, 200, 0))
        color.set_color(11, color.rgb(192, 192, 192))
        limit = life_brain
sprites.on_overlap(SpriteKind.bullet, SpriteKind.ita, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy(effects.spray, 500)
    statusbar.value += 1
sprites.on_overlap(SpriteKind.bullet, SpriteKind.food, on_on_overlap2)

def on_on_overlap3(sprite9, otherSprite5):
    sprite9.destroy()
    brain.start_effect(effects.ashes, 500)
    music.small_crash.play()
    statusbar.value += -1
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap3)

def on_on_overlap4(sprite15, otherSprite10):
    global black2, GAME
    if controller.A.is_pressed() or controller.B.is_pressed():
        black2 = sprites.create(img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffffffffbb1bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bffffffff11bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11bfffffbb1bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11bffff11bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11bfbb1bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11b11bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11bbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bff1bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bffff1bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11bffff1bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bffffff1bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11bffbbbbb1bbbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbb1bbbb111111111111bfffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbb1111111bffff1bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111b1bfffffffff1bfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffb1bfffffffff11bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bfffffffffff1bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bfffffffffff1bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bfffffffffff1bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bfffffffffff1bffbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bfffffffbbbb1bfb11111bffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1bffffbbb1111bff1bbbbf1bfffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbb1111bfffff1b111b1bfffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbb1111bffffffff1b1bbf1bfffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbb111bfffffffffff1b111b1bfffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11bffffffffffffff1bbbbb1bfffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111bffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            SpriteKind.black)
        GAME = 4
sprites.on_overlap(SpriteKind.bullet, SpriteKind.credits_button, on_on_overlap4)

def on_overlap_tile(sprite12, location5):
    sprite12.destroy()
scene.on_overlap_tile(SpriteKind.enemy2,
    assets.tile("""
        myTile8
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite5, location2):
    sprite5.destroy()
scene.on_overlap_tile(SpriteKind.Food2_0,
    assets.tile("""
        myTile8
        """),
    on_overlap_tile2)

def Zombie_animation():
    if Math.percent_chance(50):
        if monster.x < 80:
            animation.run_image_animation(monster,
                assets.animation("""
                    animation zom 9
                    """),
                700,
                True)
        if monster.x > 80:
            animation.run_image_animation(monster,
                assets.animation("""
                    animation zom 10
                    """),
                700,
                True)
    else:
        if monster.x < 80:
            animation.run_image_animation(monster,
                assets.animation("""
                    animation zom 11
                    """),
                700,
                True)
        if monster.x > 80:
            animation.run_image_animation(monster,
                assets.animation("""
                    animation zom 12
                    """),
                700,
                True)

def on_menu_pressed():
    global menu
    if GAME == 0:
        menu += 1
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_overlap_tile3(sprite6, location3):
    sprite6.destroy()
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        myTile8
        """),
    on_overlap_tile3)

def on_on_overlap5(sprite17, otherSprite12):
    _0.destroy()
    music.beam_up.play()
    if linguage == 2:
        game.show_long_text("difficulty", DialogLayout.CENTER)
    else:
        game.show_long_text("difficoltà", DialogLayout.CENTER)
    game.show_long_text(story.get_last_answer(), DialogLayout.CENTER)
    if linguage == 2:
        game.show_long_text("time:", DialogLayout.CENTER)
    else:
        game.show_long_text("tempo:", DialogLayout.CENTER)
    game.show_long_text(Math.round(game.runtime() / 1000 - meno_tempo),
        DialogLayout.CENTER)
    if linguage == 2:
        game.show_long_text("kill:", DialogLayout.CENTER)
    else:
        game.show_long_text("uccisioni:", DialogLayout.CENTER)
    game.show_long_text(kill, DialogLayout.CENTER)
    if linguage == 2:
        game.show_long_text("esplosioni", DialogLayout.CENTER)
    else:
        game.show_long_text("explosion", DialogLayout.CENTER)
    game.show_long_text(num_eplosions, DialogLayout.CENTER)
    if linguage == 2:
        game.show_long_text("try again?", DialogLayout.CENTER)
    else:
        game.show_long_text("riprovare?", DialogLayout.CENTER)
    game.reset()
sprites.on_overlap(SpriteKind.a1, SpriteKind.a2, on_on_overlap5)

def Music():
    music.play_melody("D E A D F D A E ", 200)
    music.play_melody("E D - D C - - - ", 1200)

def on_overlap_tile4(sprite4, location):
    sprite4.destroy()
scene.on_overlap_tile(SpriteKind.bullet,
    assets.tile("""
        myTile8
        """),
    on_overlap_tile4)

def on_on_zero(status):
    global ombra, GAME, _0
    copristatus2.destroy()
    statusbar2.destroy()
    statusbar2.destroy()
    reload.destroy()
    sprites.destroy_all_sprites_of_kind(SpriteKind.explo)
    ombra = sprites.create(img("""
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            ................................................................................................................................................................
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            f..............................................................................................................................................................f
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            ff............................................................................................................................................................ff
            fff..........................................................................................................................................................fff
            ffff........................................................................................................................................................ffff
            ffff........................................................................................................................................................ffff
            fffff......................................................................................................................................................fffff
            ffffff....................................................................................................................................................ffffff
            ffffffff................................................................................................................................................ffffffff
            ffffffffff............................................................................................................................................ffffffffff
            fffffffffffff......................................................................................................................................fffffffffffff
            ffffffffffffffff................................................................................................................................ffffffffffffffff
            ffffffffffffffffffffff....................................................................................................................ffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            """),
        SpriteKind.player)
    GAME += 1
    color.set_color(6, color.rgb(0, 102, 0))
    music.stop_all_sounds()
    music.big_crash.play()
    tiles.set_tilemap(tilemap("""
        level6
        """))
    tiles.load_map(tiles.create_small_map(tilemap("""
        level4
        """)))
    pause(100)
    tiles.set_tilemap(tilemap("""
        level8
        """))
    if multic == 0:
        if Math.percent_chance(50):
            scene.set_background_image(assets.image("""
                animation 1
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 2
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 3
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 4
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 5
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 6
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 7
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 8
                """))
            pause(200)
            scene.set_background_image(img("""
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 10
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 11
                """))
            pause(200)
            scene.set_background_image(assets.image("""
                animation 12
                """))
        else:
            scene.set_background_image(assets.image("""
                Brain 1
                """))
            scene.set_background_image(assets.image("""
                Brain 2
                """))
            scene.set_background_image(assets.image("""
                Brain 3
                """))
            scene.set_background_image(assets.image("""
                Brain 4
                """))
            pause(500)
            scene.set_background_image(assets.image("""
                Brain 5
                """))
            pause(500)
            scene.set_background_image(assets.image("""
                Brain 6
                """))
            pause(500)
            scene.set_background_image(assets.image("""
                Brain 7
                """))
            pause(500)
            scene.set_background_image(assets.image("""
                Brain 8
                """))
            pause(500)
    elif multic == 1:
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff11111111111111111fff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff11111111111111111111111fff2222222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111fffffff111111111ff22222222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff1111111111111fffffffff1ffffff1111ff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f1111111111111fffffffffffffffffff11111f22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff1111111111111fffffffffffffffffffff11111ff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111fffffffffffffffffffffff111111f22222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f11111111111111ffffffffffffffffffffffff1111111f2222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f111111111111111fffffffffffffffffffffffff1111111f222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111fffffffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f111111111111111ffffffffffffffffffffffffffff11111111f2222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111fffffffffffffffffffffffffffff111111111f222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f1111111fff1111fffffffffffffffffffffffffffffff1111111111f22222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111fffffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f111111111ffffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111fffffffffffffffffffffffffffffffffffff11111111111f222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111f55fffffffffffffffffffffffffffffffff1111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f1111111111111f555555fffffffffffffffffffffffffffffff111111111111f2222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111f55555555fffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111ff55555555ffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f1111111111111ffff55555555555fffffffffffffffffffffffff111111111111f222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f11111111111111fbfff555555555555ffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f11111111111111ffbfff5555555555555fffffffffffffffffffffffff111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f11111111111111f5fbffff5555555555555555ffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111f55fbbfff5555555555555555555555ffffffffffffffff1111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f555fbbff55555555555555555555555ffffffffffff111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f5555ffbffffffff555555555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f555555fbbfffffff5555555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f5fff555fbfffffff55555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111f5feef5555fbfffffffffffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111f5feef5555fbffffffffffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111feef55555fbbffffbfffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111fef555555ffbbbbf555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111fef5ff55555ffff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222244444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222244444444442222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222222222222222fff11111111111111111fff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222222222222fff11111111111111111111111fff2222222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222444444444442222222222222222222222222222ff1111111111111fffffff111111111ff22222222222222222222222222222222222222222222222222222222222222
            222222222222222222222222244444444442222222222222222222222222222ff1111111111111fffffffff1ffffff1111ff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222244444444422222222222222222222222222222f1111111111111fffffffffffffffffff11111f22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222444444444222222222222222222222222222ff1111111111111fffffffffffffffffffff11111ff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222244444444222222222222222222222222222f11111111111111fffffffffffffffffffffff111111f22222222222222222222222222222222222222222222222222222222
            2222222222222222222222244444444222222222222222222222222222f11111111111111ffffffffffffffffffffffff1111111f2222222222222222222222222222222222222222222222222222222
            222222222222222222222224444442222222222222222222222222222f111111111111111fffffffffffffffffffffffff1111111f222222222222222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222222222222222222f111111111111111fffffffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222222222222
            2222222222222222222222444444422222222222222222222222222f111111111111111ffffffffffffffffffffffffffff11111111f2222222222222222222222222222222222222222222222222222
            222222222222222222222244444422222222222222222222222222f111111111111111fffffffffffffffffffffffffffff111111111f222222222222222222222222222222222222222222222222222
            22222222222222222222244444442222222222222222222222222f1111111fff1111fffffffffffffffffffffffffffffff1111111111f22222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111111fffffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f111111111ffffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f11111111111fffffffffffffffffffffffffffffffffffff11111111111f222222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111111111fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111111111fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111111111f55fffffffffffffffffffffffffffffffff1111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f1111111111111f555555fffffffffffffffffffffffffffffff111111111111f2222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111f55555555fffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111ff55555555ffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f1111111111111ffff55555555555fffffffffffffffffffffffff111111111111f222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f11111111111111fbfff555555555555ffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f11111111111111ffbfff5555555555555fffffffffffffffffffffffff111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f11111111111111f5fbffff5555555555555555ffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111f55fbbfff5555555555555555555555ffffffffffffffff1111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f555fbbff55555555555555555555555ffffffffffff111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f5555ffbffffffff555555555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f555555fbbfffffff5555555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111f5fff555fbfffffff55555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111f5feef5555fbfffffffffffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111f5feef5555fbffffffffffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111feef55555fbbffffbfffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111fef555555ffbbbbf555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111fef5ff55555ffff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222244444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222244444444442222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222222222222222fff11111111111111111fff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222222222222fff11111111111111111111111fff2222222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222444444444442222222222222222222222222222ff1111111111111fffffff111111111ff22222222222222222222222222222222222222222222222222222222222222
            222222222222222222222222244444444442222222222222222222222222222ff1111111111111fffffffff1ffffff1111ff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222244444444422222222222222222222222222222f1111111111111fffffffffffffffffff11111f22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222444444444222222222222222222222222222ff1111111111111fffffffffffffffffffff11111ff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222244444444222222222222222222222222222f11111111111111fffffffffffffffffffffff111111f22222222222222222222222222222222222222222222222222222222
            2222222222222222222222244444444222222222222222222222222222f11111111111111ffffffffffffffffffffffff1111111f2222222222222222222222222222222222222222222222222222222
            222222222222222222222224444442222222222222222222222222222f111111111111111fffffffffffffffffffffffff1111111f222222222222222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222222222222222222f111111111111111fffffffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222222222222
            2222222222222222222222444444422222222222222222222222222f111111111111111ffffffffffffffffffffffffffff11111111f2222222222222222222222222222222222222222222222222222
            222222222222222222222244444422222222222222222222222222f111111111111111fffffffffffffffffffffffffffff111111111f222222222222222222222222222222222222222222222222222
            22222222222222222222244444442222222222222222222222222f1111111fff1111fffffffffffffffffffffffffffffff1111111111f22222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111111fffffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f111111111ffffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f11111111111fffffffffffffffffffffffffffffffffffff11111111111f222222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111111111fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111111111fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111111111f55fffffffffffffffffffffffffffffffff1111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f1111111111111f555555fffffffffffffffffffffffffffffff111111111111f2222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f11111111111111f55555555fffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f11111111111111ff55555555ffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f1111111111111ffff55555555555fffffffffffffffffffffffff111111111111f222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111111fbfff555555555555ffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111111ffbfff5555555555555fffffffffffffffffffffffff111111111f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111111f5fbffff5555555555555555ffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222
            22222222222222222222244444422222222222222244444111111111111111f55fbbfff5555555555555555555555ffffffffffffffff1111111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111111f555fbbff55555555555555555555555ffffffffffff111111111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111111f5555ffbffffffff555555555555555555f111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222444444422222222222222444441111111111111111f555555fbbfffffff5555555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222244444422222222222222444441111111111111111f5fff555fbfffffff55555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222244444111111111111111f5feef5555fbfffffffffffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444422222222222444444111111111111111f5feef5555fbffffffffffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222224444444222222222224444441111111111111111feef55555fbbffffbfffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222244444444422222222444444411111111111111111fef555555ffbbbbf555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222224444444422222224444444411111111111111111fef5ff55555ffff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444222244444444f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444444444444444f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222244444444444444444442f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222224444444444444444422f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222444444444444444422f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222224444444444442222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222224444444444422222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222244444444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222444442222222222222222222222244444444444444222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222244444442222222222222222222222444444444444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222444444442222222222222222222224444444444444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222224444444444222222222222222222222444444442244444444ffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444444222f4444444111111111111fff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444442fff11444444111111111111111fff2222222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222444444444442222222222222222222222444444ff1111111111111fffffff111111111ff22222222222222222222222222222222222222222222222222222222222222
            222222222222222222222222244444444442222222222222222222222224444441111111111111fffffffff1ffffff1111ff222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222224444444442222222222222222222222222244444111111111111fffffffffffffffffff11111f22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222444444444222222222222222222222222224444411111111111fffffffffffffffffffff11111ff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222244444444222222222222222222222222222444441111111111fffffffffffffffffffffff111111f22222222222222222222222222222222222222222222222222222222
            2222222222222222222222244444444222222222222222222222222222f44444111111111ffffffffffffffffffffffff1111111f2222222222222222222222222222222222222222222222222222222
            222222222222222222222224444442222222222222222222222222222f144444111111111fffffffffffffffffffffffff1111111f222222222222222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222222222222222222f114444411111111fffffffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222222222222
            2222222222222222222222444444422222222222222222222222222f111444441111111ffffffffffffffffffffffffffff11111111f2222222222222222222222222222222222222222222222222222
            222222222222222222222244444422222222222222222222222222f111144444111111fffffffffffffffffffffffffffff111111111f222222222222222222222222222222222222222222222222222
            22222222222222222222244444442222222222222222222222222f11111444441111fffffffffffffffffffffffffffffff1111111111f22222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffffffffffffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f111111144444ffffffffffffffffffffffffffffffffffff11111111111f222222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441fffffffffffffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444f55fffffffffffffffffffffffffffffffff1111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444455555fffffffffffffffffffffffffffffff111111111111f2222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f11111111114444445555555fffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f111111111144444445555555ffffffffffffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f1111111111444444455555555555fffffffffffffffffffffffff111111111111f222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f111111111111444444f555555555555ffffffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f1111111111114444444f5555555555555fffffffffffffffffffffffff111111111f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111114444444ff5555555555555555ffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222
            22222222222222222222244444422222222222222244444111111111111114444444fff5555555555555555555555ffffffffffffffff1111111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111144444444bff55555555555555555555555ffffffffffff111111111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111114444444fbffffffff555555555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222224444444222222222222224444411111111111111144444444fbbfffffff5555555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444442222222222222244444111111111111111144444444fbfffffff55555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222244444111111111111111f54444444444444ffffffffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444422222222222444444111111111111111f54444444444444fffffffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222224444444222222222224444441111111111111111fe444444444444ffbfffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222244444444422222222444444411111111111111111fe44444444444bbf555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222224444444422222224444444411111111111111111fef4444444444ff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444222244444444f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444444444444444f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222244444444444444444442f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222224444444444444444422f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222444444444444444422f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222224444444444442222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222224444444444422222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222244444444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222444442222222222222222222222244444444444444222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222244444442222222222222222222222444444444444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222444444442222222222222222222224444444444444444442222222222222222222222222222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222224444444444222222222222222222222444444442244444444ffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444444222f4444444111111111111fff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444442fff11444444111111111111111fff2222222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222444444444442222222222222222222222444444ff1111111111111fffffff111111111ff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222444444444422222222222222222222222244444411111111444444ffffffff1ffffff1111ff222222222222222222222222222222222222222222222222222222222222
            222222222222222222222222444444444222222222222222222222222224444411111111144444444ffffffffffffff11111f22222222222222222222222222222222222222222222222222222222222
            2222222222222222222222224444444442222222222222222222222222244444111111111444444444ffffffffffffff11111ff222222222222222222222222222222222222222222222222222222222
            2222222222222222222222224444444422222222222222222222222222244444111111111444444444fffffffffffffff111111f22222222222222222222222222222222222222222222222222222222
            2222222222222222222222244444444222222222222222222222222222f44444111111111444444444fffffffffffffff1111111f2222222222222222222222222222222222222222222222222222222
            222222222222222222222224444442222222222222222222222222222f144444111111111ff4444444ffffffffffffffff1111111f222222222222222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222222222222222222f114444411111111fff4444444fffffffffffffffff1111111f22222222222222222222222222222222222222222222222222222
            2222222222222222222222444444422222222222222222222222222f111444441111111ffff4444444fffffffffffffffff11111111f2222222222222222222222222222222222222222222222222222
            222222222222222222222244444422222222222222222222222222f111144444111111fffff444444ffffffffffffffffff111111111f222222222222222222222222222222222222222222222222222
            22222222222222222222244444442222222222222222222222222f11111444441111fffffff4444444fffffffffffffffff1111111111f22222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444ffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444ffffffffffffffffff1111111111f2222222222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f111111144444ffffffffffff4444444fffffffffffffffff11111111111f222222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444fffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444fffffffffffffffff111111111111f22222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444f55ffffffffff444444fffffffffffffffff1111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444455555ffffffff44444ffffffffffffffffff111111111111f2222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f11111111114444445555555ffffff44444ffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f111111111144444445555555fffff44444ffffffffffffffffff1111111111111f222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f1111111111444444455555555555f44444fffffffffffffffffff111111111111f222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f111111111111444444f5555555555544444ffffffffffffffffffff111111111111f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f1111111111114444444f555555555544444fffffffffffffffffffffff111111111f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111114444444ff5555555444444555ffffffffffffffffffffff1111111f22222222222222222222222222222222222222222222
            22222222222222222222244444422222222222222244444111111111111114444444fff5555554444445555555555ffffffffffffffff1111111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111144444444bff55554444444555555555555ffffffffffff111111111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111114444444fbfffff444444455555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222224444444222222222222224444411111111111111144444444fbbff444444455555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444442222222222222244444111111111111111144444444fb444444444555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222244444111111111111111f5444444444444444444fffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444422222222222444444111111111111111f544444444444444444fffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222224444444222222222224444441111111111111111fe444444444444444fffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222244444444422222222444444411111111111111111fe44444444444444555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222224444444422222224444444411111111111111111fef4444444444ff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444222244444444f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444444444444444f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222244444444444444444442f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222224444444444444444422f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222444444444444444422f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222224444444444442222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444444444222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444422222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222224444444444422222222222224444444444444444444222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222244444444444442222222222224444444444444444444422222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222444442222222222222222222222244444444444444222222222224444444444444444444442222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222244444442222222222222222222222444444444444444442222222224444442222244444444444222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222444444442222222222222222222224444444444444444442222222224444442222222444444444422222222222222222222222222222222222222222222222222
            222222222222222222222222222224444444444222222222222222222222444444442244444444fffffffff4444422222222244444444442222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444444222f444444411111111144444f2222222224444444442222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444442fff11444444111111111111111fff2222222444444444222222222222222222222222222222222222222222222222
            22222222222222222222222222444444444442222222222222222222222444444ff1111111111111fffffff111111111ff22222244444444222222222222222222222222222222222222222222222222
            2222222222222222222222222444444444422222222222222222222222244444411111111444444ffffffff1ffffff1111ff222224444444422222222222222222222222222222222222222222222222
            222222222222222222222222444444444222222222222222222222222224444411111111144444444ffffffffffffff11111f22222444444422222222222222222222222222222222222222222222222
            2222222222222222222222224444444442222222222222222222222222244444111111111444444444ffffffffffffff11111ff222244444422222222222222222222222222222222222222222222222
            2222222222222222222222224444444422222222222222222222222222244444111111111444444444fffffffffffffff111111f22244444442222222222222222222222222222222222222222222222
            2222222222222222222222244444444222222222222222222222222222f44444111111111444444444fffffffffffffff1111111f2244444442222222222222222222222222222222222222222222222
            222222222222222222222224444442222222222222222222222222222f144444111111111ff4444444ffffffffffffffff1111111f224444442222222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222222222222222222f114444411111111fff4444444fffffffffffffffff1111111f24444444222222222222222222222222222222222222222222222
            2222222222222222222222444444422222222222222222222222222f111444441111111ffff4444444fffffffffffffffff11111111f2444444222222222222222222222222222222222222222222222
            222222222222222222222244444422222222222222222222222222f111144444111111fffff444444ffffffffffffffffff111111111f444444222222222222222222222222222222222222222222222
            22222222222222222222244444442222222222222222222222222f11111444441111fffffff4444444fffffffffffffffff1111111111444444222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444ffffffffffffffffff111111111444444222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444ffffffffffffffffff111111111144444222222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f111111144444ffffffffffff4444444fffffffffffffffff111111111144444222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444fffffffffffffffff111111111144444222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444fffffffffffffffff111111111144444222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444f55ffffffffff444444fffffffffffffffff111111111144444222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444455555ffffffff44444ffffffffffffffffff11111111144444222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f11111111114444445555555ffffff44444ffffffffffffffffff11111111444444222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f111111111144444445555555fffff44444ffffffffffffffffff11111111444444222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f1111111111444444455555555555f44444fffffffffffffffffff1111144444444222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f111111111111444444f5555555555544444ffffffffffffffffffff444444444444f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f1111111111114444444f555555555544444ffffffffffffffffffff444444444444f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111114444444ff5555555444444555fffffffffffffffff444444444441f22222222222222222222222222222222222222222222
            22222222222222222222244444422222222222222244444111111111111114444444fff5555554444445555555555ffffffffff4444444444411f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111144444444bff55554444444555555555555ffffffff4444444441111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111114444444fbfffff444444455555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222224444444222222222222224444411111111111111144444444fbbff444444455555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444442222222222222244444111111111111111144444444fb444444444555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222244444111111111111111f5444444444444444444fffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444422222222222444444111111111111111f544444444444444444fffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222224444444222222222224444441111111111111111fe444444444444444fffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222244444444422222222444444411111111111111111fe44444444444444555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222224444444422222224444444411111111111111111fef4444444444ff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444222244444444f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444444444444444f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222244444444444444444442f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222224444444444444444422f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222444444444444444422f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222224444444444442222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444444444222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444422222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222224444444444422222222222224444444444444444444222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222244444444444442222222222224444444444444444444422222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222444442222222222222222222222244444444444444222222222224444444444444444444442222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222244444442222222222222222222222444444444444444442222222224444442222244444444444222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222444444442222222222222222222224444444444444444442222222224444442222222444444444422222222222222222222222222222222222222222222222222
            222222222222222222222222222224444444444222222222222222222222444444442244444444fffffffff4444422222222244444444442222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444444222f444444411111111144444f2222222224444444442222222222222222222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444442fff11444444111111111111111fff2222222444444444222222222222222222222222222222222222222222222222
            22222222222222222222222222444444444442222222222222222222222444444ff1111111111111fffffff111111111ff22222244444444222222222222222222222222222222222222222222222222
            2222222222222222222222222444444444422222222222222222222222244444411111111444444ffffffff1ffffff1111ff222224444444422222222222222222222222222222222222222222222222
            222222222222222222222222444444444222222222222222222222222224444411111111144444444ffffffffffffff11111f22222444444422222222222222222222222222222222222222222222222
            2222222222222222222222224444444442222222222222222222222222244444111111111444444444ffffff44444fff11111ff222244444422222222222222222222222222222222222222222222222
            2222222222222222222222224444444422222222222222222222222222244444111111111444444444ffffff44444ffff111111f22244444442222222222222222222222222222222222222222222222
            2222222222222222222222244444444222222222222222222222222222f44444111111111444444444ffffff44444ffff1111111f2244444442222222222222222222222222222222222222222222222
            222222222222222222222224444442222222222222222222222222222f144444111111111ff4444444ffffff444444ffff1111111f224444442222222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222222222222222222f114444411111111fff4444444ffffff444444fffff1111111f24444444222222222222222222222222222222222222222222222
            2222222222222222222222444444422222222222222222222222222f111444441111111ffff4444444ffffff4444444ffff11111111f2444444222222222222222222222222222222222222222222222
            222222222222222222222244444422222222222222222222222222f111144444111111fffff444444fffffff4444444ffff111111111f444444222222222222222222222222222222222222222222222
            22222222222222222222244444442222222222222222222222222f11111444441111fffffff4444444fffffff444444ffff1111111111444444222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444fffffff4444444ffff111111111444444222222222222222222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444fffffff4444444ffff111111111144444222222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f111111144444ffffffffffff4444444fffffff4444444fff111111111144444222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444fffffff4444444fff111111111144444222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444ffffffff4444444ff111111111144444222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444f55ffffffffff444444ffffffff44444444f111111111144444222222222222222222222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444455555ffffffff44444fffffffff44444444f11111111144444222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f11111111114444445555555ffffff44444fffffffff44444444411111111444444222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f111111111144444445555555fffff44444ffffffffff4444444444111111444444222222222222222222222222222222222222222222222
            222222222222222222222444442222222222222222222222f1111111111444444455555555555f44444fffffffffff444444444411144444444222222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f111111111111444444f5555555555544444ffffffffffff44444444444444444444f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f1111111111114444444f555555555544444ffffffffffff44444444444444444444f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111114444444ff5555555444444555fffffffffff444444444444444441f22222222222222222222222222222222222222222222
            22222222222222222222244444422222222222222244444111111111111114444444fff5555554444445555555555fffff444444444444444411f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111144444444bff55554444444555555555555fffff4444444444441111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111114444444fbfffff444444455555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222224444444222222222222224444411111111111111144444444fbbff444444455555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444442222222222222244444111111111111111144444444fb444444444555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222244444111111111111111f5444444444444444444fffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444422222222222444444111111111111111f544444444444444444fffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222224444444222222222224444441111111111111111fe444444444444444fffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222244444444422222222444444411111111111111111fe44444444444444555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222224444444422222224444444411111111111111111fef4444444444ff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444222244444444f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444444444444444f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222244444444444444444442f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222224444444444444444422f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222444444444444444422f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222224444444444442222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444442222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444442222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444444444222222222222224444444222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444222222222224444444442222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444422222222224444444442222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222224444444444422222222222224444444444444444444222222222444444442222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222244444444444442222222222224444444444444444444422222222244444444222222222222222222222222222222222222
            2222222222222222222222222222222222444442222222222222222222222244444444444444222222222224444444444444444444442222222224444444422222222222222222222222222222222222
            2222222222222222222222222222222244444442222222222222222222222444444444444444442222222224444442222244444444444222222222444444422222222222222222222222222222222222
            2222222222222222222222222222222444444442222222222222222222224444444444444444442222222224444442222222444444444422222222444444442222222222222222222222222222222222
            222222222222222222222222222224444444444222222222222222222222444444442244444444fffffffff4444422222222244444444442222222244444442222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444444222f444444411111111144444f2222222224444444442222222224444444222222222222222222222222222222222
            2222222222222222222222222222444444444442222222222222222222244444442fff11444444111111111111111fff2222222444444444222222224444444222222222222222222222222222222222
            22222222222222222222222222444444444442222222222222222222222444444ff1111111111111fffffff111111111ff22222244444444222222222444444222222222222222222222222222222222
            2222222222222222222222222444444444422222222222222222222222244444411111111444444ffffffff1ffffff1111ff222224444444422222222444444422222222222222222222222222222222
            222222222222222222222222444444444222222222222222222222222224444411111111144444444ffffffffffffff11111f22222444444422222222244444422222222222222222222222222222222
            2222222222222222222222224444444442222222222222222222222222244444111111111444444444ffffff44444fff11111ff222244444422222222244444422222222222222222222222222222222
            2222222222222222222222224444444422222222222222222222222222244444111111111444444444ffffff44444ffff111111f22244444442222222244444422222222222222222222222222222222
            2222222222222222222222244444444222222222222222222222222222f44444111111111444444444ffffff44444ffff1111111f2244444442222222244444442222222222222222222222222222222
            222222222222222222222224444442222222222222222222222222222f144444111111111ff4444444ffffff444444ffff1111111f224444442222222224444442222222222222222222222222222222
            22222222222222222222224444444222222222222222222222222222f114444411111111fff4444444ffffff444444fffff1111111f24444444222222224444442222222222222222222222222222222
            2222222222222222222222444444422222222222222222222222222f111444441111111ffff4444444ffffff4444444ffff11111111f2444444222222224444442222222222222222222222222222222
            222222222222222222222244444422222222222222222222222222f111144444111111fffff444444fffffff4444444ffff111111111f444444222222224444442222222222222222222222222222222
            22222222222222222222244444442222222222222222222222222f11111444441111fffffff4444444fffffff444444ffff1111111111444444222222222444444222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444fffffff4444444ffff111111111444444222222222444444222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444fffffff4444444ffff111111111144444222222222444444222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f111111144444ffffffffffff4444444fffffff4444444fff111111111144444222222222444444222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444fffffff4444444fff111111111144444222222222244444222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444ffffffff4444444ff111111111144444222222222244444422222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444f55ffffffffff444444ffffffff44444444f111111111144444222222222244444444444422222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444455555ffffffff44444fffffffff44444444f11111111144444222222222244444444444422222222222222222222222
            222222222222222222222444442222222222222222222222f11111111114444445555555ffffff44444fffffffff44444444411111111444444222222222244444444444422222222222222222222222
            222222222222222222222444442222222222222222222222f111111111144444445555555fffff44444ffffffffff4444444444111111444444222222222224444444444422222222222222222222222
            222222222222222222222444442222222222222222222222f1111111111444444455555555555f44444fffffffffff444444444411144444444222222222224444444444422222222222222222222222
            22222222222222222222244444222222222222222222222f111111111111444444f5555555555544444ffffffffffff44444444444444444444f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f1111111111114444444f555555555544444ffffffffffff44444444444444444444f22222222222222222222222222222222222222222222
            22222222222222222222244444222222222222222222222f11111111111114444444ff5555555444444555fffffffffff444444444444444441f22222222222222222222222222222222222222222222
            22222222222222222222244444422222222222222244444111111111111114444444fff5555554444445555555555fffff444444444444444411f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111144444444bff55554444444555555555555fffff4444444444441111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111114444444fbfffff444444455555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222224444444222222222222224444411111111111111144444444fbbff444444455555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444442222222222222244444111111111111111144444444fb444444444555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222244444111111111111111f5444444444444444444fffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444422222222222444444111111111111111f544444444444444444fffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222224444444222222222224444441111111111111111fe444444444444444fffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222244444444422222222444444411111111111111111fe44444444444444555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222224444444422222224444444411111111111111111fef4444444444ff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444222244444444f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444444444444444f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222244444444444444444442f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222224444444444444444422f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222444444444444444422f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222224444444444442222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(300)
        scene.set_background_image(img("""
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444422222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444442222222222222222224444442222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444442222222222222222224444442222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224444444444222222222222224444444222222222222222224444442222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444222222222224444444442222222222222224444444222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222444444444444444422222222224444444442222222222222222444444222222222222222
            2222222222222222222222222222222222222222222222222222222222222224444444444422222222222224444444444444444444222222222444444442222222222222222444444422222222222222
            2222222222222222222222222222222222222222222222222222222222222244444444444442222222222224444444444444444444422222222244444444222222222222222444444422222222222222
            2222222222222222222222222222222222444442222222222222222222222244444444444444222222222224444444444444444444442222222224444444422222222222222244444422222222222222
            2222222222222222222222222222222244444442222222222222222222222444444444444444442222222224444442222244444444444222222222444444422222222222222244444442222222222222
            2222222222222222222222222222222444444442222222222222222222224444444444444444442222222224444442222222444444444422222222444444442222222222222224444442222222222222
            222222222222222222222222222224444444444222222222222222222222444444442244444444fffffffff4444422222222244444444442222222244444442222222222222224444444222222222222
            2222222222222222222222222222444444444442222222222222222222244444444222f444444411111111144444f2222222224444444442222222224444444222222222222224444444222222222222
            2222222222222222222222222222444444444442222222222222222222244444442fff11444444111111111111111fff2222222444444444222222224444444222222222222222444444422222222222
            22222222222222222222222222444444444442222222222222222222222444444ff1111111111111fffffff111111111ff22222244444444222222222444444222222222222222444444422222222222
            2222222222222222222222222444444444422222222222222222222222244444411111111444444ffffffff1ffffff1111ff222224444444422222222444444422222222222222244444422222222222
            222222222222222222222222444444444222222222222222222222222224444411111111144444444ffffffffffffff11111f22222444444422222222244444422222222222222244444422222222222
            2222222222222222222222224444444442222222222222222222222222244444111111111444444444ffffff44444fff11111ff222244444422222222244444422222222222222244444422222222222
            2222222222222222222222224444444422222222222222222222222222244444111111111444444444ffffff44444ffff111111f22244444442222222244444422222222222222224444422222222222
            2222222222222222222222244444444222222222222222222222222222f44444111111111444444444ffffff44444ffff1111111f2244444442222222244444442222222222222224444422222222222
            222222222222222222222224444442222222222222222222222222222f144444111111111ff4444444ffffff444444ffff1111111f224444442222222224444442222222222222224444422222222222
            22222222222222222222224444444222222222222222222222222222f114444411111111fff4444444ffffff444444fffff1111111f24444444222222224444442222222222222224444422222222222
            2222222222222222222222444444422222222222222222222222222f111444441111111ffff4444444ffffff4444444ffff11111111f2444444222222224444442222222222222224444422222222222
            222222222222222222222244444422222222222222222222222222f111144444111111fffff444444fffffff4444444ffff111111111f444444222222224444442222222222222224444422222222222
            22222222222222222222244444442222222222222222222222222f11111444441111fffffff4444444fffffff444444ffff1111111111444444222222222444444222222222222224444422222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444fffffff4444444ffff111111111444444222222222444444222222222222222222222222222222
            2222222222222222222224444442222222222222222222222222f11111144444ffffffffffff444444fffffff4444444ffff111111111144444222222222444444222222222222222222222222222222
            222222222222222222222444444222222222222222222222222f111111144444ffffffffffff4444444fffffff4444444fff111111111144444222222222444444222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444fffffff4444444fff111111111144444222222222244444222222222222222222222222222222
            22222222222222222222244444222222222222222222222222f11111111444441ffffffffffff444444ffffffff4444444ff111111111144444222222222244444422222222222222222222222222222
            2222222222222222222224444422222222222222222222222f11111111144444f55ffffffffff444444ffffffff44444444f111111111144444222222222244444444444422222222444444422222222
            2222222222222222222224444422222222222222222222222f11111111144444455555ffffffff44444fffffffff44444444f11111111144444222222222244444444444422222222444444422222222
            222222222222222222222444442222222222222222222222f11111111114444445555555ffffff44444fffffffff44444444411111111444444222222222244444444444422222222444444422222222
            222222222222222222222444442222222222222222222222f111111111144444445555555fffff44444ffffffffff4444444444111111444444222222222224444444444422222222444444422222222
            222222222222222222222444442222222222222222222222f1111111111444444455555555555f44444fffffffffff444444444411144444444222222222224444444444422222222444444422222222
            22222222222222222222244444222222222222222222222f111111111111444444f5555555555544444ffffffffffff44444444444444444444f22222222222222222222222222222444444422222222
            22222222222222222222244444222222222222222222222f1111111111114444444f555555555544444ffffffffffff44444444444444444444f22222222222222222222222222222444444222222222
            22222222222222222222244444222222222222222222222f11111111111114444444ff5555555444444555fffffffffff444444444444444441f22222222222222222222222222222222222222222222
            22222222222222222222244444422222222222222244444111111111111114444444fff5555554444445555555555fffff444444444444444411f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111144444444bff55554444444555555555555fffff4444444444441111f2222222222222222222222222222222222222222222
            222222222222222222222444444222222222222222444441111111111111114444444fbfffff444444455555555555555f111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222224444444222222222222224444411111111111111144444444fbbff444444455555555555555ff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444442222222222222244444111111111111111144444444fb444444444555555555555ffff111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444222222222222244444111111111111111f5444444444444444444fffffffffffffff1111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222224444444422222222222444444111111111111111f544444444444444444fffffffffffffff11111111111111111111f2222222222222222222222222222222222222222222
            222222222222222222222224444444222222222224444441111111111111111fe444444444444444fffbbffffbffbf55f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222244444444422222222444444411111111111111111fe44444444444444555ff5555feef555f1111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222224444444422222224444444411111111111111111fef4444444444ff5555555ffffeef5ff11111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444222244444444f11111111111111111ff5feef55555555555555f555ffeff1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222444444444444444444444f11111111111111111f555feef55555555555ff5555f4f111111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222244444444444444444442f111111111111111111f55feeef555555555f555555f45f11111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222224444444444444444422f1111111111111111111f5feeff55555555fef555555f45f1111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222444444444444444422f11111111111111111111f5ff555555555feef5555555ff5f111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222224444444444442222f111111111111111111111f555555555555feef555555f1ff111111111111111111111f2222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222f1111111111111111111111f5555555555fdfef555555ff11111111111111111111111f2222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f55555555ffdfdf5555555f4f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555555ffdfdfdf555555f45f111111111111111111111f22222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222f111111111111111111111f555fff5fddfddf55555f5ff1111111111111111111111f22222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111ffffddf45ffddf555555ff11111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfdfddffddff5555555f1ff111111111111111111111f222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222f11111111111111111111fdfddffdfdf55555555f4f5f111111111111111111111f222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111ffffddfdf55555555f455f111111111111111111111f2222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222f11111111111111111111fdfdfdff55555555f45fff111111111111111111111f2222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f11111111111111111111fdfff55555555ff45f444fffffff1111111111111f22222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222f111111111111111111111f5555555555f1f55ffff5ffffffff1111111111ff22222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222f11111111111111111111f555555555f111ff4445fbffffffff111111111f222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f1111111111111111111f55555555f1111f4455fffbfffffffff111111f2222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222f11111111111111111111f55555ff111fff55ff44fbbfffffffff11111f2222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222f11111111111111111111fffff111ffffffff54fbbbffffffffff111f22222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222f111111111111111111111111111fffffbf54ffbbbffffffffff11f222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222f1111111111111111111111111fffffbf44fbbbbfffffffffffff2222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222f111111111111111111111111fffffbbffbbbbbffffffffffff22222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222f1111111111111111111111ffffffbbbbbbbbffffffffffff222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222f111111111111111111111fffffffbbbbbbffffffffffff2222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222f11111111111111111111ffffffffbbbfffffffffffff22222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222ff111111111111111111fffffffffffffffffffffff222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222f11111111111111111fffffffffffffffffffff22222222222222222222222222222222222222222222222222222222222
            222222222222222222222222222222222222222222222222222222222222222ff111111111111111ffffffffffffffffffff222222222222222222222222222222222222222222222222222222222222
            22222222222222222222222222222222222222222222222222222222222222222ff1111111111111ffffffffffffffffff22222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222fff1111111111ffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222fff1111111fffffffffffff2222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222fffffffffffffffff2222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
            """))
        pause(500)
        color.set_palette(color.adafruit)
        scene.set_background_image(img("""
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaa9999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa9999999999999999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa99aaaaa999999999999999999999999999999999999999
            99999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa99aaaaaa99999999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999aaaaa99999999aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa99aaaaaaaa999999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999aaaaa99999999aaaaaaaaaaaaaaaaaaaaaaaaaa999999999999999999966666aaaaa99999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999aaaaaa9999999aaaaaaaaaaaaaaaa9999999999999999999999999999966666aaaaaaa999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999aaaaaa9999999aaaaaaaaa11111111111999999999999999999999999966666aaaaaaaa99999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999aaaaaaa999999aaaaaaffffffffffffff111999999999999999999999966666aaaaaaaa99999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999aaaaaaa999111faaaaafffffffffffffffff111999999999999999999966666aaaaaaaaa9999999999999999999999999999999
            99999999999999999aaaaaaaaaaaaaaaa9999999999999999999999999aaaaaaa11ffffaaaaaafff1111111fffffffff119999999999999999966666aaaaaaaaaa999999999999999999999999999999
            99999999999999999aaaaaaaaaaaaaaaaaa99999999999999999999999aaaaaaaffffffaaaaaaf111111111f111111ffff1199999999999999966666aa9aaaaaaa999999999999999999999999999999
            99999999999999999aaaaaaaaaaaaaaaaaaaa9999999999999999999999aaaaaaffffffaaaaaa111111111111111111fffff19999999999999966666aa9aaaaaaaa99999999999999999999999999999
            99999999999999999aaaaaaaaaaaaaaaaaaaaaa99999999999999999999aaaaaaffffffaaaaaa1111111111111111111fffff1199999999999966666aa99aaaaaaa99999999999999999999999999999
            99999999999999999aaaaaaaaaaaaaaaaaaaaaaaa9999999999999999991aaaaafffffffaaaaaa1111111111111111111ffffff19999999999966666aa999aaaaaaa9999999999999999999999999999
            999999999999999999aaaaaa99999aaaaaaaaaaaaaa9999999999999991faaaaafffffffaaaaaa1111111111111111111fffffff1999999999966666aa999aaaaaaaa999999999999999999999999999
            999999999999999999aaaaaaa999999aaaaaaaaaaaaa99999999999991ffaaaaaaffffffaaaaaa11111111111111111111fffffff199999999966666aa9999aaaaaaa999999999999999999999999999
            9999999999999999966666aaa99999999aaaaaaaaaaaa999999999991fffaaaaaaffffffaaaaaaa11111111111111111111fffffff19999999666666aa9999aaaaaaaa99999999999999999999999999
            99999999999999999666666aa9999999999aaaaaaaaaaa9999999991ffffaaaaaaaffff11aaaaaa11111111111111111111ffffffff1999999666666aa99999aaaaaaaa9999999999999999999999999
            99999999999999999666666aa999999999999aaaaaaaaaa99999991fffffaaaaaaafff111aaaaaa111111111111aaaaaaaaaafffffff199999666666aa999999aaaaaaa9999999999999999999999999
            999999999999999996666666aa9999999999999aaaaaaaaa999991fffffffaaaaaaa11111aaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffff19999666666aa999999aaaaaaaa999999999999999999999999
            999999999999999996666666aa99999999999999aaaaaaaaa9991ffffffffaaaaaaa111111aaaaaaaaaaaaaaaaaaaaaaaaaaafffffffff199966666aaa9999999aaaaaaa999999999999999999999999
            999999999999999999666666aaa99999999999999aaaaaaaa9991fffffffffaaaaaa1111166666aaaaaaaaaaaaaaaaaaaaaaafffffffff199966666aaa99999999aaaaaaa99999999999999999999999
            9999999999999999996666666aa999999999999999aaaaaaaa91ffffffffffaaaaaa1111166666aaaaaaaaaaaaaaaaaaaaaaaffffffffff19666666aaa99999999aaaaaaa99999999999999999999999
            99999999999999999996666666aa999999999999999aaaaaaaaffffffffffffaaaaa1111166666aaaaaaaaaaaaaaaaa11111ffffffffffff1666666aaa999999999aaaaaaa9999999999999999999999
            99999999999999999996666666aa9999999999999999aaaaaaaafffffffffffaaaaa1111166666aaaa111111111111111111ffffffffffff1666666aaa999999999aaaaaaa9999999999999999999999
            99999999999999999996666666aa9999999999999999aaaaaaaaffffffffff66666aa111166666aa11111111111111111111fffffffffffff666666aaa9999999999aaaaaa9999999999999999999999
            999999999999999999996666666aa9999999999999999aaaaaaaffffffffff66666aa811166666aa111111111111111111111ffffffffffff66666aaa99999999999aaaaaa9999999999999999999999
            999999999999999999999666666aa99999999999999999aaaaaaffffffffff66666aa8881666666aa11111111111111111111ffffffffffff66666aaa999999999999aaaaa9999999999999999999999
            999999999999999999999666666aa999999999999999999aaaaaffffffffff66666aa8888666666aa11111111111111111111fffffffffff666666aaa999999999999aaaaa9999999999999999999999
            9999999999999999999996666666a999999999999999999aaaaaffffffffff66666aaa888666666aa111111111111111111111ffffffffff666666aaa999999999999aaaaa9999999999999999999999
            9999999999999999999999666666a999999999999999999aaaaaafffffffff66666aaa888666666aa1111111111111111111111fffffffff666666aaa999999999999aaaaa9999999999999999999999
            9999999999999999999999666666aa99999999999999999aaaaaafffffffff66666aaa888866666aa1111111111111111111111111fffff6666666aa999999999999aaaaaa9999999999999999999999
            9999999999999999999999666666aa99999999999999999aaaaaafffffffff666666aa8888666666a888881111111111111111111111fff666666aaa99999999999aaaaaaa9999999999999999999999
            9999999999999999999999666666aaa9999999999999991aaaaaaaffffffff666666aa1888666666a8888888888881111111111111111ff666666aaa9999999999aaaaaaaa9999999999999999999999
            9999999999999999999999966666aaa9999999999999991faaaaaaffffffff6666666a1188666666aa8888888888888111111111111ffff666666aa9999999999aaaaaaaaa9999999999999999999999
            9999999999999999999999966666aaaa999999999999991faaaaaaffffffff6666666ac1116666666a8888888888888881aaaaaffffffff66666aaa99999999aaaaaaaaaa99999999999999999999999
            99999999999999999999999666666aaa999999999999991faaaaaafffffffff6666666a9911666666aa888888888888aaaaaaaaffffffff66666aaa99aaaaaaaaaaaaaaa999999999999999999999999
            99999999999999999999999666666aaa999999999999991faaaaaafffffffff6666666a19116666666aaaaaaaaaaaaaaaaaaaaaffffffff666666aaaaaaaaaaaaaaaaaa9999999999999999999999999
            99999999999999999999999666666aaa999999999999991aaaaaaaffffffff18666666a8191666666666aaaaaaaaaaaaaaaaaaaffffffff6666666aaaaaaaaaaaaaaaa99999999999999999999999999
            999999999999999999999996666666aa999999999999991aaaaaaaffffffff18666666681911666666666666666666666666aaaffffffff66666666666aaaaaaaaaaa999999999999999999999999999
            999999999999999999999999666666aa99999999999999aaaaaaaafffffffff19666666819916666666666666666666666666afffffffff6666666666666666666a99999999999999999999999999999
            999999999999999999999999666666aa999999999999aaaaaaaaafffffffffff1666666881196666666666666666666666666fffffffffff666666666666666666999999999999999999999999999999
            9999999999999999999999996666666a9999999999aaaaaaaaaaffffffffffff16666668888111666666666666666666666666ffffffffff666666666666666666999999999999999999999999999999
            9999999999999999999999999666666a99999999aaaaaaaaaaaaffffffffffff11666668888888886666666666666666666666ffffffffff666666666666666666999999999999999999999999999999
            9999999999999999999999999666666a99999aaaaaaaaaaaaaafffffffffffff1866666188888888888666666661fff6666666ffffffffff666666666666666666699999999999999999999999999999
            99999999999999999999999996666666999aaaaaaaaaaaaaaaffffffffffffffff666669188888888816666666681fff666666fffffffffff66666999966666666699999999999999999999999999999
            99999999999999999999999999666666aaaaaaaaaaaaaaaaffffffffffffffffff666661188888888191666666168fff666666fffffffffff66666999996666666669999999999999999999999999999
            99999999999999999999999999666666aaaaaaaaaaaaaa1ffffffffffffffffffff1811888888888199166666681181ff66666fffffffffff66666999999966666669999999999999999999999999999
            99999999999999999999999999666666aaaaaaaaaaaa991ffffffffffffffffffff6666688888888819966666681f11ff66666ffffffffffffff19999999966666669999999999999999999999999999
            9999999999999999999999999996666666666aaaa999991ffffffffffffffffffff66666888888881619666666811ffff66666ffffffffffffff19999999996666669999999999999999999999999999
            9999999999999999999999999996666666666aa999999991fffffffffffffffff66666668888881161616666668161fffffffffffffffffffff199999999996666669999999999999999999999999999
            999999999999999999999999999666666666699999999991fffffffffffffffff66666668888116161618888881681fffffffffffffffffffff199999999996666669999999999999999999999999999
            999999999999999999999999999666666666699999999991fffffffffffffffff6666666811181661661888881811fffffffffffffffffffff6666699999996666669999999999999999999999999999
            9999999999999999999999999996666666666999999999991ffffffffffffffff66666661661981166188888811fffffffffffffffffffffff6666699999996666669999999999999999999999999999
            9999999999999999999999999996666666666999999999991ffffffffffffffff6666666616611661188886666611fffffffffffffffffffff6666699999996666669999999999999999999999999999
            9999999999999999999999999999666666666999999999991ffffffffffffffff6666661661161618888886666681fffffffffffffffffffff6666699999999999999999999999999999999999999999
            99999999999999999999999999996666666699999999999991ffffffffffffffffffff1111661618888888666661fffff66666fffffffffff16666699999999999999999999999999999999999999999
            99999999999999999999999999996666666699999999999991ffffffffffffffffffff1616161188888888666661ffff666666fffffffffff16666699999999999999999999999999999999999999999
            999999999999999999999999999996666669999999999999991ffffffffffffffffffff16111888888881166666611116666666fffffffff199999999999999999999999999999999999999999999999
            999999999999999999999999999996666669999999999999991fffffffffffffffffffff188888888881f188111181116666666fffffffff199999999999999666666999999999999999999999999999
            9999999999999999999999999999966666699999999999999991ffffffffffffffffffff18888888881fff1166681c116666666ffffffff1999999999999996666666999999999999999999999999999
            99999999999999999999999999999666669999999999999999991fffffffffffffffffff1888888881ffff16688111c166666661ffffff19999999999999996666666999999999999999999999999999
            99999999999999999999999999999999999999999999999999991ffffffffffffffffffff18888811fff1118811661cc666666611fffff19999999999999996666666999999999999999999999999999
            999999999999999999999999999999999999999999999999999991ffffffffffffffffffff11111fff11111111861ccc6666666111fff199999999999999996666666999999999999999999999999999
            9999999999999999999999999999999999999999999999999999991fffffffffffffffffffffffffff11111c18611ccc6666666111ff1999999999999999996666666999999999999999999999999999
            99999999999999999999999999999999999999999999999999999991fffffffffffffffffffffffff11111c1661cccc16666666111119999999999999999999999999999999999999999999999999999
            999999999999999999999999999966666999999999999999999999991ffffffffffffffffffffffff11111cc11ccccc16666666111199999999999999999999999999999999999999999999999999999
            9999999999999999999999999999666669999999999999999999999991ffffffffffffffffffffff111111cccccccc111666661111999999999999999999999999999999999999999999999999999999
            99999999999999999999999999996666669999999999999999999999991fffffffffffffffffffff1111111cccccc1111666661119999999999999999999999999999999999999999999999999999999
            999999999999999999999999999966666699999999999999999999999991ffffffffffffffffffff11111111ccc111111666661199999999999999999999999999999999999999999999999999999999
            99999999999999999999999999996666669999999999999999999999999911ffffffffffffffffff11111111111111111666661999999999999999999999999999999999999999999999999999999999
            999999999999999999999999999966666699999999999999999999999999991fffffffffffffffff11111111111111111111199999999999999999999999999999999999999999999999999999999999
            99999999999999999999999999996666669999999999999999999999999999911fffffffffffffff11111111111111111111999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999666666999999999999999999999999999999911fffffffffffff11111111111111111199999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999666666999999999999999999999999999999999111ffffffffff11111111111111119999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999666666999999999999999999999999999999999999111fffffff11111111111119999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999666666999999999999999999999999999999999999999111111111111111119999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            """))
        pause(500)
    game.set_dialog_frame(assets.image("""
        trasparent text
        """))
    game.set_dialog_cursor(assets.image("""
        statistic text
        """))
    game.show_long_text("", DialogLayout.BOTTOM)
    game.set_dialog_cursor(assets.image("""
        continue text
        """))
    game.set_dialog_frame(assets.image("""
        text 2
        """))
    game.set_dialog_text_color(1)
    tiles.load_map(tiles.create_small_map(tilemap("""
        level4
        """)))
    _0 = sprites.create(assets.image("""
        White
        """), SpriteKind.a2)
    monster.destroy()
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_on_overlap6(sprite2, otherSprite2):
    global frequenza, kill, reload_bar
    otherSprite2.destroy(effects.spray, 500)
    frequenza += -30
    kill += 1
    reload_bar += 1
    statusbar2.value += 1
    music.pew_pew.play()
sprites.on_overlap(SpriteKind.bullet, SpriteKind.enemy2, on_on_overlap6)

def on_on_overlap7(sprite10, otherSprite6):
    otherSprite6.destroy(effects.spray, 500)
    statusbar.value += 2
sprites.on_overlap(SpriteKind.bullet, SpriteKind.Food2_0, on_on_overlap7)

def on_on_overlap8(sprite3, otherSprite3):
    tiles.place_on_random_tile(sprite3, assets.tile("""
        myTile
        """))
sprites.on_overlap(SpriteKind.food, SpriteKind.Food2_0, on_on_overlap8)

def old_codes():
    # beta
    scene.set_background_image(assets.image("""
        Background begin
        """))
    animation.run_image_animation(cure, assets.animation("""
        Cure 2
        """), 100, False)
    cure.set_kind(SpriteKind.Food2_0)
    if GAME == 1:
        if reload_bar == 0:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 6 6 6 6 6 f . . .
                    . . f 6 6 f f f f f f f 6 6 f . .
                    . f 6 6 f . . . . . . . f 6 6 f .
                    f 6 6 f . . . . . . . . . f 6 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 6 f . . . . . . . . . f 6 6 f
                    . f 6 6 f . . . . . . . f 6 6 f .
                    . . f 6 6 f f f f f f f 6 6 f . .
                    . . . f 6 6 6 6 6 6 6 6 6 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 1:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 6 6 6 f . . .
                    . . f 6 6 f f f f f f f 6 6 f . .
                    . f 6 6 f . . . . . . . f 6 6 f .
                    f 6 6 f . . . . . . . . . f 6 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 6 f . . . . . . . . . f 6 6 f
                    . f 6 6 f . . . . . . . f 6 6 f .
                    . . f 6 6 f f f f f f f 6 6 f . .
                    . . . f 6 6 6 6 6 6 6 6 6 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 1:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 6 6 f . . . . . . . . . f 7 7 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 f . . . . . . . . . . . f 6 f
                    f 6 6 f . . . . . . . . . f 6 6 f
                    . f 6 6 f . . . . . . . f 6 6 f .
                    . . f 6 6 f f f f f f f 6 6 f . .
                    . . . f 6 6 6 6 6 6 6 6 6 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 8:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 6 6 f . . . . . . . . . f 7 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 6 f . . . . . . . . . f 6 7 f
                    . f 6 6 f . . . . . . . f 6 6 f .
                    . . f 6 6 f f f f f f f 6 6 f . .
                    . . . f 6 6 6 6 6 6 6 6 6 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 12:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 6 6 f . . . . . . . . . f 7 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 6 f . . . . . . . . . f 7 7 f
                    . f 6 6 f . . . . . . . f 7 7 f .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . . . f 6 6 6 6 6 6 6 7 7 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 16:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 6 6 f . . . . . . . . . f 7 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 6 f . . . . . . . . . f 7 7 f
                    . f 6 6 f . . . . . . . f 7 7 f .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 21:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 6 6 f . . . . . . . . . f 7 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 6 f . . . . . . . . . f 7 7 f
                    . f 6 6 f . . . . . . . f 7 7 f .
                    . . f 6 7 f f f f f f f 7 7 f . .
                    . . . f 7 7 7 7 7 7 7 7 7 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 26:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 6 6 f . . . . . . . . . f 7 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 7 f . . . . . . . . . f 7 7 f
                    . f 7 7 f . . . . . . . f 7 7 f .
                    . . f 7 7 f f f f f f f 7 7 f . .
                    . . . f 7 7 7 7 7 7 7 7 7 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 30:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 6 6 f . . . . . . . . . f 7 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 6 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 7 f . . . . . . . . . f 7 7 f
                    . f 7 7 f . . . . . . . f 7 7 f .
                    . . f 7 7 f f f f f f f 7 7 f . .
                    . . . f 7 7 7 7 7 7 7 7 7 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 35:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 6 6 6 6 7 7 7 7 7 f . . .
                    . . f 6 6 f f f f f f f 7 7 f . .
                    . f 6 6 f . . . . . . . f 7 7 f .
                    f 7 6 f . . . . . . . . . f 7 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 7 f . . . . . . . . . f 7 7 f
                    . f 7 7 f . . . . . . . f 7 7 f .
                    . . f 7 7 f f f f f f f 7 7 f . .
                    . . . f 7 7 7 7 7 7 7 7 7 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)
        elif reload_bar == 40:
            animation.run_image_animation(reload,
                [img("""
                    . . . . f f f f f f f f f . . . .
                    . . . f 7 7 7 7 7 7 7 7 7 f . . .
                    . . f 7 7 f f f f f f f 7 7 f . .
                    . f 7 7 f . . . . . . . f 7 7 f .
                    f 7 7 f . . . . . . . . . f 7 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 f . . . . . . . . . . . f 7 f
                    f 7 7 f . . . . . . . . . f 7 7 f
                    . f 7 7 f . . . . . . . f 7 7 f .
                    . . f 7 7 f f f f f f f 7 7 f . .
                    . . . f 7 7 7 7 7 7 7 7 7 f . . .
                    . . . . f f f f f f f f f . . . .
                    """)],
                100,
                False)

def on_on_overlap9(sprite152, otherSprite102):
    global GAME, _return, _3, _2, statusbar3, Credits
    if controller.A.is_pressed() or controller.B.is_pressed():
        GAME = 5
        italian.set_flag(SpriteFlag.GHOST, True)
        italian.set_flag(SpriteFlag.INVISIBLE, True)
        English.set_flag(SpriteFlag.GHOST, True)
        English.set_flag(SpriteFlag.INVISIBLE, True)
        impo.set_flag(SpriteFlag.GHOST, True)
        impo.set_flag(SpriteFlag.INVISIBLE, True)
        scene.set_background_image(img("""
            222222222222222222224fff22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224fff22222222222222222222
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffff224ff224f222224f224f224f224f224fffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffff22242224f224ffff2224224f224f224fffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffff22222224f2224fff2222224f224f224fffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffff22424224f22444ff2242224f2244224fffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffff224ff224f222224f224f224f2222224fffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffff224f224f2222224f224ffff224f224f224ff224f222224ffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffff224f224f224f224f224ffff224f224f22242224f224fffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffff2222224f224f224f224ffff224f224f22222224f2224ffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24ffffffffffffffffffffffffffffffff22224ff2244224f22444ff2244224f22424224f22444fffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffff224fff2222224f222224f2222224f224ff224f222224ffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            244444444444444444424fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24444444444444444442
            222222222222222222224fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff22222222222222222222
            ffffffffffffffffffffffff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fffffffffffffffffffffff
            ffffffffffffffffffffffff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fffffffffffffffffffffff
            ffffffffffffffffffffffff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fffffffffffffffffffffff
            444444444444444444444fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff44444444444444444444
            222222222222222222224fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff22222222222222222222
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            244444444444444444424fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24444444444444444442
            222222222222222222224fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff22222222222222222222
            ffffffffffffffffffffffff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fffffffffffffffffffffff
            ffffffffffffffffffffffff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fffffffffffffffffffffff
            ffffffffffffffffffffffff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fffffffffffffffffffffff
            444444444444444444444fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff44444444444444444444
            222222222222222222224fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff22222222222222222222
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
            244444444444444444424fff24444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444424fff24444444444444444442
            222222222222222222224fff22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224fff22222222222222222222
            """))
        _return = sprites.create(img("""
                bbbbbbbbbbbbbbb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bffff4ffffffffb
                bfff424fffffffb
                bff42244444fffb
                bf4222222224ffb
                bff4224444224fb
                bfff424fff424fb
                bffff4ffff424fb
                bfffffffff424fb
                bfffffffff424fb
                bfffffffff424fb
                bfffffffff424fb
                bffffffffff4ffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bfffffffffffffb
                bbbbbbbbbbbbbbb
                """),
            SpriteKind.undo)
        _return.set_position(11, 16)
        _3 = sprites.create(img("""
                4 4 4 4 4 4 4
                4 2 2 2 2 2 4
                4 2 2 4 2 2 4
                4 2 4 4 4 2 4
                4 2 2 4 2 2 4
                4 2 2 2 2 2 4
                4 4 4 4 4 4 4
                """),
            SpriteKind.plus)
        _3.set_position(110, 40)
        _2 = sprites.create(img("""
                4 4 4 4 4 4 4
                4 2 2 2 2 2 4
                4 2 2 2 2 2 4
                4 2 4 4 4 2 4
                4 2 2 2 2 2 4
                4 2 2 2 2 2 4
                4 4 4 4 4 4 4
                """),
            SpriteKind.minus)
        _2.set_position(50, 40)
        statusbar3 = statusbars.create(51, 9, StatusBarKind.volume)
        statusbar3.set_position(80, 40)
        statusbar3.set_color(2, 4, 4)
        statusbar3.set_bar_border(1, 4)
        statusbar3.max = 255
        statusbar3.z = -1
        Credits = sprites.create(img("""
                ..44444444444444444444444444444444444444444444444...
                .4222222222222222222222222222222222222222222222224..
                42fffffffffffffffffffffffffffffffffffffffffffffff24.
                2ff222224f222224f222224f22224ff224f2222224f42222ff24
                2ff224ffff224f24f224ffff224224f224f2222224f2244fff24
                2ff224ffff224424f2222fff224424f224fff224ffff2224ff24
                2ff22444ff22224ff22444ff224224f224fff224fff44422ff24
                2ff222224f224f24f222224f22224ff224fff224fff22224ff24
                .2fffffffffffffffffffffffffffffffffffffffffffffff24.
                ..222222222222222222222222222222222222222222222224..
                """),
            SpriteKind.credits_button)
        Credits.set_position(80, 105)
sprites.on_overlap(SpriteKind.bullet, SpriteKind.impstazioni, on_on_overlap9)

def on_overlap_tile5(sprite7, location4):
    sprite7.destroy()
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile8
        """),
    on_overlap_tile5)

def on_on_overlap10(sprite16, otherSprite11):
    global frequenza, kill, reload_bar
    otherSprite11.destroy(effects.spray, 500)
    frequenza += -30
    kill += 1
    reload_bar += 1
    music.set_volume(volu)
    music.pew_pew.play()
    statusbar2.value += 1
sprites.on_overlap(SpriteKind.bullet, SpriteKind.enemy, on_on_overlap10)

def on_on_overlap11(sprite8, otherSprite4):
    global explosion, num_eplosions
    if controller.A.is_pressed():
        if statusbar2.value >= 40:
            if explosion == 1:
                explosion = 2
                statusbar2.value = 0
                statusbar2.set_color(6, 0, 0)
                music.set_volume(volu)
                music.buzzer.play()
                num_eplosions += 1
    elif controller.B.is_pressed():
        if statusbar2.value >= 40:
            if explosion == 1:
                explosion = 2
                statusbar2.value = 0
                statusbar2.set_color(6, 0, 0)
                music.set_volume(volu)
                music.buzzer.play()
                num_eplosions += 1
sprites.on_overlap(SpriteKind.a1, SpriteKind.projectile, on_on_overlap11)

def on_b_released():
    global volu
    if GAME == 5:
        if Bullet_.overlaps_with(_2):
            volu += -25.5
            music.knock.play()
        elif Bullet_.overlaps_with(_3):
            volu += 25.5
            music.knock.play()
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def on_on_overlap12(sprite13, otherSprite8):
    sprite13.destroy()
    brain.start_effect(effects.ashes, 500)
    music.small_crash.play()
    statusbar.value += -1
sprites.on_overlap(SpriteKind.enemy2, SpriteKind.projectile, on_on_overlap12)

def color_ingame():
    color.set_palette(color.original_palette)
    color.set_color(4, color.rgb(220, 70, 0))
    color.set_color(7, color.rgb(0, 200, 0))
    color.set_color(2, color.rgb(204, 0, 0))
    color.set_color(3, color.rgb(204, 0, 0))
    color.set_color(8, color.rgb(0, 0, 153))
    color.set_color(6, color.rgb(0, 102, 0))
    color.set_color(7, color.rgb(220, 70, 0))
    color.set_color(3, color.rgb(255, 153, 204))
    color.set_color(6, color.rgb(120, 120, 120))
    color.set_color(7, color.rgb(0, 200, 0))
    color.set_color(11, color.rgb(192, 192, 192))
def fade_color_ingame():
    color.set_palette(color.original_palette)
    color.set_color(5, color.rgb(255, 200, 0))
    color.set_color(4, color.rgb(220, 70, 0))
    color.set_color(2, color.rgb(204, 0, 0))
    color.set_color(3, color.rgb(204, 0, 0))
    color.set_color(8, color.rgb(0, 0, 153))
    color.set_color(3, color.rgb(255, 153, 204))
    color.set_color(6, color.rgb(120, 120, 120))
    color.set_color(7, color.rgb(0, 200, 0))
    color.set_color(11, color.rgb(192, 192, 192))
def start():
    global GAME, frequenza, frequenza20, kill, brain, statusbar, life_brain, Bullet_, limit
    color.set_color(3, color.rgb(204, 0, 0))
    GAME = 1
    frequenza = 3000
    frequenza20 = 3000
    kill = 0
    info.set_score(kill)
    info.player2.set_score(frequenza)
    brain = sprites.create(assets.image("""
        brain
        """), SpriteKind.projectile)
    statusbar = statusbars.create(21, 5, StatusBarKind.health)
    statusbar.set_color(7, 2, 6)
    statusbar.set_bar_border(1, 15)
    statusbar.attach_to_sprite(brain, -20, 0)
    statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    color.set_color(7, color.rgb(220, 70, 0))
    if linguage == 2:
        life_brain = game.ask_for_number("Select life (1-9)", 1)
    else:
        life_brain = game.ask_for_number("Seleziona vita (1-9)", 1)
    Bullet_ = sprites.create(assets.image("""
        bullet
        """), SpriteKind.bullet)
    controller.move_sprite(Bullet_, 100, 100)
    Bullet_.set_stay_in_screen(True)
    scene.set_background_image(assets.image("""
        Trasparent Background
        """))
    color.set_color(3, color.rgb(255, 153, 204))
    color.set_color(6, color.rgb(120, 120, 120))
    color.set_color(7, color.rgb(0, 200, 0))
    color.set_color(11, color.rgb(192, 192, 192))
    limit = life_brain
    statusbar.max = life_brain * 2
    tiles.set_tilemap(tilemap("""
        level2
        """))

def on_a_released():
    global volu
    if GAME == 5:
        if Bullet_.overlaps_with(_2):
            volu += -25.5
            music.knock.play()
        elif Bullet_.overlaps_with(_3):
            volu += 25.5
            music.knock.play()
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_on_overlap13(sprite153, otherSprite103):
    global GAME
    if controller.A.is_pressed() or controller.B.is_pressed():
        GAME = 0
        italian.set_flag(SpriteFlag.GHOST, False)
        italian.set_flag(SpriteFlag.INVISIBLE, False)
        English.set_flag(SpriteFlag.GHOST, False)
        English.set_flag(SpriteFlag.INVISIBLE, False)
        impo.set_flag(SpriteFlag.GHOST, False)
        impo.set_flag(SpriteFlag.INVISIBLE, False)
        scene.set_background_image(assets.image("""
            language text
            """))
        _return.destroy()
        _2.destroy()
        _3.destroy()
        statusbar3.destroy()
        Credits.destroy()
sprites.on_overlap(SpriteKind.bullet, SpriteKind.undo, on_on_overlap13)

def on_on_overlap14(sprite154, otherSprite104):
    global meno_tempo, linguage, _1, frequenza, frequenza20, kill, ombra, copristatus2, statusbar2, life_brain, difficulty, fade, limit
    if controller.A.is_pressed() or controller.B.is_pressed():
        meno_tempo = game.runtime() / 1000
        italian.destroy()
        English.destroy()
        game.set_dialog_frame(assets.image("""
            text 3
            """))
        game.show_long_text("Use the \"WASD\" keys to move the bullet and hit all the monsters",
            DialogLayout.FULL)
        game.set_dialog_frame(assets.image("""
            trasparent
            """))
        linguage = 2
        music.stop_all_sounds()
        music.set_volume(volu)
        _1 = sprites.create(assets.image("""
            black
            """), SpriteKind.a1)
        _1.set_flag(SpriteFlag.INVISIBLE, True)
        frequenza = 3000
        frequenza20 = 3000
        kill = 0
        ombra = sprites.create(img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffff....................................................................................................................ffffffffffffffffffffff
                ffffffffffffffff................................................................................................................................ffffffffffffffff
                fffffffffffff......................................................................................................................................fffffffffffff
                ffffffffff............................................................................................................................................ffffffffff
                ffffffff................................................................................................................................................ffffffff
                ffffff....................................................................................................................................................ffffff
                fffff......................................................................................................................................................fffff
                ffff........................................................................................................................................................ffff
                ffff........................................................................................................................................................ffff
                fff..........................................................................................................................................................fff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                f..............................................................................................................................................................f
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff............................................................................................................................................................ff
                ff...........................................................................................................................................................fff
                ff..........................................................................................................................................................ffff
                ff..........................................................................................................................................................ffff
                ff.........................................................................................................................................................fffff
                ff........................................................................................................................................................ffffff
                ff......................................................................................................................................................ffffffff
                ff....................................................................................................................................................ffffffffff
                ff.................................................................................................................................................fffffffffffff
                ff..............ffffff..........................................................................................................................ffffffffffffffff
                ff..............ffffff....................................................................................................................ffffffffffffffffffffff
                fff............fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffff..........ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            SpriteKind.shadow)
        ombra.set_position(80, 60)
        ombra.z = 99999999
        copristatus2 = sprites.create(img("""
                fffff...........ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            SpriteKind.shadow)
        copristatus2.z = 100000009
        copristatus2.set_position(80, 117)
        statusbar2 = statusbars.create(160, 4, StatusBarKind.magic)
        statusbar2.set_color(6, 0, 0)
        statusbar2.max = 40
        statusbar2.value = 0
        statusbar2.set_position(80, 117)
        statusbar2.z = 100000000
        color.set_color(7, color.rgb(220, 70, 0))
        if story.check_last_answer("          EASY"):
            life_brain = 8
            difficulty = 1
        elif story.check_last_answer("         MEDIUM"):
            life_brain = 5
            difficulty = 2
        elif story.check_last_answer("         HARDER"):
            life_brain = 3
            difficulty = 3
        elif story.check_last_answer("       IMPOSSIBLE"):
            life_brain = 0.5
            difficulty = 4
        color.set_color(3, color.rgb(255, 153, 204))
        color.fade_to_black.start_screen_effect(500)
        music.spooky.play()
        fade = 1
        scene.set_background_image(assets.image("""
            trasp backgrond
            """))
        color.set_color(5, color.rgb(255, 200, 0))
        color.set_color(3, color.rgb(255, 153, 204))
        color.set_color(6, color.rgb(120, 120, 120))
        color.set_color(7, color.rgb(0, 200, 0))
        color.set_color(11, color.rgb(192, 192, 192))
        limit = life_brain
sprites.on_overlap(SpriteKind.bullet, SpriteKind.ing, on_on_overlap14)

def on_overlap_tile6(sprite18, location6):
    sprite18.destroy()
scene.on_overlap_tile(SpriteKind.food,
    assets.tile("""
        myTile8
        """),
    on_overlap_tile6)

bomb: Sprite = None
skeletron: Sprite = None
Credits: Sprite = None
statusbar3: StatusBarSprite = None
_2: Sprite = None
_3: Sprite = None
_return: Sprite = None
cure: Sprite = None
reload_bar = 0
reload: Sprite = None
_0: Sprite = None
monster: Sprite = None
black2: Sprite = None
brain: Sprite = None
statusbar: StatusBarSprite = None
limit = 0
fade = 0
life_brain = 0
statusbar2: StatusBarSprite = None
copristatus2: Sprite = None
ombra: Sprite = None
kill = 0
frequenza20 = 0
frequenza = 0
_1: Sprite = None
Bullet_: Sprite = None
English: Sprite = None
italian: Sprite = None
impo: Sprite = None
volu = 0
num_eplosions = 0
explosion = 0
multic = 0
GAME = 0
linguage = 0
meno_tempo = 0
difficulty = 0
if not (blockSettings.exists("n")):
    blockSettings.write_string("n", game.ask_for_string("name?", 3))
    story.show_player_choices("italiano", "english")
    blockSettings.write_string("l", story.get_last_answer())
music.sonar.play()
music.spooky.play()
difficulty = 0
meno_tempo = 0
linguage = 0
GAME = 0
menu = 0
multic = 0
explosion = 0
num_eplosions = 0
volu = 25.5
color.set_color(5, color.rgb(255, 200, 0))
color.set_color(4, color.rgb(220, 70, 0))
color.set_color(7, color.rgb(0, 200, 0))
color.set_color(2, color.rgb(204, 0, 0))
color.set_color(3, color.rgb(204, 0, 0))
color.set_color(8, color.rgb(0, 0, 153))
color.set_color(6, color.rgb(0, 102, 0))
scene.set_background_image(assets.image("""
    Backgrond not beta
    """))
game.set_dialog_text_color(1)
game.set_dialog_frame(assets.image("""
    trasparent 3
    """))
game.set_dialog_cursor(assets.image("""
    continue text 2
    """))
game.show_long_text("", DialogLayout.BOTTOM)
scene.set_background_image(img("""
    222222222222222222224fff22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224fff22222222222222222222
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff224fffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222224fffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2224f2224ffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff224ff4224ffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff4224fffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff42224fffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffff22224ff224f222224f222224f224f222224f224f224f224fff2222224f2244224ffff2224ffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffff224224f224f224ffff224ffff224f224ffff224f224f224fff2222224f2222224ffff224fffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffff224424f224f2244fff2244fff224f224ffff224f224f224fffff224fffff224ffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffff224224f224f22224ff22224ff224f22444ff2244224f22444fff224fffff224ffffff224fffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24ffffffffffffffffff22224ff224f224ffff224ffff224f222224f2222224f22224fff224fffff224ffffff224fffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    244444444444444444424fff24444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444424fff24444444444444444442
    222222222222222222224fff22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224fff22222222222222222222
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    444444444444444444444fff44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444fff44444444444444444444
    222222222222222222224fff22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224fff22222222222222222222
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    24fffffffffffffffff24fff24fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff24fff24fffffffffffffffff2
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    """))
story.show_player_choices("          EASY",
    "         MEDIUM",
    "         HARDER",
    "       IMPOSSIBLE")
impo = sprites.create(img("""
        bbbbbbbbbbbbbbb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfff4f444f4fffb
        bff424222424ffb
        bf42222222224fb
        bff422444224ffb
        bf4224fff4224fb
        bf4224fff4224fb
        bf4224fff4224fb
        bff422444224ffb
        bf42222222224fb
        bff424222424ffb
        bfff4f444f4fffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bfffffffffffffb
        bbbbbbbbbbbbbbb
        """),
    SpriteKind.impstazioni)
impo.set_position(151, 16)
italian = sprites.create(assets.image("""
    italian
    """), SpriteKind.ita)
English = sprites.create(assets.image("""
    english
    """), SpriteKind.ing)
Bullet_ = sprites.create(assets.image("""
    Bullet
    """), SpriteKind.bullet)
Bullet_.z = 999999999
controller.move_sprite(Bullet_, 75, 75)
Bullet_.set_stay_in_screen(True)
scene.set_background_image(assets.image("""
    language text
    """))

def on_forever():
    global cure
    if GAME == 1:
        if brain.tile_kind_at(TileDirection.CENTER, assets.tile("""
            myTile10
            """)):
            if frequenza < 3000:
                pause(frequenza * 3)
                if GAME == 1:
                    cure = sprites.create(assets.image("""
                        cure
                        """), SpriteKind.food)
                    tiles.place_on_random_tile(cure, assets.tile("""
                        myTile
                        """))
                    cure.start_effect(effects.bubbles, 500)
forever(on_forever)

def on_forever2():
    global skeletron, frequenza20, frequenza
    if GAME == 1:
        if brain.tile_kind_at(TileDirection.CENTER, assets.tile("""
            myTile10
            """)):
            if frequenza < 2500:
                pause(frequenza20)
                if GAME == 1:
                    skeletron = sprites.create(assets.image("""
                        skeletron
                        """), SpriteKind.enemy2)
                    tiles.place_on_random_tile(skeletron, assets.tile("""
                        myTile11
                        """))
                    skeletron.follow(brain, 25)
                    skeletron.start_effect(effects.spray, 500)
                frequenza20 = frequenza20 - 30
                if skeletron.x < 80:
                    if multic == 0:
                        animation.run_image_animation(skeletron,
                            [img("""
                                    . . f f f f f f f f . . . .
                                    . f b b 1 1 1 1 1 1 f . . .
                                    f b b 1 1 1 1 1 1 1 1 f . .
                                    f b 1 1 f 1 1 1 f 1 1 f . .
                                    f b 1 f f f 1 f f f 1 f . .
                                    f b 1 f f f 1 f f f 1 f . .
                                    f b 1 1 1 1 1 1 1 1 1 f . .
                                    f b 1 1 1 1 1 1 1 1 1 f . .
                                    . f f f b f 1 f 1 f f . . .
                                    . . f f f f f f f f f f f .
                                    . f b 1 1 f 1 1 1 f b 1 1 f
                                    . . f f f 1 1 1 1 f f f f .
                                    . . . f 1 1 1 1 f . . . . .
                                    . . . f f 1 1 f f . . . . .
                                    . . f b 1 1 1 1 1 f . . . .
                                    . . . f f 1 1 f f . . . . .
                                    . . f b 1 f f b 1 f . . . .
                                    . . . f f . . f f . . . . .
                                    """),
                                img("""
                                    . . . . . . . . . . . . . .
                                    . . f f f f f f f f . . . .
                                    . f b b 1 1 1 1 1 1 f . . .
                                    f b b 1 1 1 1 1 1 1 1 f . .
                                    f b 1 1 f 1 1 1 f 1 1 f . .
                                    f b 1 f f f 1 f f f 1 f . .
                                    f b 1 f f f 1 f f f 1 f . .
                                    f b 1 1 1 1 1 1 1 1 1 f . .
                                    f b 1 1 1 1 1 1 1 1 1 f . .
                                    . f f f b f 1 f 1 f f . . .
                                    . . f f f f f f f f f f f .
                                    . f b 1 1 f 1 1 1 f b 1 1 f
                                    . . f f f 1 1 1 1 f f f f .
                                    . . . f 1 1 1 1 f . . . . .
                                    . . . f f 1 1 f f f f . . .
                                    . . f b 1 1 1 1 1 1 1 f . .
                                    . f b 1 f f f f f b 1 f . .
                                    . f f f . . . . . f f . . .
                                    """)],
                            300,
                            True)
                    else:
                        animation.run_image_animation(skeletron,
                            assets.animation("""
                                animation sk 1
                                """),
                            300,
                            True)
                if skeletron.x > 80:
                    if multic == 0:
                        animation.run_image_animation(skeletron,
                            assets.animation("""
                                animation sk 2
                                """),
                            300,
                            True)
                    else:
                        animation.run_image_animation(skeletron,
                            [img("""
                                    . . . . f f f f f f f f . .
                                    . . . f 5 5 5 f 5 5 4 4 f .
                                    . . f 5 5 5 5 f f 5 5 4 4 f
                                    . . f 5 5 f 5 5 f f 5 5 4 f
                                    . . f 5 f f f 5 f f f 5 4 f
                                    . . f 5 f f f 5 f f f f 4 f
                                    . . f 5 5 5 5 5 5 5 5 f f f
                                    . . f 5 5 5 5 5 5 5 5 5 f f
                                    . . . f f 5 f 5 f 4 f f f .
                                    . f f f f f f f f f f f . .
                                    f 5 5 4 f 5 5 5 f 5 5 4 f .
                                    . f f f f 5 5 5 5 f f f . .
                                    . . . . . f 5 5 5 5 f . . .
                                    . . . . . f f 5 5 f f . . .
                                    . . . . f 5 5 5 5 5 4 f . .
                                    . . . . . f f 5 5 f f . . .
                                    . . . . f 5 4 f f 5 4 f . .
                                    . . . . . f f . . f f . . .
                                    """),
                                img("""
                                    . . . . . . . . . . . . . .
                                    . . . . f f f f f f f f . .
                                    . . . f 5 5 5 f 5 5 4 4 f .
                                    . . f 5 5 5 5 f f 5 5 4 4 f
                                    . . f 5 5 f 5 5 f f 5 5 4 f
                                    . . f 5 f f f 5 f f f 5 4 f
                                    . . f 5 f f f 5 f f f f 4 f
                                    . . f 5 5 5 5 5 5 5 5 f f f
                                    . . f 5 5 5 5 5 5 5 5 5 f f
                                    . . . f f 5 f 5 f 4 f f f .
                                    . f f f f f f f f f f f . .
                                    f 5 5 4 f 5 5 5 f 5 5 4 f .
                                    . f f f f 5 5 5 5 f f f . .
                                    . . . . . f 5 5 5 5 f . . .
                                    . . . f f f f 5 5 f f . . .
                                    . . f 5 5 5 5 5 5 5 4 f . .
                                    . . f 5 4 f f f f f 5 4 f .
                                    . . . f f . . . . . f f f .
                                    """)],
                            300,
                            True)
        if frequenza < 600:
            frequenza = frequenza + 30
        if frequenza20 < 600:
            frequenza20 = frequenza20 + 30
forever(on_forever2)

def on_forever3():
    if GAME == 1:
        if kill == 0:
            music.set_volume(0)
            music.stop_all_sounds()
        else:
            music.set_volume(volu)
forever(on_forever3)

def on_forever4():
    global monster, frequenza
    if GAME == 1:
        if brain.tile_kind_at(TileDirection.CENTER, assets.tile("""
            myTile10
            """)):
            if frequenza < 3001:
                pause(frequenza)
                if GAME == 1:
                    monster = sprites.create(assets.image("""
                        zombie 3
                        """), SpriteKind.enemy)
                    tiles.place_on_random_tile(monster, assets.tile("""
                        myTile11
                        """))
                    monster.follow(brain, 9)
                    monster.start_effect(effects.spray, 500)
                    Zombie_animation()
        music.thump.play()
        if frequenza < 600:
            frequenza = frequenza + 30
forever(on_forever4)

def on_forever5():
    global life_brain
    if limit != life_brain:
        life_brain = limit
forever(on_forever5)

def on_forever6():
    global fade, GAME, brain, reload, statusbar
    if fade == 1:
        Bullet_.set_position(80, 60)
        fade = 0
        pause(1000)
        GAME += 1
        fade_color_ingame()
        brain = sprites.create(assets.image("""
            brain 3
            """), SpriteKind.projectile)
        brain.z = 99999999999
        reload = sprites.create(img("""
                . . . . f f f f f f f f f . . . .
                . . . f 6 6 6 6 6 6 6 6 6 f . . .
                . . f 6 6 f f f f f f f 6 6 f . .
                . f 6 6 f . . . . . . . f 6 6 f .
                f 6 6 f . . . . . . . . . f 6 6 f
                f 6 f . . . . . . . . . . . f 6 f
                f 6 f . . . . . . . . . . . f 6 f
                f 6 f . . . . . . . . . . . f 6 f
                f 6 f . . . . . . . . . . . f 6 f
                f 6 f . . . . . . . . . . . f 6 f
                f 6 f . . . . . . . . . . . f 6 f
                f 6 f . . . . . . . . . . . f 6 f
                f 6 6 f . . . . . . . . . f 6 6 f
                . f 6 6 f . . . . . . . f 6 6 f .
                . . f 6 6 f f f f f f f 6 6 f . .
                . . . f 6 6 6 6 6 6 6 6 6 f . . .
                . . . . f f f f f f f f f . . . .
                """),
            SpriteKind.player)
        reload.z = 9999999999
        reload.set_position(10, 110)
        statusbar = statusbars.create(21, 5, StatusBarKind.health)
        statusbar.set_color(7, 2, 6)
        statusbar.set_bar_border(1, 15)
        statusbar.attach_to_sprite(brain, -20, 0)
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
        tiles.set_tilemap(tilemap("""
            level2
            """))
        statusbar.max = life_brain * 2
forever(on_forever6)

def on_forever7():
    global explosion
    if explosion == 2:
        for index in range(2):
            bomb.follow(brain, 100)
            bomb.ay = -100
            bomb.ax = 100
            bomb.z = 99999999999999
            scaling.scale_by_percent(bomb, 200, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
            pause(1000)
            scene.camera_shake(1, 200)
        music.zapped.play()
        music.sonar.play()
        music.spooky.play()
        explosion = 0
        bomb.destroy(effects.fire, 500)
        scene.camera_shake(3, 500)
forever(on_forever7)

def on_forever8():
    global monster, frequenza
    if GAME == 1:
        if brain.tile_kind_at(TileDirection.CENTER, assets.tile("""
            myTile10
            """)):
            if frequenza < 3000:
                pause(frequenza + frequenza / 2)
                if GAME == 1:
                    monster = sprites.create(assets.image("""
                        zombie
                        """), SpriteKind.enemy)
                    tiles.place_on_random_tile(monster, assets.tile("""
                        myTile11
                        """))
                    monster.follow(brain, 9)
                    monster.start_effect(effects.spray, 500)
                    Zombie_animation()
        music.thump.play()
        if frequenza < 600:
            frequenza = frequenza + 30
forever(on_forever8)

def on_forever9():
    global explosion, bomb
    if GAME == 1:
        if statusbar2.value >= 40:
            if explosion == 0:
                statusbar2.set_color(10, 0, 0)
                explosion = 1
                bomb = sprites.create(img("""
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . f f f . 5 4 . . . .
                        . . . . . . f f f f 4 . . 5 . . .
                        . . . . . f f f f 5 f f . . . . .
                        . . . . . f f f f f f f . . . . .
                        . . . . . f f f f f f f . . . . .
                        . . . . . . f f f f f . . . . . .
                        . . . . . . . f f f . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . . .
                        """),
                    SpriteKind.explo)
                bomb.set_position(10, 110)
                bomb.z = 9999999999
forever(on_forever9)

def on_forever10():
    if Bullet_.overlaps_with(italian):
        italian.image.replace(11, 5)
    elif not (Bullet_.overlaps_with(italian)):
        italian.image.replace(5, 11)
    if Bullet_.overlaps_with(English):
        English.image.replace(11, 5)
    elif not (Bullet_.overlaps_with(English)):
        English.image.replace(5, 11)
    if Bullet_.overlaps_with(impo):
        impo.image.replace(11, 5)
    elif not (Bullet_.overlaps_with(impo)):
        impo.image.replace(5, 11)
    if GAME == 5:
        if Bullet_.overlaps_with(_2):
            _2.image.replace(4, 5)
        elif not (Bullet_.overlaps_with(_2)):
            _2.image.replace(5, 4)
        if Bullet_.overlaps_with(_3):
            _3.image.replace(4, 5)
        elif not (Bullet_.overlaps_with(_3)):
            _3.image.replace(5, 4)
        if Bullet_.overlaps_with(_return):
            _return.image.replace(11, 5)
        elif not (Bullet_.overlaps_with(_return)):
            _return.image.replace(5, 11)
        if Bullet_.overlaps_with(Credits):
            animation.run_image_animation(Credits,
                [img("""
                    ..55555555555555555555555555555555555555555555555...
                    .5444444444444444444444444444444444444444444444445..
                    54fffffffffffffffffffffffffffffffffffffffffffffff45.
                    4ff444445f444445f444445f44445ff445f4444445f54444ff45
                    4ff445ffff445f45f445ffff445445f445f4444445f4455fff45
                    4ff445ffff445545f4444fff445545f445fff445ffff4445ff45
                    4ff44555ff44445ff44555ff445445f445fff445fff55544ff45
                    4ff444445f445f45f444445f44445ff445fff445fff44445ff45
                    .4fffffffffffffffffffffffffffffffffffffffffffffff45.
                    ..444444444444444444444444444444444444444444444445..
                    """)],
                500,
                False)
        elif not (Bullet_.overlaps_with(Credits)):
            animation.run_image_animation(Credits,
                [img("""
                    ..44444444444444444444444444444444444444444444444...
                    .4222222222222222222222222222222222222222222222224..
                    42fffffffffffffffffffffffffffffffffffffffffffffff24.
                    2ff222224f222224f222224f22224ff224f2222224f42222ff24
                    2ff224ffff224f24f224ffff224224f224f2222224f2244fff24
                    2ff224ffff224424f2222fff224424f224fff224ffff2224ff24
                    2ff22444ff22224ff22444ff224224f224fff224fff44422ff24
                    2ff222224f224f24f222224f22224ff224fff224fff22224ff24
                    .2fffffffffffffffffffffffffffffffffffffffffffffff24.
                    ..222222222222222222222222222222222222222222222224..
                    """)],
                500,
                False)
forever(on_forever10)

def on_forever11():
    global monster, frequenza
    if GAME == 1:
        if brain.tile_kind_at(TileDirection.CENTER, assets.tile("""
            myTile10
            """)):
            if frequenza < 3000:
                pause(frequenza + frequenza / 2)
                if GAME == 1:
                    monster = sprites.create(assets.image("""
                        zombie 2
                        """), SpriteKind.enemy)
                    tiles.place_on_random_tile(monster, assets.tile("""
                        myTile11
                        """))
                    monster.follow(brain, 9)
                    monster.start_effect(effects.spray, 500)
                    Zombie_animation()
        music.thump.play()
        if frequenza < 600:
            frequenza = frequenza + 30
forever(on_forever11)

def on_forever12():
    if explosion == 2:
        pause(1000)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy2)
forever(on_forever12)

def on_forever13():
    if GAME == 5:
        statusbar3.value = volu
        music.set_volume(volu)
forever(on_forever13)

def on_forever14():
    global volu
    if volu >= 255:
        volu = 255
    if volu <= 0:
        volu = 0
forever(on_forever14)

def on_forever15():
    global menu, multic
    if menu >= 23:
        menu = 23
        multic = 1
forever(on_forever15)

def on_forever16():
    if menu >= 24:
        music.pew_pew.stop()
forever(on_forever16)

def on_forever17():
    global GAME
    if controller.A.is_pressed() or controller.B.is_pressed():
        if GAME == 4:
            GAME = 5
            sprites.destroy_all_sprites_of_kind(SpriteKind.black)
forever(on_forever17)
