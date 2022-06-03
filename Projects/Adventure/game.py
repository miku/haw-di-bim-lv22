#!/usr/bin/env python

instructions = """

Welcome young time traveller!

###################(((((((#(((((((((((//////////////////////////(((////////////(((((################
####################(((((((((((((((((((((((///////////////////(((///////***////((((((##(######((((((
(((((((((((((((((((#(((((////((((((((((((((((((////////****///////////******/////(((((((((((((((((((
((/////////////((((((((((/////**////((////(((((((((((((//////////////*//******/////(((((((((((((((((
((((///////////*/*****//**/************///////((((((((((((((//////////***********////////////////(((
((((((((/////////***************************////////((((((((((/////*///*************/////////(((/((/
//(((((((((((/((//////**************,,,,,,,,,****///////////////******************////////(((((/////
///////((((((((((((((((((///********,,,,,,,....,,,,,,*******************,,******/////////(((((((((((
,,*********/////////////////******,*,,,,**,,,,,,..,,,,.*#%%/,,,,,,,,,,,,......,***//////((((((((((((
****,,,,,,,,,,,,,,,******/////********,,**#%&&&/*,,,,####%%%%#,,,,,,,,,,.....,,..,,**///////((((((((
*********,,,,,,,,,,,,,,,,,,,,***,,,,,,,*%#%%%%%%#%,%#(/#########(,,,,,,,,,,,,,,,***,,,,,,****////(((
,,.,,,,,,,,,,,,,...................,,((#%%#%##%#%%%#%(#((((##(#####/*(%%#/**,,,,,,*,**/////((////(((
,...........................,,,,*,,#%##%##%#####%(###(%#(#############%%####(*/*////***,,**//(((((#(
,,,,,,,...................,,,,,,,############(###(####((%#%#&(######%#%######%%(*********///(((////(
,,,,,,,,,,,.,.........#%###/,,(#((#((%#((%%%#%########(#(###########(######%######/*,*****//((//((##
%%%%%%###(####(((//(%&%%&%%%#%%####%%##/%#%#####(##(####((#((%###(#((/((#(#((########(*/////////%###
#((*/#((////((#%%#%%%%%%%%%#%#%%(((%%##%%####%######((/(((%((%#(#((#(//((/((#((%(#//*/////(#(##(#(#(
(#####((/**///////((/(///************,,,*,*,,,,,,,,,*,,,,************,,*/////((/((#(((#(###(#//(((((
####((///////**,**,******/////***********************************************,***///////((((((((((//
###(((((((/////********///(/****,,**//**********************************/***********//////////((/(//
#####(((((((((//***,****//#//****//((((///****************/*****/((((//(#((((((((((((((((((((((#((((
##########(((((/(((///***//////***//********////////////(//(((((///////(//((((((((((((((((((((######
##########(####(///((/(((////*****///////////////////*****/////((((((((((//(((##((((((((((((((((####

The time machine your friend gave you worked, you left your port city and woke
up in a desert. On the horizon, you see some monuments. Nearby is a gate.

It feel good, but you have no idea, how to come back - which makes you a little
nervous. Can you find your way home?

* walk around with "n", "e", "s", "w" (north, east, south, west)
* do something like: "t", "p", "d" (talk, pickup, drop)
* type "q" to quit

"""

world = {
    "todo": "find a way to represent a small world and let the user navigate",
}

def main():
    print(instructions)
    while True:
        command = input("direction (n, e, s, w) or action (t, p, d) >> ")
        print("...")
        if command == "q":
            break


if __name__ == '__main__':
    main()