#FK chain system LVO - Jan 2022

import maya.cmds as mc
import maya.mel as mel

def rig_fk_chain(arg):
    # List old joint chain
    mc.select (hi=True)
    originJoints = mc.ls(selection=True, type='joint')
    # Snap Joints for function
    mc.select(originJoints[0])
    
    def copyJointChain(prefix = 'FK',joints=[]):
        if not joints:
            mc.select(hi = True)
            joints = mc.ls(selection=True, type='joint')
        
        mc.select(clear=True)
        counter=1
        for joint in joints:
            pos=mc.xform(joint, query=True, translation=True, worldSpace=True)
            jointOrientation = mc.joint(joint, query=True, orientation=True)
            newJoint = mc.joint(name=prefix+"_"+str(counter)+"_JNT", p=pos, o=jointOrientation)
            counter +=1
            			
    copyJointChain(mc.textFieldGrp(jntNameField, q=True, text=True))

    # Hide old joint chain
    mc.hide(originJoints[0])
    

       
"""__________________WINDOW_______________"""

windowName = "FKChainSystemValentinaOrozco"
windowTitle ='FK Chain System Valentina Orozco'
windowWidth = 400
windowHeight = 175

def UI():

    if mc.window(windowName, exists=True):
        mc.deleteUI(windowName)

    # Window
    myWindow = mc.window(windowName, title=windowTitle, w=windowWidth, h=windowHeight)
    mc.window(windowName, edit=True, w=windowWidth, h=windowHeight)

    # Main Layout
    mainLayout = mc.columnLayout('mainLayout', w=windowWidth, rowSpacing=5)


    mc.separator(h=10)
    mc.text('Select first joint chain', w=windowWidth, align='center', backgroundColor=(0.4,0.4,0.4), h=35)
    mc.separator(h=3)
    
    # TextFields
    global jntNameField
    jntNameField = mc.textFieldGrp(l="Joints' Name", editable=True, pht='fk_JNT')
    mc.separator(h=3)

    # Button
    mc.button('Button1',label='Create Joints', w=windowWidth, h= 35, backgroundColor=(0.1,0.7,0.85), command= rig_fk_chain)
    
    mc.separator(h=5)
    mc.text('Select the joints you want to rig', w=windowWidth, align='center', backgroundColor=(0.4,0.4,0.4), h=35)
    mc.separator(h=3)
    
    global ctrlSizeSlider
    ctrlSizeSlider = mc.intSliderGrp(l="Controls' Size", min=1, max=15, field=True, v=1)
    mc.separator(h=3)
    
    # Button
    mc.button('Button2',label='Rig it!', w=windowWidth, h= 35, backgroundColor=(0.1,0.7,0.85), command= rig_fk_chain)
   
    mc.separator(h=7)
    

    mc.showWindow(myWindow)


UI()    