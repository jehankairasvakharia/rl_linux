# Automatically generated. Do not modify!

###### const from defines ######
MINVAL = 1e-15                      # minimum value in any denominator
PI = 3.141592653589793              # 
MAXVAL = 10000000000.0              # maximum value in qpos, qvel, qacc
MINMU = 1e-05                       # minimum friction coefficient
MINIMP = 0.0001                     # minimum constraint impedance
MAXIMP = 0.9999                     # maximum constraint impedance
MAXCONPAIR = 50.0                   # maximum number of contacts per geom pair
MAXVFS = 200.0                      # maximum number of files in virtual file system
MAXVFSNAME = 100.0                  # maximum filename size in virtual file system
NEQDATA = 7.0                       # number of eq_data fields
NDYN = 3.0                          # number of actuator dynamics parameters
NGAIN = 3.0                         # number of actuator gain parameters
NBIAS = 3.0                         # number of actuator bias parameters
NREF = 2.0                          # number of solver reference parameters
NIMP = 3.0                          # number of solver impedance parameters
NSOLVER = 1000.0                    # size of mjData.solver_XXX arrays
NGROUP = 5.0                        # number of geom and site groups with visflags
MAXOVERLAY = 500.0                  # maximum number of characters in overlay text
MAXLINE = 100.0                     # maximum number of lines per plot
MAXLINEPNT = 500.0                  # maximum number points per line
MAXPLANEGRID = 100.0                # maximum number of grid points for plane rendering

###### const from enums ######

 # _mjtDisableBit
DSBL_CONSTRAINT = 0
DSBL_EQUALITY = 1
DSBL_FRICTIONLOSS = 2
DSBL_LIMIT = 3
DSBL_CONTACT = 4
DSBL_PASSIVE = 5
DSBL_GRAVITY = 6
DSBL_CLAMPCTRL = 7
DSBL_WARMSTART = 8
DSBL_FILTERPARENT = 9
DSBL_ACTUATION = 10
DSBL_REFSAFE = 11
NDISABLE = 12

 # _mjtEnableBit
ENBL_OVERRIDE = 0
ENBL_ENERGY = 1
ENBL_FWDINV = 2
ENBL_SENSORNOISE = 3
NENABLE = 4

 # _mjtJoint
JNT_FREE = 0
JNT_BALL = 1
JNT_SLIDE = 2
JNT_HINGE = 3

 # _mjtGeom
GEOM_PLANE = 0
GEOM_HFIELD = 1
GEOM_SPHERE = 2
GEOM_CAPSULE = 3
GEOM_ELLIPSOID = 4
GEOM_CYLINDER = 5
GEOM_BOX = 6
GEOM_MESH = 7
NGEOMTYPES = 8
GEOM_ARROW = 100
GEOM_ARROW1 = 101
GEOM_ARROW2 = 102
GEOM_LABEL = 103
GEOM_NONE = 1001

 # _mjtCamLight
CAMLIGHT_FIXED = 0
CAMLIGHT_TRACK = 1
CAMLIGHT_TRACKCOM = 2
CAMLIGHT_TARGETBODY = 3
CAMLIGHT_TARGETBODYCOM = 4

 # _mjtTexture
TEXTURE_2D = 0
TEXTURE_CUBE = 1
TEXTURE_SKYBOX = 2

 # _mjtIntegrator
INT_EULER = 0
INT_RK4 = 1

 # _mjtCollision
COL_ALL = 0
COL_PAIR = 1
COL_DYNAMIC = 2

 # _mjtCone
CONE_PYRAMIDAL = 0
CONE_ELLIPTIC = 1

 # _mjtJacobian
JAC_DENSE = 0
JAC_SPARSE = 1
JAC_AUTO = 2

 # _mjtSolver
SOL_PGS = 0
SOL_CG = 1
SOL_NEWTON = 2

 # _mjtImp
IMP_CONSTANT = 0
IMP_SIGMOID = 1
IMP_LINEAR = 2
IMP_USER = 3

 # _mjtRef
REF_SPRING = 0
REF_USER = 1

 # _mjtEq
