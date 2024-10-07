print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input('Your\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 =="left":
    choice2 = input('you\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        print('''                                      I
                                           _.$I
                                        _.$#$$I
                           I            $._   I
                           I            _.$   I
                           I     ...:::"""    I
                           I                  IU
                           I                  ==
                           IU                 IU
                           ==           =======U=======
                           IU           |      U      |
                       =====U=====      |      U      |
                       |    U    |     |       U       |
                       |    U    |     |       U       |
                      |     U     |   |        U        |
                      |     U     |   |        U        |
                     |      U      |  |        U        |         I
                     |      U      | |         U         |    ---~I        //
                    |       U       ||         U         | -=~ qp I       //|
                    |       U       |         _U____      | }  >< I      // |
                   |       _U___    |___----~~\WWWW/~---__|/  ---~I     //  |
                   |__---~~YYYYY---__|         U||         ~~~    I    //   |
                            U||    =============||============    I|| //    `.
                   ==========||====|            ||           |    ===//      |
                   |         ||    |            ||           |    I||/       |
                   |         ||    |            ZZ           |    /||        `.
                   |         ZZ    |            ZZ           |   //||         |
                   |         ZZ    |            ||           |  // ||         |
            I      |         ||    |            ||           | //  ||         `.
         ===I===   |         ||    |            ||           |//   ||          |
         |  I  |   |         ||    |            ||           //    ||          |
         |  I  |   |         ||    |            ZZ          //_____||_-----~~~~~|
         |__I__|   |_________||____|            ZZ          /|     ||     !!!!!! |
           .I                ||    |            ZZ           |     ||     ;  A I==+==
           `bo.              ||    |____________||___________|   !!!!!!!!!    /
           ===`bo.===        ||                 ||               ;   888    ,/
           |     `boo.   TTTTTTTTT              ||   !!!!!!!!!!!!   A   A A I
           |     &--`boo/        |______________LL   ;                 iiiiiii
           |     (___        8888 !!!!!!!!!!!!!!!!---'8888888            /
           |________\                                                   /
                     \            []   []   []   []   []   []   []     /
                      \                                               =|
                       \                                              =||
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        choice3 = input("The boat ride to the island is relaxing as the breeze over the water luls you into a nap. You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and on blue. Which colour do you choose?\n").lower()
        if choice3 == "red":
            print('''
               ,.   (   .      )        .      "
               ("     )  )'     ,'        )  . (`     '`
             .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
             _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..''')
            print("Flames burst from the room as you open the door. You are engulfed by the flames! Stop, Drop, and Roll! RolL! ARGGGHHHHHHH! Game Over")
        elif choice3 == "yellow":
            print("Upon opening the door, mountains of gold and Gems sparkle in the light from open door! You found the treasure! You Win!")
        elif choice3 == "blue":
            print('''
                                   ,aodObo,
                    ,AMMMMP~~~~
                 ,MMMMMMMMA.
               ,M;'     `YV'
              AM' ,OMA,
             AM|   `~VMM,.      .,ama,____,amma,..
             MML      )MMMD   .AMMMMMMMMMMMMMMMMMMD.
             VMMM    .AMMY'  ,AMMMMMMMMMMMMMMMMMMMMD
             `VMM, AMMMV'  ,AMMMMMMMMMMMMMMMMMMMMMMM,                ,
              VMMMmMMV'  ,AMY~~''  'MMMMMMMMMMMM' '~~             ,aMM
              `YMMMM'   AMM'        `VMMMMMMMMP'_              A,aMMMM
               AMMM'    VMMA. YVmmmMMMMMMMMMMML MmmmY          MMMMMMM
              ,AMMA   _,HMMMMmdMMMMMMMMMMMMMMMML`VMV'         ,MMMMMMM
              AMMMA _'MMMMMMMMMMMMMMMMMMMMMMMMMMA `'          MMMMMMMM
             ,AMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMa      ,,,   `MMMMMMM
             AMMMMMMMMM'~`YMMMMMMMMMMMMMMMMMMMMMMA    ,AMMV    MMMMMMM
             VMV MMMMMV   `YMMMMMMMMMMMMMMMMMMMMMY   `VMMY'  adMMMMMMM
             `V  MMMM'      `YMMMMMMMV.~~~~~~~~~,aado,`V''   MMMMMMMMM
                aMMMMmv       `YMMMMMMMm,    ,/AMMMMMA,      YMMMMMMMM
                VMMMMM,,v       YMMMMMMMMMo oMMMMMMMMM'    a, YMMMMMMM
                `YMMMMMY'       `YMMMMMMMY' `YMMMMMMMY     MMmMMMMMMMM
                 AMMMMM  ,        ~~~~~,aooooa,~~~~~~      MMMMMMMMMMM
                   YMMMb,d'         dMMMMMMMMMMMMMD,   a,, AMMMMMMMMMM
                    YMMMMM, A       YMMMMMMMMMMMMMY   ,MMMMMMMMMMMMMMM
                   AMMMMMMMMM        `~~~~'  `~~~~'   AMMMMMMMMMMMMMMM
                   `VMMMMMM'  ,A,                  ,,AMMMMMMMMMMMMMMMM
                 ,AMMMMMMMMMMMMMMA,       ,aAMMMMMMMMMMMMMMMMMMMMMMMMM
               ,AMMMMMMMMMMMMMMMMMMA,    AMMMMMMMMMMMMMMMMMMMMMMMMMMMM
             ,AMMMMMMMMMMMMMMMMMMMMMA   AMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            AMMMMMMMMMMMMMMMMMMMMMMMMAaAMMMMMMMMM''')
            print("You open door. A low growl emanates from the room. The lion springs on you from dark. The a last site you see are huge fangs decend upon you!")
        else:
            print("Not a correct answer. Your indecision causes you to panic and run into the water. You cannot Swim! Game Over.")
else:
    print("You fell into a pit! Game Over!")
