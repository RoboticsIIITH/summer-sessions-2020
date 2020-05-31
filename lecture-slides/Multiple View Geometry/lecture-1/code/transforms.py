import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


'''
Coded with love by Rahul Sajnani
'''

def drawAxis(points_3D_homogeneous):

    '''

    Function to draw axis for different cameras and origin 
    Input:
        points_3D_homogeneous - 4 x 4 - 3D homogeneous points in the given order
            
            1) origin [X Y Z 1] **column vector**
            2) x - axis 
            3) y - axis 
            4) z - axis 
    
    Returns:
        None

    '''

    
    
    line_ox = np.array([[points_3D_homogeneous[0, 0], points_3D_homogeneous[1,  0], points_3D_homogeneous[2,  0]],
                        [points_3D_homogeneous[0, 1], points_3D_homogeneous[1,  1], points_3D_homogeneous[2,  1]]])

    ax.plot3D(line_ox[:, 0], line_ox[:, 1], line_ox[:, 2], 'red')
    
    
    line_oy = np.array([[points_3D_homogeneous[0, 0], points_3D_homogeneous[1,  0], points_3D_homogeneous[2,  0]],
                        [points_3D_homogeneous[0, 2], points_3D_homogeneous[1,  2], points_3D_homogeneous[2,  2]]])
    
    ax.plot3D(line_oy[:, 0], line_oy[:, 1], line_oy[:, 2], 'green')


    line_oz = np.array([[points_3D_homogeneous[0,  0], points_3D_homogeneous[1,  0], points_3D_homogeneous[2,  0]],
                        [points_3D_homogeneous[0,  3], points_3D_homogeneous[1,  3], points_3D_homogeneous[2,  3]]])
    
    ax.plot3D(line_oz[:, 0], line_oz[:, 1], line_oz[:, 2], 'blue')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_zlim(-2.0, 2.0)
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 2.0)

def rotateAxis(degrees, axis):
    '''
    Function to rotate around given axis

    Input:
        degrees - scalar - Angle in degrees
        
        axis - scalar - options:
            0 - around x axis
            1 - around y axis
            2 - around z axis  
    
    Returns:
        Homogeneous rotation matrix
    '''

    radians = np.radians(degrees)

    if axis == 2: # z - axis

        rotation_mat = np.array([[np.cos(radians), -np.sin(radians),           0,          0],
                                 [np.sin(radians),  np.cos(radians),           0,          0],
                                 [              0,                0,           1,          0],
                                 [              0,                0,           0,          1]])

    elif axis == 1: # y - axis

        rotation_mat = np.array([[np.cos(radians),                0,  np.sin(radians),          0],
                                 [              0,                1,                0,          0],
                                 [-np.sin(radians),               0, np.cos(radians),          0],
                                 [              0,                0,                0,          1]])

    elif axis == 0: # x - axis


        rotation_mat = np.array([[             1,                0,                0,          0],
                                [              0,  np.cos(radians), -np.sin(radians),          0],
                                [              0,  np.sin(radians),  np.cos(radians),          0], 
                                [              0,                0,                0,          1]])
    
    return rotation_mat

def translateMatrix(x, y, z):

    translation_matrix = np.eye(4)
    translation_matrix[0,3] += x
    translation_matrix[1,3] += y
    translation_matrix[2,3] += z

    return translation_matrix


if __name__ == "__main__":
    

    #                                        o  x  y  z

    points_3D_homogeneous_world = np.array([[0, 1, 0, 0],
                                            [0, 0, 1, 0],
                                            [0, 0, 0, 1],
                                            [1, 1, 1, 1]])   # <======== appending 1 as homogeneous coordinates

    points_3D_homogeneous_camera = points_3D_homogeneous_world.copy()

    fig = plt.figure()
    fig.suptitle('Frame transforms')
    
    ############################ INITIAL SYSTEM  ####################################################
    ax = fig.add_subplot(1, 3, 1, projection='3d')
    
    # Drawing world origin here
    drawAxis(points_3D_homogeneous_world)
    transformation_matrix = np.eye(4)
    rotation_mat = rotateAxis(90, 0)
    translation_mat = translateMatrix(1, 1, 0)

    # perform frame translation 
    # NOTE: This transformation matrix (frame) bring the coordinate system from WORLD FRAME to CAMERA FRAME

                            ####### IMPORTANT ########
    #  Since frame transforms are INVERSE of point transforms it brings POINTS from CAMERA to WORLD 
    transformation_matrix = translation_mat

    # Multiplying the transformtion matrix to POINTS in CAMERA to bring to WORLD
    drawAxis(transformation_matrix @ points_3D_homogeneous_camera)
    plt.title('Initial system')
    
    ############################## POST MULTIPLYING ################################################
    ax = fig.add_subplot(1, 3, 2, projection='3d')    
    drawAxis(points_3D_homogeneous_world)
    transformation_matrix = np.eye(4)
    rotation_mat = rotateAxis(90, 0)
    translation_mat = translateMatrix(1, 1, 0)


    # perform frame translation first then rotation along x axis
    # NOTE: This transformation matrix (frame) bring the coordinate system from WORLD FRAME to CAMERA FRAME
    # Since frame transforms are INVERSE of point transforms it brings POINTS from CAMERA to WORLD 
    transformation_matrix = translation_mat @ rotation_mat
    drawAxis(transformation_matrix @ points_3D_homogeneous_camera)
    plt.title('Post multiplying (around camera frame)')
    
    
    ############################## PRE MULTIPLYING ################################################
    
    ax = fig.add_subplot(1, 3, 3, projection='3d')
    drawAxis(points_3D_homogeneous_world)
    transformation_matrix = np.eye(4)
    rotation_mat = rotateAxis(90, 0)
    translation_mat = translateMatrix(1, 1, 0)


    # perform frame rotation along x axis first then translation 
    # NOTE: This transformation matrix (frame) bring the coordinate system from WORLD FRAME to CAMERA FRAME
    # Since frame transforms are INVERSE of point transforms it brings POINTS from CAMERA to WORLD
    transformation_matrix = rotation_mat @ translation_mat
    drawAxis(transformation_matrix @ points_3D_homogeneous_camera)
    plt.title('Pre multiplying (around world origin)')
    plt.show()