EQ_CONNECT = 0
EQ_WELD = 1
EQ_JOINT = 2
EQ_TENDON = 3
EQ_DISTANCE = 4

 # _mjtWrap
WRAP_NONE = 0
WRAP_JOINT = 1
WRAP_PULLEY = 2
WRAP_SITE = 3
WRAP_SPHERE = 4
WRAP_CYLINDER = 5

 # _mjtTrn
TRN_JOINT = 0
TRN_JOINTINPARENT = 1
TRN_SLIDERCRANK = 2
TRN_TENDON = 3
TRN_SITE = 4
TRN_UNDEFINED = 1000

 # _mjtDyn
DYN_NONE = 0
DYN_INTEGRATOR = 1
DYN_FILTER = 2
DYN_USER = 3

 # _mjtGain
GAIN_FIXED = 0
GAIN_USER = 1

 # _mjtBias
BIAS_NONE = 0
BIAS_AFFINE = 1
BIAS_USER = 2

 # _mjtObj
OBJ_UNKNOWN = 0
OBJ_BODY = 1
OBJ_XBODY = 2
OBJ_JOINT = 3
OBJ_DOF = 4
OBJ_GEOM = 5
OBJ_SITE = 6
OBJ_CAMERA = 7
OBJ_LIGHT = 8
OBJ_MESH = 9
OBJ_HFIELD = 10
OBJ_TEXTURE = 11
OBJ_MATERIAL = 12
OBJ_PAIR = 13
OBJ_EXCLUDE = 14
OBJ_EQUALITY = 15
OBJ_TENDON = 16
OBJ_ACTUATOR = 17
OBJ_SENSOR = 18
OBJ_NUMERIC = 19
OBJ_TEXT = 20
OBJ_TUPLE = 21
OBJ_KEY = 22

 # _mjtConstraint
CNSTR_EQUALITY = 0
CNSTR_FRICTION_DOF = 1
CNSTR_FRICTION_TENDON = 2
CNSTR_LIMIT_JOINT = 3
CNSTR_LIMIT_TENDON = 4
CNSTR_CONTACT_FRICTIONLESS = 5
CNSTR_CONTACT_PYRAMIDAL = 6
CNSTR_CONTACT_ELLIPTIC = 7

 # _mjtConstraintState
CNSTRSTATE_SATISFIED = 0
CNSTRSTATE_QUADRATIC = 1
CNSTRSTATE_LINEARNEG = 2
CNSTRSTATE_LINEARPOS = 3
CNSTRSTATE_CONE = 4

 # _mjtSensor
SENS_TOUCH = 0
SENS_ACCELEROMETER = 1
SENS_VELOCIMETER = 2
SENS_GYRO = 3
SENS_FORCE = 4
SENS_TORQUE = 5
SENS_MAGNETOMETER = 6
SENS_RANGEFINDER = 7
SENS_JOINTPOS = 8
SENS_JOINTVEL = 9
SENS_TENDONPOS = 10
SENS_TENDONVEL = 11
SENS_ACTUATORPOS = 12
SENS_ACTUATORVEL = 13
SENS_ACTUATORFRC = 14
SENS_BALLQUAT = 15
SENS_BALLANGVEL = 16
SENS_FRAMEPOS = 17
SENS_FRAMEQUAT = 18
SENS_FRAMEXAXIS = 19
SENS_FRAMEYAXIS = 20
SENS_FRAMEZAXIS = 21
SENS_FRAMELINVEL = 22
SENS_FRAMEANGVEL = 23
SENS_FRAMELINACC = 24
SENS_FRAMEANGACC = 25
SENS_SUBTREECOM = 26
SENS_SUBTREELINVEL = 27
SENS_SUBTREEANGMOM = 28
SENS_USER = 29

 # _mjtStage
STAGE_NONE = 0
STAGE_POS = 1
STAGE_VEL = 2
STAGE_ACC = 3

 # _mjtDataType
DATATYPE_REAL = 0
DATATYPE_POSITIVE = 1
DATATYPE_AXIS = 2
DATATYPE_QUATERNION = 3

 # _mjtWarning
