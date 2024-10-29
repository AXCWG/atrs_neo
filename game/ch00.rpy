define x = Character("Undefined", what_slow_cps=10)
define s = Character("Undefined1", what_slow_cps=10)

image b5 = Color("#000000",alpha=0.5)
image testbg = "images/testpic2.jpg"
define white = Color("#FFFFFF")


transform dissolve_atl(duration=1.0, *, new_widget = None, old_widget=None): 

    delay duration

    old_widget with Dissolve(duration)
    events False
    


    new_widget with Dissolve(duration)
    events True
    


label ch00: 

    scene testbg
    """

    漆黑的屋子里，唯有电脑屏幕亮着荧光。

    外面明媚的太阳光隐约地透过窗帘，然而却不及电脑荧幕的光亮。

    不过，对于我来说，没有什么影响，甚至这样才是我熟悉的状态。

    """

    s "“呐——”"

    "我的背后传来了话语。"

    s "“呐呐，忙完了吗？”"

    "她的双手搭上了我的肩膀。"

    x "“还没哟——”"

    "方才搭载我肩膀上的双手又缩了回去。"

    s "“姆——”"

    """

    说起来也是啊，在这电脑屏幕前坐了有两三个小时了。

    是时候休息一下了。

    “嘎吱——”

    我的旋转椅年久失修。

    转过去，看着她。

    """

    x "寂寞了吗？"

    s "还好啦……"

    """

    躺在我床上的女生，是……

    是……

    """

    show b5 with Dissolve(0)
    
    $renpy.pause(2.0,hard=True)
    
    
    

    """

    我也记不起来细节了。

    总之就是因为种种原因，在三年前来到我家中借宿。

    结果又因为种种原因，仍然在我这里住着。

    """

    hide b5 with Dissolve(0.1)

    """

    嘛——没关系的。

    反正我也是一个人，怎么会介意呢

    更何况还是这样一个美少女。

    """

    x "嘿咻——"

    """

    我坐上了床。

    """



    $_dismiss_pause = False
    scene black with dissolve_atl(2.0)
    $_dismiss_pause = True
    

    return

