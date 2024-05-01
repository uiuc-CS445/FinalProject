#coding for tour_into_image
import numpy as np
import cv2
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import OpenGL.GL as gl
import os

class vector2D:
    def __init__(self, sx, sy):
        self.sx = sx
        self.sy = sy

class vector5D:
    def __init__(self, x, y, z, sx, sy):
        self.x = x
        self.y = y
        self.z = z
        self.sx = sx
        self.sy = sy

class vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class color3D:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

PI = 3.141592853

maxnumberoffiles = 100
currentfilenumber = 0
bmpfilename = [''] * maxnumberoffiles

class AUX_RGBImageRec:
    def __init__(self):
        self.sizeX = 0
        self.sizeY = 0
        self.data = []
def getBmpdata(bmpfilepath):
    if bmpfilepath is None:
        print("invalid path")
        exit(0)
        return None
    return cv2.imread(bmpfilepath)

def getSourceImage():
    bmpfilepath = "images/" + bmpfilename[currentfilenumber]
    sourceimage = getBmpdata(bmpfilepath)

def getEstimatedVerticesScreeenCoordinates():
    gradient = [0] * 4
    gradient[0] = (ctrlPoint[1].sy - ctrlPoint[0].sy) / (ctrlPoint[1].sx - ctrlPoint[0].sx)
    estimatedVertex[0].sx = ctrlPoint[0].sx
    estimatedVertex[0].sy = ctrlPoint[0].sy
    estimatedVertex[1].sx = ctrlPoint[1].sx
    estimatedVertex[1].sy = ctrlPoint[1].sy
    estimatedVertex[2].sx = ctrlPoint[2].sx
    estimatedVertex[2].sy = ctrlPoint[2].sy
    estimatedVertex[8].sx = ctrlPoint[3].sx
    estimatedVertex[8].sy = ctrlPoint[3].sy
    estimatedVertex[7].sx = ctrlPoint[4].sx
    estimatedVertex[7].sy = ctrlPoint[4].sy
    estimatedVertex[3].sx = (0.0 - ctrlPoint[0].sy) / gradient[0] + ctrlPoint[0].sx
    estimatedVertex[3].sy = 0.0
    estimatedVertex[5].sx = 0.0
    estimatedVertex[5].sy = (0.0 - ctrlPoint[0].sx) * gradient[0] + ctrlPoint[0].sy
    estimatedVertex[4].sx = (0.0 - ctrlPoint[0].sy) / gradient[1] + ctrlPoint[0].sx
    estimatedVertex[4].sy = 0.0
    estimatedVertex[6].sx = 1.0
    estimatedVertex[6].sy = (1.0 - ctrlPoint[0].sx) * gradient[1] + ctrlPoint[0].sy
    estimatedVertex[10].sx = (1.0 - ctrlPoint[0].sy) / gradient[2] + ctrlPoint[0].sx
    estimatedVertex[10].sy = 1.0
    estimatedVertex[12].sx = 1.0
    estimatedVertex[12].sy = (1.0 - ctrlPoint[0].sx) * gradient[2] + ctrlPoint[0].sy
    estimatedVertex[9].sx = (1.0 - ctrlPoint[0].sy) / gradient[3] + ctrlPoint[0].sx
    estimatedVertex[9].sy = 1.0
    estimatedVertex[11].sx = 0.0
    estimatedVertex[11].sy = (0.0 - ctrlPoint[0].sx) * gradient[3] + ctrlPoint[0].sy
def getEstimatedVerticesWorldCoordinates():
    grad = [0] * 4
    height = (estimatedVertex[7].sy - estimatedVertex[1].sy) / (-1.0) * estimatedVertex[1].z
    eye.x = ctrlPoint[0].sx
    eye.y = ctrlPoint[0].sy
    eye.z = 0.0
    estimatedVertex[0].x = ctrlPoint[0].sx
    estimatedVertex[0].y = ctrlPoint[0].sy
    estimatedVertex[0].z = estimatedVertex[1].z
    R = R0 = -estimatedVertex[0].z
    estimatedVertex[7].x = estimatedVertex[1].x
    estimatedVertex[8].x = estimatedVertex[2].x
    estimatedVertex[7].y = estimatedVertex[8].y = height
    estimatedVertex[7].z = estimatedVertex[1].z
    estimatedVertex[8].z = estimatedVertex[2].z
    for i in range(9, 13):
        grad[i-9] = (height - eye.y) / (estimatedVertex[i].sy - eye.y)
        estimatedVertex[i].x = grad[i-9] * (estimatedVertex[i].sx - eye.x) + eye.x
        estimatedVertex[i].z = grad[i-9] * (-1.0 - eye.z) + eye.z
        estimatedVertex[i].y = height

