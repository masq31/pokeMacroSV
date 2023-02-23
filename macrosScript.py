import nxbt

eggLoop = 0 #goes to 200
walkLoop = 0 #goes to 10
overallTimer = 0 #set to as long as you want this to keep going

#reading the text file as needed. 
#TODO - make into a list for each file

text_file = open("/home/pi/Desktop/working/sandwichMacro.txt", "r")
data1 = text_file.read()
text_file.close()

text_file = open("/home/pi/Desktop/working/firstFly.txt", "r")
data2 = text_file.read()
text_file.close()

text_file = open("/home/pi/Desktop/working/picnicEggSetup.txt", "r")
data3 = text_file.read()
text_file.close()

text_file = open("/home/pi/Desktop/working/loopEggMacro.txt", "r")
data4 = text_file.read()
text_file.close()

text_file = open("/home/pi/Desktop/working/picnicEnd.txt", "r")
data5 = text_file.read()
text_file.close()

text_file = open("/home/pi/Desktop/working/boxManagement.txt", "r")
data6 = text_file.read()
text_file.close()

text_file = open("/home/pi/Desktop/working/loopWalkingScript.txt", "r")
data7 = text_file.read()
text_file.close()

text_file = open("/home/pi/Desktop/working/flyCollect.txt", "r")
data8 = text_file.read()
text_file.close()

#macro example from docs. 
#macro = """
#L_STICK@+000+100 1.016666665s
#0.016666665s
#0.016666665s
#0.016666665s
#0.016666665s
#0.016666665s
#0.016666665s
#0.016666665s
#0.016666665s
#L_STICK@+000-100 1.016666665s
#"""

# Start the NXBT service
nx = nxbt.Nxbt()

# Create a Pro Controller and wait for it to connect
controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)
#
#
# Run a macro on the Pro Controller
#TODO - make it run for a specified amount of time

#sandwich macro final
nx.macro(controller_index, data1)

#first fly
nx.macro(controller_index, data2)

#main loop, add a number!!
while (overallTimer != 8):
    
    #picnic egg setup
    nx.macro(controller_index, data3)   
    
    #loop egg macro final
    while (eggLoop != 100):
        nx.macro(controller_index, data4)
        eggLoop += 1

    #picnic end
    nx.macro(controller_index, data5)

    #box management
    nx.macro(controller_index, data6)

    nx.macro(controller_index, """\nPLUS 0.1S\n""")
    #it works!

    #loopWalking script final
    while (walkLoop != 12):
        nx.macro(controller_index, data7)
        walkLoop += 1

    #fly collect
    nx.macro(controller_index, data8)

    #reset and increment
    eggLoop = 0 
    walkLoop = 0 
    overallTimer +=1
    nx.macro(controller_index, """\nX 0.1S\n1S\nDPAD_DOWN 0.1s\n1S\nX 1S""")

#script continues to run without need for controller to reconnect all the time 