namespace SpriteKind {
    export const bullet = SpriteKind.create()
    export const a1 = SpriteKind.create()
    export const a2 = SpriteKind.create()
    export const Food2_0 = SpriteKind.create()
    export const enemy2 = SpriteKind.create()
    export const ing = SpriteKind.create()
    export const ita = SpriteKind.create()
    export const shadow = SpriteKind.create()
    export const explo = SpriteKind.create()
    export const impstazioni = SpriteKind.create()
    export const plus = SpriteKind.create()
    export const minus = SpriteKind.create()
    export const undo = SpriteKind.create()
    export const credits_button = SpriteKind.create()
    export const black = SpriteKind.create()
}
namespace StatusBarKind {
    export const volume = StatusBarKind.create()
}
sprites.onOverlap(SpriteKind.bullet, SpriteKind.ita, function (sprite11, otherSprite7) {
    if (controller.A.isPressed() || controller.B.isPressed()) {
        meno_tempo = game.runtime() / 1000
        italian.destroy()
        English.destroy()
        game.setDialogFrame(assets.image`text`)
        game.showLongText("Usa i tasti \"WASD\" per muovere il proiettile e colpisci tutti i mostri", DialogLayout.Full)
        game.setDialogFrame(assets.image`text trasparent`)
        linguage = 1
        music.stopAllSounds()
        music.setVolume(volu)
        _1 = sprites.create(assets.image`Black`, SpriteKind.a1)
        _1.setFlag(SpriteFlag.Invisible, true)
        frequenza = 3000
        frequenza20 = 3000
        kill = 0
        ombra = sprites.create(img`
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
            `, SpriteKind.shadow)
        ombra.setPosition(80, 60)
        ombra.z = 99999999
        copristatus2 = sprites.create(img`
            fffff...........ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            `, SpriteKind.shadow)
        copristatus2.z = 100000009
        copristatus2.setPosition(80, 117)
        statusbar2 = statusbars.create(160, 4, StatusBarKind.Magic)
        statusbar2.setColor(6, 0, 0)
        statusbar2.max = 40
        statusbar2.value = 0
        statusbar2.setPosition(80, 117)
        statusbar2.z = 100000000
        color.setColor(7, color.rgb(220, 70, 0))
        if (story.checkLastAnswer("          EASY")) {
            life_brain = 8
            difficulty = 1
        } else if (story.checkLastAnswer("         MEDIUM")) {
            life_brain = 5
            difficulty = 2
        } else if (story.checkLastAnswer("         HARDER")) {
            life_brain = 3
            difficulty = 3
        } else if (story.checkLastAnswer("       IMPOSSIBLE")) {
            life_brain = 0.5
            difficulty = 4
        }
        color.setColor(3, color.rgb(255, 153, 204))
        color.FadeToBlack.startScreenEffect(500)
        music.spooky.play()
        fade = 1
        scene.setBackgroundImage(assets.image`Background trasparent`)
        color.setColor(5, color.rgb(255, 200, 0))
        color.setColor(3, color.rgb(255, 153, 204))
        color.setColor(6, color.rgb(120, 120, 120))
        color.setColor(7, color.rgb(0, 200, 0))
        color.setColor(11, color.rgb(192, 192, 192))
        limit = life_brain
    }
})
sprites.onOverlap(SpriteKind.bullet, SpriteKind.Food, function (sprite, otherSprite) {
    otherSprite.destroy(effects.spray, 500)
    statusbar.value += 1
})
sprites.onOverlap(SpriteKind.bullet, SpriteKind.impstazioni, function (sprite152, otherSprite102) {
    if (controller.A.isPressed() || controller.B.isPressed()) {
        GAME = 5
        italian.setFlag(SpriteFlag.Ghost, true)
        italian.setFlag(SpriteFlag.Invisible, true)
        English.setFlag(SpriteFlag.Ghost, true)
        English.setFlag(SpriteFlag.Invisible, true)
        impo.setFlag(SpriteFlag.Ghost, true)
        impo.setFlag(SpriteFlag.Invisible, true)
        scene.setBackgroundImage(img`
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
            `)
        _return = sprites.create(img`
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
            `, SpriteKind.undo)
        _return.setPosition(11, 16)
        _3 = sprites.create(img`
            4 4 4 4 4 4 4 
            4 2 2 2 2 2 4 
            4 2 2 4 2 2 4 
            4 2 4 4 4 2 4 
            4 2 2 4 2 2 4 
            4 2 2 2 2 2 4 
            4 4 4 4 4 4 4 
            `, SpriteKind.plus)
        _3.setPosition(110, 40)
        _2 = sprites.create(img`
            4 4 4 4 4 4 4 
            4 2 2 2 2 2 4 
            4 2 2 2 2 2 4 
            4 2 4 4 4 2 4 
            4 2 2 2 2 2 4 
            4 2 2 2 2 2 4 
            4 4 4 4 4 4 4 
            `, SpriteKind.minus)
        _2.setPosition(50, 40)
        statusbar3 = statusbars.create(51, 9, StatusBarKind.volume)
        statusbar3.setPosition(80, 40)
        statusbar3.setColor(2, 4, 4)
        statusbar3.setBarBorder(1, 4)
        statusbar3.max = 255
        statusbar3.z = -1
        Credits = sprites.create(img`
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
            `, SpriteKind.credits_button)
        Credits.setPosition(80, 105)
    }
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite9, otherSprite5) {
    sprite9.destroy()
    brain.startEffect(effects.ashes, 500)
    music.smallCrash.play()
    statusbar.value += -1
})
sprites.onOverlap(SpriteKind.bullet, SpriteKind.credits_button, function (sprite15, otherSprite10) {
    if (controller.A.isPressed() || controller.B.isPressed()) {
        black2 = sprites.create(img`
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
            `, SpriteKind.black)
        GAME = 4
    }
})
scene.onOverlapTile(SpriteKind.enemy2, assets.tile`myTile8`, function (sprite12, location5) {
    sprite12.destroy()
})
scene.onOverlapTile(SpriteKind.Food2_0, assets.tile`myTile8`, function (sprite5, location2) {
    sprite5.destroy()
})
function Zombie_animation () {
    if (Math.percentChance(50)) {
        if (monster.x < 80) {
            animation.runImageAnimation(
            monster,
            assets.animation`animation zom 9`,
            700,
            true
            )
        }
        if (monster.x > 80) {
            animation.runImageAnimation(
            monster,
            assets.animation`animation zom 10`,
            700,
            true
            )
        }
    } else {
        if (monster.x < 80) {
            animation.runImageAnimation(
            monster,
            assets.animation`animation zom 11`,
            700,
            true
            )
        }
        if (monster.x > 80) {
            animation.runImageAnimation(
            monster,
            assets.animation`animation zom 12`,
            700,
            true
            )
        }
    }
}
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    if (GAME == 1) {
        menu += 1
    }
})
scene.onOverlapTile(SpriteKind.Projectile, assets.tile`myTile8`, function (sprite6, location3) {
    sprite6.destroy()
})
sprites.onOverlap(SpriteKind.a1, SpriteKind.a2, function (sprite17, otherSprite12) {
    _0.destroy()
    music.beamUp.play()
    if (linguage == 2) {
        game.showLongText("difficulty", DialogLayout.Center)
    } else {
        game.showLongText("difficoltà", DialogLayout.Center)
    }
    game.showLongText(story.getLastAnswer(), DialogLayout.Center)
    if (linguage == 2) {
        game.showLongText("time:", DialogLayout.Center)
    } else {
        game.showLongText("tempo:", DialogLayout.Center)
    }
    game.showLongText(Math.round(game.runtime() / 1000 - meno_tempo), DialogLayout.Center)
    if (linguage == 2) {
        game.showLongText("kill:", DialogLayout.Center)
    } else {
        game.showLongText("uccisioni:", DialogLayout.Center)
    }
    game.showLongText(kill, DialogLayout.Center)
    if (linguage == 2) {
        game.showLongText("esplosioni", DialogLayout.Center)
    } else {
        game.showLongText("explosion", DialogLayout.Center)
    }
    game.showLongText(num_eplosions, DialogLayout.Center)
    if (linguage == 2) {
        game.showLongText("try again?", DialogLayout.Center)
    } else {
        game.showLongText("riprovare?", DialogLayout.Center)
    }
    game.reset()
})
function Music () {
    music.playMelody("D E A D F D A E ", 200)
    music.playMelody("E D - D C - - - ", 1200)
}
sprites.onOverlap(SpriteKind.Food, SpriteKind.Food, function (sprite, otherSprite) {
    if (GAME == 1) {
        sprite.destroy()
        otherSprite.destroy()
        if (brain.tileKindAt(TileDirection.Center, assets.tile`myTile10`)) {
            if (frequenza < 3000) {
                pause(frequenza * 3)
                if (GAME == 1) {
                    cure = sprites.create(assets.image`cure`, SpriteKind.Food2_0)
                    animation.runImageAnimation(
                    cure,
                    assets.animation`Cure 2`,
                    100,
                    false
                    )
                    tiles.placeOnRandomTile(cure, assets.tile`myTile`)
                    cure.startEffect(effects.bubbles, 500)
                }
            }
        }
    }
})
sprites.onOverlap(SpriteKind.bullet, SpriteKind.ing, function (sprite154, otherSprite104) {
    if (controller.A.isPressed() || controller.B.isPressed()) {
        meno_tempo = game.runtime() / 1000
        italian.destroy()
        English.destroy()
        game.setDialogFrame(assets.image`text 3`)
        game.showLongText("Use the \"WASD\" keys to move the bullet and hit all the monsters", DialogLayout.Full)
        game.setDialogFrame(assets.image`trasparent`)
        linguage = 2
        music.stopAllSounds()
        music.setVolume(volu)
        _1 = sprites.create(assets.image`black`, SpriteKind.a1)
        _1.setFlag(SpriteFlag.Invisible, true)
        frequenza = 3000
        frequenza20 = 3000
        kill = 0
        ombra = sprites.create(img`
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
            `, SpriteKind.shadow)
        ombra.setPosition(80, 60)
        ombra.z = 99999999
        copristatus2 = sprites.create(img`
            fffff...........ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...f...
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            `, SpriteKind.shadow)
        copristatus2.z = 100000009
        copristatus2.setPosition(80, 117)
        statusbar2 = statusbars.create(160, 4, StatusBarKind.Magic)
        statusbar2.setColor(6, 0, 0)
        statusbar2.max = 40
        statusbar2.value = 0
        statusbar2.setPosition(80, 117)
        statusbar2.z = 100000000
        color.setColor(7, color.rgb(220, 70, 0))
        if (story.checkLastAnswer("          EASY")) {
            life_brain = 8
            difficulty = 1
        } else if (story.checkLastAnswer("         MEDIUM")) {
            life_brain = 5
            difficulty = 2
        } else if (story.checkLastAnswer("         HARDER")) {
            life_brain = 3
            difficulty = 3
        } else if (story.checkLastAnswer("       IMPOSSIBLE")) {
            life_brain = 0.5
            difficulty = 4
        }
        color.setColor(3, color.rgb(255, 153, 204))
        color.FadeToBlack.startScreenEffect(500)
        music.spooky.play()
        fade = 1
        scene.setBackgroundImage(assets.image`trasp backgrond`)
        color.setColor(5, color.rgb(255, 200, 0))
        color.setColor(3, color.rgb(255, 153, 204))
        color.setColor(6, color.rgb(120, 120, 120))
        color.setColor(7, color.rgb(0, 200, 0))
        color.setColor(11, color.rgb(192, 192, 192))
        limit = life_brain
    }
})
scene.onOverlapTile(SpriteKind.bullet, assets.tile`myTile8`, function (sprite4, location) {
    sprite4.destroy()
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    copristatus2.destroy()
    statusbar2.destroy()
    statusbar2.destroy()
    reload.destroy()
    sprites.destroyAllSpritesOfKind(SpriteKind.explo)
    ombra = sprites.create(img`
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
        `, SpriteKind.Player)
    GAME += 1
    color.setColor(6, color.rgb(0, 102, 0))
    music.stopAllSounds()
    music.bigCrash.play()
    tiles.setTilemap(tilemap`livello4`)
    tiles.loadMap(tiles.createSmallMap(tilemap`level4`))
    pause(100)
    tiles.setTilemap(tilemap`livello3`)
    if (multic == 0) {
        if (Math.percentChance(50)) {
            scene.setBackgroundImage(assets.image`animation 1`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 2`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 3`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 4`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 5`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 6`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 7`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 8`)
            pause(200)
            scene.setBackgroundImage(img`
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
                `)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 10`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 11`)
            pause(200)
            scene.setBackgroundImage(assets.image`animation 12`)
        } else {
            scene.setBackgroundImage(assets.image`Brain 1`)
            scene.setBackgroundImage(assets.image`Brain 2`)
            scene.setBackgroundImage(assets.image`Brain 3`)
            scene.setBackgroundImage(assets.image`Brain 4`)
            pause(500)
            scene.setBackgroundImage(assets.image`Brain 5`)
            pause(500)
            scene.setBackgroundImage(assets.image`Brain 6`)
            pause(500)
            scene.setBackgroundImage(assets.image`Brain 7`)
            pause(500)
            scene.setBackgroundImage(assets.image`Brain 8`)
            pause(500)
        }
    } else if (multic == 1) {
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(300)
        scene.setBackgroundImage(img`
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
            `)
        pause(500)
        color.setPalette(
        color.Adafruit
        )
        scene.setBackgroundImage(img`
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
            `)
        pause(500)
    }
    game.setDialogFrame(assets.image`trasparent text`)
    game.setDialogCursor(assets.image`statistic text`)
    game.showLongText("", DialogLayout.Bottom)
    game.setDialogCursor(assets.image`continue text`)
    game.setDialogFrame(assets.image`text 2`)
    game.setDialogTextColor(1)
    tiles.loadMap(tiles.createSmallMap(tilemap`level4`))
    _0 = sprites.create(assets.image`White`, SpriteKind.a2)
    monster.destroy()
})
sprites.onOverlap(SpriteKind.bullet, SpriteKind.enemy2, function (sprite2, otherSprite2) {
    otherSprite2.destroy(effects.spray, 500)
    frequenza += -30
    kill += 1
    reload_bar += 1
    music.pewPew.play()
    statusbar2.value += 1
})
function color_ingame () {
    color.setPalette(
    color.originalPalette
    )
    color.setColor(4, color.rgb(220, 70, 0))
    color.setColor(7, color.rgb(0, 200, 0))
    color.setColor(2, color.rgb(204, 0, 0))
    color.setColor(3, color.rgb(204, 0, 0))
    color.setColor(8, color.rgb(0, 0, 153))
    color.setColor(6, color.rgb(0, 102, 0))
    color.setColor(7, color.rgb(220, 70, 0))
    color.setColor(3, color.rgb(255, 153, 204))
    color.setColor(6, color.rgb(120, 120, 120))
    color.setColor(7, color.rgb(0, 200, 0))
    color.setColor(11, color.rgb(192, 192, 192))
}
sprites.onOverlap(SpriteKind.bullet, SpriteKind.Food2_0, function (sprite10, otherSprite6) {
    otherSprite6.destroy(effects.spray, 500)
    statusbar.value += 2
})
sprites.onOverlap(SpriteKind.Food, SpriteKind.Food2_0, function (sprite3, otherSprite3) {
    tiles.placeOnRandomTile(sprite3, assets.tile`myTile`)
})
function old_codes () {
    // beta
    scene.setBackgroundImage(assets.image`Background begin`)
    animation.runImageAnimation(
    cure,
    assets.animation`Cure 2`,
    100,
    false
    )
    cure.setKind(SpriteKind.Food2_0)
    if (GAME == 1) {
        if (reload_bar == 0) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 1) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 1) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 8) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 12) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 16) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 21) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 26) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 30) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 35) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        } else if (reload_bar == 40) {
            animation.runImageAnimation(
            reload,
            [img`
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
                `],
            100,
            false
            )
        }
    }
}
scene.onOverlapTile(SpriteKind.Enemy, assets.tile`myTile8`, function (sprite7, location4) {
    sprite7.destroy()
})
sprites.onOverlap(SpriteKind.bullet, SpriteKind.Enemy, function (sprite16, otherSprite11) {
    otherSprite11.destroy(effects.spray, 500)
    frequenza += -30
    kill += 1
    reload_bar += 1
    music.setVolume(volu)
    music.pewPew.play()
    statusbar2.value += 1
})
sprites.onOverlap(SpriteKind.a1, SpriteKind.Projectile, function (sprite8, otherSprite4) {
    if (controller.A.isPressed()) {
        if (statusbar2.value >= 40) {
            if (explosion == 1) {
                explosion = 2
                statusbar2.value = 0
                statusbar2.setColor(6, 0, 0)
                music.setVolume(volu)
                music.buzzer.play()
                num_eplosions += 1
            }
        }
    } else if (controller.B.isPressed()) {
        if (statusbar2.value >= 40) {
            if (explosion == 1) {
                explosion = 2
                statusbar2.value = 0
                statusbar2.setColor(6, 0, 0)
                music.setVolume(volu)
                music.buzzer.play()
                num_eplosions += 1
            }
        }
    }
})
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    if (GAME == 5) {
        if (Bullet_.overlapsWith(_2)) {
            volu += -25.5
            music.knock.play()
        } else if (Bullet_.overlapsWith(_3)) {
            volu += 25.5
            music.knock.play()
        }
    }
})
sprites.onOverlap(SpriteKind.enemy2, SpriteKind.Projectile, function (sprite13, otherSprite8) {
    sprite13.destroy()
    brain.startEffect(effects.ashes, 500)
    music.smallCrash.play()
    statusbar.value += -2
})
sprites.onOverlap(SpriteKind.bullet, SpriteKind.undo, function (sprite153, otherSprite103) {
    if (controller.A.isPressed() || controller.B.isPressed()) {
        GAME = 0
        italian.setFlag(SpriteFlag.Ghost, false)
        italian.setFlag(SpriteFlag.Invisible, false)
        English.setFlag(SpriteFlag.Ghost, false)
        English.setFlag(SpriteFlag.Invisible, false)
        impo.setFlag(SpriteFlag.Ghost, false)
        impo.setFlag(SpriteFlag.Invisible, false)
        scene.setBackgroundImage(assets.image`language text`)
        _return.destroy()
        _2.destroy()
        _3.destroy()
        statusbar3.destroy()
        Credits.destroy()
    }
})
function start () {
    color.setColor(3, color.rgb(204, 0, 0))
    GAME = 1
    frequenza = 3000
    frequenza20 = 3000
    kill = 0
    info.setScore(kill)
    info.player2.setScore(frequenza)
    brain = sprites.create(assets.image`brain`, SpriteKind.Projectile)
    statusbar = statusbars.create(21, 5, StatusBarKind.Health)
    statusbar.setColor(7, 2, 6)
    statusbar.setBarBorder(1, 15)
    statusbar.attachToSprite(brain, -20, 0)
    statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    color.setColor(7, color.rgb(220, 70, 0))
    if (linguage == 2) {
        life_brain = game.askForNumber("Select life (1-9)", 1)
    } else {
        life_brain = game.askForNumber("Seleziona vita (1-9)", 1)
    }
    Bullet_ = sprites.create(assets.image`bullet`, SpriteKind.bullet)
    controller.moveSprite(Bullet_, 100, 100)
    Bullet_.setStayInScreen(true)
    scene.setBackgroundImage(assets.image`Trasparent Background`)
    color.setColor(3, color.rgb(255, 153, 204))
    color.setColor(6, color.rgb(120, 120, 120))
    color.setColor(7, color.rgb(0, 200, 0))
    color.setColor(11, color.rgb(192, 192, 192))
    limit = life_brain
    statusbar.max = life_brain * 2
    tiles.setTilemap(tilemap`level2`)
}
controller.A.onEvent(ControllerButtonEvent.Released, function () {
    if (GAME == 5) {
        if (Bullet_.overlapsWith(_2)) {
            volu += -25.5
            music.knock.play()
        } else if (Bullet_.overlapsWith(_3)) {
            volu += 25.5
            music.knock.play()
        }
    }
})
scene.onOverlapTile(SpriteKind.Food, assets.tile`myTile8`, function (sprite18, location6) {
    sprite18.destroy()
})
function fade_color_ingame () {
    color.setPalette(
    color.originalPalette
    )
    color.setColor(5, color.rgb(255, 200, 0))
    color.setColor(4, color.rgb(220, 70, 0))
    color.setColor(2, color.rgb(204, 0, 0))
    color.setColor(3, color.rgb(204, 0, 0))
    color.setColor(8, color.rgb(0, 0, 153))
    color.setColor(3, color.rgb(255, 153, 204))
    color.setColor(6, color.rgb(120, 120, 120))
    color.setColor(7, color.rgb(0, 200, 0))
    color.setColor(11, color.rgb(192, 192, 192))
}
let bomb: Sprite = null
let skeletron: Sprite = null
let reload_bar = 0
let reload: Sprite = null
let cure: Sprite = null
let _0: Sprite = null
let menu = 0
let monster: Sprite = null
let black2: Sprite = null
let brain: Sprite = null
let Credits: Sprite = null
let statusbar3: StatusBarSprite = null
let _2: Sprite = null
let _3: Sprite = null
let _return: Sprite = null
let statusbar: StatusBarSprite = null
let limit = 0
let fade = 0
let life_brain = 0
let statusbar2: StatusBarSprite = null
let copristatus2: Sprite = null
let ombra: Sprite = null
let kill = 0
let frequenza20 = 0
let frequenza = 0
let _1: Sprite = null
let Bullet_: Sprite = null
let English: Sprite = null
let italian: Sprite = null
let impo: Sprite = null
let volu = 0
let num_eplosions = 0
let explosion = 0
let multic = 0
let GAME = 0
let linguage = 0
let meno_tempo = 0
let difficulty = 0
if (!(blockSettings.exists("n"))) {
    blockSettings.writeString("n", game.askForString("name?", 3))
    story.showPlayerChoices("italiano", "english")
    blockSettings.writeString("l", story.getLastAnswer())
}
music.sonar.play()
music.spooky.play()
difficulty = 0
meno_tempo = 0
linguage = 0
GAME = 0
multic = 0
explosion = 0
num_eplosions = 0
volu = 25.5
color.setColor(5, color.rgb(255, 200, 0))
color.setColor(4, color.rgb(220, 70, 0))
color.setColor(7, color.rgb(0, 200, 0))
color.setColor(2, color.rgb(204, 0, 0))
color.setColor(3, color.rgb(204, 0, 0))
color.setColor(8, color.rgb(0, 0, 153))
color.setColor(6, color.rgb(0, 102, 0))
scene.setBackgroundImage(assets.image`Backgrond not beta`)
game.setDialogTextColor(1)
game.setDialogFrame(assets.image`trasparent 3`)
game.setDialogCursor(assets.image`continue text 2`)
game.showLongText("", DialogLayout.Bottom)
scene.setBackgroundImage(img`
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
    `)
story.showPlayerChoices("          EASY", "         MEDIUM", "         HARDER", "       IMPOSSIBLE")
impo = sprites.create(img`
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
    `, SpriteKind.impstazioni)
impo.setPosition(151, 16)
italian = sprites.create(assets.image`italian`, SpriteKind.ita)
English = sprites.create(assets.image`english`, SpriteKind.ing)
Bullet_ = sprites.create(assets.image`Bullet`, SpriteKind.bullet)
Bullet_.z = 999999999
controller.moveSprite(Bullet_, 75, 75)
Bullet_.setStayInScreen(true)
scene.setBackgroundImage(assets.image`language text`)
forever(function () {
    if (GAME == 1) {
        if (brain.tileKindAt(TileDirection.Center, assets.tile`myTile10`)) {
            if (frequenza < 3000) {
                pause(frequenza * 3)
                if (GAME == 1) {
                    cure = sprites.create(assets.image`cure`, SpriteKind.Food)
                    tiles.placeOnRandomTile(cure, assets.tile`myTile`)
                    cure.startEffect(effects.bubbles, 500)
                }
            }
        }
    }
})
forever(function () {
    if (GAME == 1) {
        if (brain.tileKindAt(TileDirection.Center, assets.tile`myTile10`)) {
            if (frequenza < 2500) {
                pause(frequenza20)
                if (GAME == 1) {
                    skeletron = sprites.create(assets.image`skeletron`, SpriteKind.enemy2)
                    tiles.placeOnRandomTile(skeletron, assets.tile`myTile11`)
                    skeletron.follow(brain, 25)
                    skeletron.startEffect(effects.spray, 500)
                }
                frequenza20 = frequenza20 - 30
                if (skeletron.x < 80) {
                    if (multic == 0) {
                        animation.runImageAnimation(
                        skeletron,
                        [img`
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
                            `,img`
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
                            `],
                        300,
                        true
                        )
                    } else {
                        animation.runImageAnimation(
                        skeletron,
                        assets.animation`animation sk 1`,
                        300,
                        true
                        )
                    }
                }
                if (skeletron.x > 80) {
                    if (multic == 0) {
                        animation.runImageAnimation(
                        skeletron,
                        assets.animation`animation sk 2`,
                        300,
                        true
                        )
                    } else {
                        animation.runImageAnimation(
                        skeletron,
                        [img`
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
                            `,img`
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
                            `],
                        300,
                        true
                        )
                    }
                }
            }
        }
        if (frequenza < 600) {
            frequenza = frequenza + 30
        }
        if (frequenza20 < 600) {
            frequenza20 = frequenza20 + 30
        }
    }
})
forever(function () {
    if (GAME == 1) {
        if (kill == 0) {
            music.setVolume(0)
            music.stopAllSounds()
        } else {
            music.setVolume(volu)
        }
    }
})
forever(function () {
    if (GAME == 1) {
        if (brain.tileKindAt(TileDirection.Center, assets.tile`myTile10`)) {
            if (frequenza < 3001) {
                pause(frequenza)
                if (GAME == 1) {
                    monster = sprites.create(assets.image`zombie 3`, SpriteKind.Enemy)
                    tiles.placeOnRandomTile(monster, assets.tile`myTile11`)
                    monster.follow(brain, 9)
                    monster.startEffect(effects.spray, 500)
                    Zombie_animation()
                }
            }
        }
        music.thump.play()
        if (frequenza < 600) {
            frequenza = frequenza + 30
        }
    }
})
forever(function () {
    if (limit != life_brain) {
        life_brain = limit
    }
})
forever(function () {
    if (fade == 1) {
        Bullet_.setPosition(80, 60)
        fade = 0
        pause(1000)
        GAME += 1
        fade_color_ingame()
        brain = sprites.create(assets.image`brain 3`, SpriteKind.Projectile)
        brain.z = 99999999999
        reload = sprites.create(img`
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
            `, SpriteKind.Player)
        reload.z = 9999999999
        reload.setPosition(10, 110)
        statusbar = statusbars.create(21, 5, StatusBarKind.Health)
        statusbar.setColor(7, 2, 6)
        statusbar.setBarBorder(1, 15)
        statusbar.attachToSprite(brain, -20, 0)
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
        tiles.setTilemap(tilemap`level2`)
        statusbar.max = life_brain * 2
    }
})
forever(function () {
    if (explosion == 2) {
        for (let index = 0; index < 2; index++) {
            bomb.follow(brain, 100)
            bomb.ay = -100
            bomb.ax = 100
            bomb.z = 99999999999999
            scaling.scaleByPercent(bomb, 200, ScaleDirection.Uniformly, ScaleAnchor.Middle)
            pause(1000)
            scene.cameraShake(1, 200)
        }
        music.zapped.play()
        music.sonar.play()
        music.spooky.play()
        explosion = 0
        bomb.destroy(effects.fire, 500)
        scene.cameraShake(3, 500)
    }
})
forever(function () {
    if (GAME == 1) {
        if (brain.tileKindAt(TileDirection.Center, assets.tile`myTile10`)) {
            if (frequenza < 3000) {
                pause(frequenza + frequenza / 2)
                if (GAME == 1) {
                    monster = sprites.create(assets.image`zombie`, SpriteKind.Enemy)
                    tiles.placeOnRandomTile(monster, assets.tile`myTile11`)
                    monster.follow(brain, 9)
                    monster.startEffect(effects.spray, 500)
                    Zombie_animation()
                }
            }
        }
        music.thump.play()
        if (frequenza < 600) {
            frequenza = frequenza + 30
        }
    }
})
forever(function () {
    if (GAME == 1) {
        if (statusbar2.value >= 40) {
            if (explosion == 0) {
                statusbar2.setColor(10, 0, 0)
                explosion = 1
                bomb = sprites.create(img`
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
                    `, SpriteKind.explo)
                bomb.setPosition(10, 110)
                bomb.z = 9999999999
            }
        }
    }
})
forever(function () {
    if (Bullet_.overlapsWith(italian)) {
        italian.image.replace(11, 5)
    } else if (!(Bullet_.overlapsWith(italian))) {
        italian.image.replace(5, 11)
    }
    if (Bullet_.overlapsWith(English)) {
        English.image.replace(11, 5)
    } else if (!(Bullet_.overlapsWith(English))) {
        English.image.replace(5, 11)
    }
    if (Bullet_.overlapsWith(impo)) {
        impo.image.replace(11, 5)
    } else if (!(Bullet_.overlapsWith(impo))) {
        impo.image.replace(5, 11)
    }
    if (GAME == 5) {
        if (Bullet_.overlapsWith(_2)) {
            _2.image.replace(4, 5)
        } else if (!(Bullet_.overlapsWith(_2))) {
            _2.image.replace(5, 4)
        }
        if (Bullet_.overlapsWith(_3)) {
            _3.image.replace(4, 5)
        } else if (!(Bullet_.overlapsWith(_3))) {
            _3.image.replace(5, 4)
        }
        if (Bullet_.overlapsWith(_return)) {
            _return.image.replace(11, 5)
        } else if (!(Bullet_.overlapsWith(_return))) {
            _return.image.replace(5, 11)
        }
        if (Bullet_.overlapsWith(Credits)) {
            animation.runImageAnimation(
            Credits,
            [img`
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
                `],
            500,
            false
            )
        } else if (!(Bullet_.overlapsWith(Credits))) {
            animation.runImageAnimation(
            Credits,
            [img`
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
                `],
            500,
            false
            )
        }
    }
})
forever(function () {
    if (GAME == 1) {
        if (brain.tileKindAt(TileDirection.Center, assets.tile`myTile10`)) {
            if (frequenza < 3000) {
                pause(frequenza + frequenza / 2)
                if (GAME == 1) {
                    monster = sprites.create(assets.image`zombie 2`, SpriteKind.Enemy)
                    tiles.placeOnRandomTile(monster, assets.tile`myTile11`)
                    monster.follow(brain, 9)
                    monster.startEffect(effects.spray, 500)
                    Zombie_animation()
                }
            }
        }
        music.thump.play()
        if (frequenza < 600) {
            frequenza = frequenza + 30
        }
    }
})
forever(function () {
    if (explosion == 2) {
        pause(1000)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
        sprites.destroyAllSpritesOfKind(SpriteKind.enemy2)
    }
})
forever(function () {
    if (GAME == 5) {
        statusbar3.value = volu
        music.setVolume(volu)
    }
})
forever(function () {
    if (volu >= 255) {
        volu = 255
    }
    if (volu <= 0) {
        volu = 0
    }
})
forever(function () {
    if (menu >= 23) {
        menu = 23
        multic = 1
    }
})
forever(function () {
    if (menu >= 24) {
        music.pewPew.stop()
    }
})
forever(function () {
    if (controller.A.isPressed() || controller.B.isPressed()) {
        if (GAME == 4) {
            GAME = 5
            sprites.destroyAllSpritesOfKind(SpriteKind.black)
        }
    }
})