def getPerspectiveTransferMatrix():
    st = np.sin(theta)
    ct = np.cos(theta)
    sp = np.sin(phi)
    cp = np.cos(phi)
    eye.x = R * st * cp + estimatedVertex[0].x
    eye.y = R * sp + estimatedVertex[0].y
    eye.z = R * ct * cp + estimatedVertex[0].z
    mat[0] = ct
    mat[1] = st * sp
    mat[2] = -st * cp
    mat[3] = 0.0
    mat[4] = cp
    mat[5] = sp
    mat[6] = st
    mat[7] = -ct * sp
    mat[8] = ct * cp
def getTransferedEstimatedVerticesScreeenCoordinates():
    for i in range(1, 13):
        diff = vector3D(estimatedVertex[i].x - estimatedVertex[0].x, estimatedVertex[i].y - estimatedVertex[0].y, estimatedVertex[i].z - estimatedVertex[0].z)
        inte = vector3D(diff.x * mat[0] + diff.y * mat[3] + diff.z * mat[6], diff.x * mat[1] + diff.y * mat[4] + diff.z * mat[7], diff.x * mat[2] + diff.y * mat[5] + diff.z * mat[8])
        transferedEstimatedVertex[i].sx = R * inte.x / (R - inte.z)
        transferedEstimatedVertex[i].sy = R * inte.y / (R - inte.z)
    tevminx = 0.0
    tevmaxx = 0.0
    tevminy = 0.0
    tevmaxy = 0.0
    for i in range(1, 13):
        if transferedEstimatedVertex[i].sx > tevmaxx:
            tevmaxx = transferedEstimatedVertex[i].sx
        if transferedEstimatedVertex[i].sy > tevmaxy:
            tevmaxy = transferedEstimatedVertex[i].sy
    tevdiffx = tevmaxx - tevminx
    tevdiffy = tevmaxy - tevminy
    for i in range(1, 13):
        transferedEstimatedVertex[i].sx = (transferedEstimatedVertex[i].sx - tevminx) / tevdiffx
        transferedEstimatedVertex[i].sy = (transferedEstimatedVertex[i].sy - tevminy) / tevdiffy
        transferedEstimatedVertex[i].sx *= oevdiffx
        transferedEstimatedVertex[i].sy *= oevdiffy
        transferedEstimatedVertex[i].sx += oevminx
        transferedEstimatedVertex[i].sy += oevminy

def getScreeenCoordinates(input):
    diff = vector3D(input.x - estimatedVertex[0].x, input.y - estimatedVertex[0].y, input.z - estimatedVertex[0].z)
    inte = vector3D(diff.x * mat[0] + diff.y * mat[3] + diff.z * mat[6], diff.x * mat[1] + diff.y * mat[4] + diff.z * mat[7], diff.x * mat[2] + diff.y * mat[5] + diff.z * mat[8])
    output = vector2D(R * inte.x / (R - inte.z), R * inte.y / (R - inte.z))
    output.sx = (output.sx - tevminx) / tevdiffx
    output.sy = (output.sy - tevminy) / tevdiffy
    output.sx *= oevdiffx
    output.sy *= oevdiffy
    output.sx += oevminx
    output.sy += oevminy
    return output
def getInitialScreeenCoordinates(input):
    inv = [0] * 9
    inv[0] = ct
    inv[1] = st * sp
    inv[2] = -st * cp
    inv[3] = 0.0
    inv[4] = cp
    inv[5] = sp
    inv[6] = st
    inv[7] = -ct * sp
    inv[8] = ct * cp
    diff = vector3D(input.x - estimatedVertex[0].x, input.y - estimatedVertex[0].y, input.z - estimatedVertex[0].z)
    inte = vector3D(diff.x * inv[0] + diff.y * inv[3] + diff.z * inv[6], diff.x * inv[1] + diff.y * inv[4] + diff.z * inv[7], diff.x * inv[2] + diff.y * inv[5] + diff.z * inv[8])
    output = vector2D(R * inte.x / (R - inte.z), R * inte.y / (R - inte.z))
    output.sx = (output.sx - tevminx0) / tevdiffx0
    output.sy = (output.sy - tevminy0) / tevdiffy0
    output.sx *= oevdiffx
    output.sy *= oevdiffy
    output.sx += oevminx
    output.sy += oevminy
    return output