WARN_INERTIA = 0
WARN_CONTACTFULL = 1
WARN_CNSTRFULL = 2
WARN_VGEOMFULL = 3
WARN_BADQPOS = 4
WARN_BADQVEL = 5
WARN_BADQACC = 6
WARN_BADCTRL = 7
NWARNING = 8

 # _mjtTimer
TIMER_STEP = 0
TIMER_FORWARD = 1
TIMER_INVERSE = 2
TIMER_POSITION = 3
TIMER_VELOCITY = 4
TIMER_ACTUATION = 5
TIMER_ACCELERATION = 6
TIMER_CONSTRAINT = 7
TIMER_POS_KINEMATICS = 8
TIMER_POS_INERTIA = 9
TIMER_POS_COLLISION = 10
TIMER_POS_MAKE = 11
TIMER_POS_PROJECT = 12
NTIMER = 13

 # _mjtCatBit
CAT_STATIC = 1
CAT_DYNAMIC = 2
CAT_DECOR = 4
CAT_ALL = 7

 # _mjtMouse
MOUSE_NONE = 0
MOUSE_ROTATE_V = 1
MOUSE_ROTATE_H = 2
MOUSE_MOVE_V = 3
MOUSE_MOVE_H = 4
MOUSE_ZOOM = 5
MOUSE_SELECT = 6

 # _mjtPertBit
PERT_TRANSLATE = 1
PERT_ROTATE = 2

 # _mjtCamera
CAMERA_FREE = 0
CAMERA_TRACKING = 1
CAMERA_FIXED = 2
CAMERA_USER = 3

 # _mjtLabel
LABEL_NONE = 0
LABEL_BODY = 1
LABEL_JOINT = 2
LABEL_GEOM = 3
LABEL_SITE = 4
LABEL_CAMERA = 5
LABEL_LIGHT = 6
LABEL_TENDON = 7
LABEL_ACTUATOR = 8
LABEL_CONSTRAINT = 9
LABEL_SELECTION = 10
LABEL_SELPNT = 11
LABEL_CONTACTFORCE = 12
NLABEL = 13

 # _mjtFrame
FRAME_NONE = 0
FRAME_BODY = 1
FRAME_GEOM = 2
FRAME_SITE = 3
FRAME_CAMERA = 4
FRAME_LIGHT = 5
FRAME_WORLD = 6
NFRAME = 7

 # _mjtVisFlag
VIS_CONVEXHULL = 0
VIS_TEXTURE = 1
VIS_JOINT = 2
VIS_ACTUATOR = 3
VIS_CAMERA = 4
VIS_LIGHT = 5
VIS_CONSTRAINT = 6
VIS_INERTIA = 7
VIS_PERTFORCE = 8
VIS_PERTOBJ = 9
VIS_CONTACTPOINT = 10
VIS_CONTACTFORCE = 11
VIS_CONTACTSPLIT = 12
VIS_TRANSPARENT = 13
VIS_AUTOCONNECT = 14
VIS_COM = 15
VIS_SELECT = 16
VIS_STATIC = 17
NVISFLAG = 18

 # _mjtRndFlag
RND_SHADOW = 0
RND_WIREFRAME = 1
RND_REFLECTION = 2
RND_FOG = 3
RND_SKYBOX = 4
NRNDFLAG = 5

 # _mjtStereo
STEREO_NONE = 0
STEREO_QUADBUFFERED = 1
STEREO_SIDEBYSIDE = 2

 # _mjtGridPos
GRID_TOPLEFT = 0
GRID_TOPRIGHT = 1
GRID_BOTTOMLEFT = 2
GRID_BOTTOMRIGHT = 3

 # _mjtFramebuffer
FB_WINDOW = 0
FB_OFFSCREEN = 1

 # _mjtFontScale
FONTSCALE_100 = 100
FONTSCALE_150 = 150
FONTSCALE_200 = 200

 # _mjtFont
FONT_NORMAL = 0
FONT_SHADOW = 1
FONT_BIG = 2
