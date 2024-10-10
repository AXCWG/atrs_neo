define e = Character(None,what_xalign=0.5,what_yalign=0.5,window_yalign=0.5,window_background=None,what_slow_abortable=False, what_slow_cps=10, 
)
screen disableclick(time):
    timer time action Hide("disableclick")
    key "mouseup_1" action NullAction()
label start:
    $ quick_menu = False
    show screen disableclick(2)
    e "问你个问题。" 
    show screen disableclick(2)
    e ""

    show screen disableclick(2)


    
    return