def screenCoordinates2sourceImageColor(input):
    x = int(input.sx * sourceimage.sizeX)
    y = int(input.sy * sourceimage.sizeY)
    headindex = y * 3 * sourceimage.sizeX + x * 3
    output = color3D(sourceimage.data[headindex] / 255.0, sourceimage.data[headindex+1] / 255.0, sourceimage.data[headindex+2] / 255.0)
    return output

def drawSpideryMesh():
    pass

def draw3Dbackground():
    pass

def drawGeneratedImage():
    pass

def myDisplay():
    pass

def myIdle():
    pass

def myReshape(w, h):
    pass
# Global variables
sourceimage = None
ctrlPoint = [None] * 5
estimatedVertices = []
estimatedVerticesScreenCoordinates = []
transferedEstimatedVerticesScreenCoordinates = []
theta = 0.0
phi = 0.0
deduceFlag = False
selectedCtrlPointIndex = -1
pbeginsx = 0.0
pbeginsy = 0.0
resolutionnumber = 0
rough_coefficient = 0.05
main_window = None
glui = None
maxnumberoffiles = 100
bmpfilename = [None] * maxnumberoffiles
currentfilenumber = 0

def myKeyboard(key, x, y):
    global theta, phi, deduceFlag

    if key == b'\x1b' or key == b'q':  # Escape or 'q'
        glut.glutLeaveMainLoop()
    elif deduceFlag:
        if key == b'4':
            theta += 1.0 * 3.14159 / 180.0
            getPerspectiveTransferMatrix()
            getTransferedEstimatedVerticesScreeenCoordinates()
            glut.glutPostRedisplay()
        elif key == b'6':
            theta -= 1.0 * 3.14159 / 180.0
            getPerspectiveTransferMatrix()
            getTransferedEstimatedVerticesScreeenCoordinates()
            glut.glutPostRedisplay()
        elif key == b'2':
            phi += 1.0 * 3.14159 / 180.0
            getPerspectiveTransferMatrix()
            getTransferedEstimatedVerticesScreeenCoordinates()
            glut.glutPostRedisplay()
        elif key == b'8':
            phi -= 1.0 * 3.14159 / 180.0
            getPerspectiveTransferMatrix()
            getTransferedEstimatedVerticesScreeenCoordinates()
            glut.glutPostRedisplay()

    glut.glutPostRedisplay()

def myMouse(button, state, x, y):
    global selectedCtrlPointIndex, pbeginsx, pbeginsy, deduceFlag

    pointedCoordinate = {'sx': 0.0, 'sy': 0.0}
    threshold = 5.0 / sourceimage['sizeX'] * 5.0 / sourceimage['sizeY']

    if button == glut.GLUT_LEFT_BUTTON:
        if state == glut.GLUT_DOWN:
            pointedCoordinate['sx'] = x / sourceimage['sizeX']
            pointedCoordinate['sy'] = 1.0 - y / sourceimage['sizeY']
            if deduceFlag:
                pbeginsx = pointedCoordinate['sx']
                pbeginsy = pointedCoordinate['sy']
            else:
                for i in range(5):
                    diffx = pointedCoordinate['sx'] - ctrlPoint[i]['sx']
                    diffy = pointedCoordinate['sy'] - ctrlPoint[i]['sy']
                    dist = diffx * diffx + diffy * diffy
                    if dist <= threshold:
                        selectedCtrlPointIndex = i
                        threshold = dist
        elif state == glut.GLUT_UP:
            selectedCtrlPointIndex = -1

