import maya.cmds as cmds

body = 'Body'
wheels = ['wheel_01', 'wheel_02', 'wheel_03', 'wheel_04']

maya.cmds.select(body)

def assemble_car(name, body, wheel):
    
    wheels_grp = cmds.group('wheel_01', 'wheel_02', 'wheel_03', 'wheel_04', name="wheels_grp")

    car_grp = cmds.group(body, wheels_grp)
    return car_grp
    


cube = maya.cmds.polyCube()[0];


maya.cmds.connectAttr(cube+'.rx', body +'.tz');
cmds.select( 'wheels' )

maya.cmds.connectAttr( wheels+'.rx', body +'.tz');
maya.cmds.select(cube);