def myMotion(x, y):
    global theta, phi, pbeginsx, pbeginsy, selectedCtrlPointIndex, deduceFlag

    pointedCoordinate = {'sx': x / sourceimage['sizeX'], 'sy': 1.0 - y / sourceimage['sizeY']}

    if deduceFlag:
        theta += (pbeginsx - pointedCoordinate['sx']) * 10.0 * 3.14159 / 180.0
        phi += (pbeginsy - pointedCoordinate['sy']) * 10.0 * 3.14159 / 180.0
        pbeginsx = pointedCoordinate['sx']
        pbeginsy = pointedCoordinate['sy']
        getPerspectiveTransferMatrix()
        getTransferedEstimatedVerticesScreeenCoordinates()
        glut.glutPostRedisplay()
    else:
        ctrlPoint[selectedCtrlPointIndex]['sx'] = pointedCoordinate['sx']
        ctrlPoint[selectedCtrlPointIndex]['sy'] = pointedCoordinate['sy']
        if selectedCtrlPointIndex == 0:  # Vanishing point
            if ctrlPoint[0]['sx'] <= ctrlPoint[1]['sx']:
                ctrlPoint[0]['sx'] = ctrlPoint[1]['sx'] + 1.0 / sourceimage['sizeX']
            elif ctrlPoint[0]['sx'] >= ctrlPoint[3]['sx']:
                ctrlPoint[0]['sx'] = ctrlPoint[3]['sx'] - 1.0 / sourceimage['sizeX']
            if ctrlPoint[0]['sy'] <= ctrlPoint[1]['sy']:
                ctrlPoint[0]['sy'] = ctrlPoint[1]['sy'] + 1.0 / sourceimage['sizeY']
            elif ctrlPoint[0]['sy'] >= ctrlPoint[3]['sy']:
                ctrlPoint[0]['sy'] = ctrlPoint[3]['sy'] - 1.0 / sourceimage['sizeY']
        elif selectedCtrlPointIndex == 1:  # Bottom left
            if ctrlPoint[1]['sx'] <= 0.0:
                ctrlPoint[1]['sx'] = 0.0 + 1.0 / sourceimage['sizeX']
            elif ctrlPoint[1]['sx'] >= ctrlPoint[0]['sx']:
                ctrlPoint[1]['sx'] = ctrlPoint[0]['sx'] - 1.0 / sourceimage['sizeX']
            if ctrlPoint[1]['sy'] >= ctrlPoint[0]['sy']:
                ctrlPoint[1]['sy'] = ctrlPoint[0]['sy'] - 1.0 / sourceimage['sizeY']
            elif ctrlPoint[1]['sy'] <= 0.0:
                ctrlPoint[1]['sy'] = 0.0 + 1.0 / sourceimage['sizeY']
            ctrlPoint[4]['sx'] = ctrlPoint[1]['sx']
            ctrlPoint[2]['sy'] = ctrlPoint[1]['sy']
        elif selectedCtrlPointIndex == 2:  # Bottom right
            if ctrlPoint[2]['sx'] <= ctrlPoint[0]['sx']:
                ctrlPoint[2]['sx'] = ctrlPoint[0]['sx'] + 1.0 / sourceimage['sizeX']
            elif ctrlPoint[2]['sx'] >= 1.0:
                ctrlPoint[2]['sx'] = 1.0 - 1.0 / sourceimage['sizeX']
            if ctrlPoint[2]['sy'] >= ctrlPoint[0]['sy']:
                ctrlPoint[2]['sy'] = ctrlPoint[0]['sy'] - 1.0 / sourceimage['sizeY']
            elif ctrlPoint[2]['sy'] <= 0.0:
                ctrlPoint[2]['sy'] = 0.0 + 1.0 / sourceimage['sizeY']
            ctrlPoint[3]['sx'] = ctrlPoint[2]['sx']
            ctrlPoint[1]['sy'] = ctrlPoint[2]['sy']
        elif selectedCtrlPointIndex == 3:  # Top right
            if ctrlPoint[3]['sx'] <= ctrlPoint[0]['sx']:
                ctrlPoint[3]['sx'] = ctrlPoint[0]['sx'] + 1.0 / sourceimage['sizeX']
            elif ctrlPoint[3]['sx'] >= 1.0:
                ctrlPoint[3]['sx'] = 1.0 - 1.0 / sourceimage['sizeX']
            if ctrlPoint[3]['sy'] >= 1.0:
                ctrlPoint[3]['sy'] = 1.0 - 1.0 / sourceimage['sizeY']
            elif ctrlPoint[3]['sy'] <= ctrlPoint[0]['sy']:
                ctrlPoint[3]['sy'] = ctrlPoint[0]['sy'] + 1.0 / sourceimage['sizeY']
            ctrlPoint[2]['sx'] = ctrlPoint[3]['sx']
            ctrlPoint[4]['sy'] = ctrlPoint[3]['sy']
        elif selectedCtrlPointIndex == 4:  # Top left
            if ctrlPoint[4]['sx'] <= 0.0:
                ctrlPoint[1]['sx'] = 0.0 + 1.0 / sourceimage['sizeX']
            elif ctrlPoint[4]['sx'] >= ctrlPoint[0]['sx']:
                ctrlPoint[4]['sx'] = ctrlPoint[0]['sx'] - 1.0 / sourceimage['sizeX']
            if ctrlPoint[4]['sy'] >= 1.0:
                ctrlPoint[4]['sy'] = 1.0 - 1.0 / sourceimage['sizeY']
            elif ctrlPoint[4]['sy'] <= ctrlPoint[0]['sy']:
                ctrlPoint[4]['sy'] = ctrlPoint[0]['sy'] + 1.0 / sourceimage['sizeY']
            ctrlPoint[1]['sx'] = ctrlPoint[4]['sx']
            ctrlPoint[3]['sy'] = ctrlPoint[4]['sy']

        getEstimatedVerticesScreeenCoordinates()
        glut.glutPostRedisplay()

# GLUI callback IDs
SOURCEIMAGE_ID = 200
DEDUCE_ID = 300
INITIALIZE_ID = 400
RESOLUTION_ID = 500

# GLUI variables
sourceImageListbox = None
deduceButton = None
resolutionListbox = None
initializeButton = None

def control_cb(control):
    global sourceImageListbox, deduceButton, resolutionListbox, initializeButton
    global sourceimage, deduceFlag, resolutionnumber, rough_coefficient

    if control == SOURCEIMAGE_ID:
        getSourceImage()
        initEstimatedVertices()
        glut.glutSetWindow(main_window)
        glut.glutReshapeWindow(sourceimage['sizeX'], sourceimage['sizeY'])
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluOrtho2D(0.0, 1.0, 0.0, 1.0)
        gl.glViewport(0, 0, sourceimage['sizeX'], sourceimage['sizeY'])
        glut.glutPostRedisplay()
    elif control == DEDUCE_ID:
        getEstimatedVerticesWorldCoordinates()
        getPerspectiveTransferMatrix()
        getTransferedEstimatedVerticesScreeenCoordinates()
        deduceFlag = True
        if glut.glutGetWindow() != main_window:
            glut.glutSetWindow(main_window)
        glut.glutPostRedisplay()
        sourceImageListbox.disable()
        deduceButton.disable()
        resolutionListbox.enable()
    elif control == INITIALIZE_ID:
        theta = 0.0
        phi = 0.0
        deduceFlag = False
        if glut.glutGetWindow() != main_window:
            glut.glutSetWindow(main_window)
        glut.glutPostRedisplay()
        sourceImageListbox.enable()
        deduceButton.enable()
        resolutionListbox.disable()
        resolutionnumber = 0
        glui.sync_live()
        rough_coefficient = 0.05
    elif control == RESOLUTION_ID:
        initializeButton.disable()
        resolutionListbox.disable()
        if resolutionnumber == 0:
            rough_coefficient = 0.05
        elif resolutionnumber == 1:
            rough_coefficient = 0.01
        elif resolutionnumber == 2:
            rough_coefficient = 0.005
        elif resolutionnumber == 3:
            rough_coefficient = 0.001
        if glut.glutGetWindow() != main_window:
            glut.glutSetWindow(main_window)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glColor3ub(0, 0, 0)
        gl.glRasterPos2f(0.05, 0.05)
        message = "NOW CALCULATING"
        for char in message:
            glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord(char))
        glut.glutSwapBuffers()
        glut.glutPostRedisplay()
        initializeButton.enable()
        resolutionListbox.enable()

def myGlui():
    global sourceImageListbox, deduceButton, resolutionListbox, initializeButton, glui

    glui = glut.GLUI_Master.create_glui("Controller", 0, 100, 100)

    sourceImageListbox = glui.add_listbox("Source image", currentfilenumber, SOURCEIMAGE_ID, control_cb)
    for bmp_file in os.listdir("images"):
        if bmp_file.endswith(".bmp"):
            sourceImageListbox.add_item(len(bmpfilename), bmp_file)
            bmpfilename[len(bmpfilename)] = "images/" + bmp_file

    glui.add_column(False)
    deduceButton = glui.add_button("Deduce", DEDUCE_ID, control_cb)
    glui.add_column(False)
    resolutionListbox = glui.add_listbox("Resolution", resolutionnumber, RESOLUTION_ID, control_cb)
    resolutionListbox.add_item(0, "Preview")
    resolutionListbox.add_item(1, "Low")
    resolutionListbox.add_item(2, "Normal")
    resolutionListbox.add_item(3, "High")
    resolutionListbox.disable()
    glui.add_column(False)
    initializeButton = glui.add_button("Initialize", INITIALIZE_ID, control_cb)

def main():
    global main_window

    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
    glut.glutInitWindowPosition(100, 200)
    main_window = glut.glutCreateWindow("Tour Into the Picture")

    glut.glutDisplayFunc(myDisplay)
    glut.glutIdleFunc(None)
    glut.glutReshapeFunc(myReshape)
    glut.glutKeyboardFunc(myKeyboard)
    glut.glutMouseFunc(myMouse)
    glut.glutMotionFunc(myMotion)

    myGlui()
    myInit()

    glut.glutMainLoop()

if __name__ == "__main__":
    main()

