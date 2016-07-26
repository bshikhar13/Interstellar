#Interstellar
#Shikhar Bansal
#Shweta Katheria
#Dr. Somnath Dey
#IIT Indore
#Computer Graphics Project 2015

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math
from OpenGL.GLUT import *
import string, time




vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )




edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )


colors = (
    (0,1,0),
    (1,0,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

ground_surfaces = (0,1,2,3)

ground_vertices = (
    (-10000,-1,50),
    (10000,-1,50),
    (-10000,-1,-3000),
    (10000,-1,-3000),

    )

def Ground():
    
    glBegin(GL_QUADS)

    
    for vertex in ground_vertices:
       
        glColor3fv((0,0,1))
        glVertex3fv(vertex)
        
    glEnd()
    


def Cube():
    glBegin(GL_QUADS)
    
    for surface in surfaces:

        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
        
    glEnd()
    


    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    



def set_vertices(max_distance):
    x_value_change = random.randrange(-20,20)
    y_value_change = 0#random.randrange(-10,10)
    z_value_change = random.randrange(-1*max_distance,-20)


    
    new_vertices = []
    for vert in vertices:
        new_vert = []
        
        
        new_x= vert[0] + x_value_change
        new_y= vert[1] + y_value_change
        new_z= vert[2] + z_value_change
        

        
        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices




def Cubes(new_vertices):
    
    glBegin(GL_QUADS)
    
    for surface in surfaces:
        x = 0

        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(new_vertices[vertex])
            
        
    glEnd()

# CUT LINES BC THEY HURT PROCESSING
##    glBegin(GL_LINES)
##    for edge in edges:
##        for vertex in edge:
##            glVertex3fv(new_vertices[vertex])
##    glEnd()

    


def main():
    pygame.init()
    display = (800,600)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)
    glTranslatef(random.randrange(-50,50),0, -100)
   



    x_move = 0
    y_move = 0
    hit=0
    max_distance = 1000

    
    cube_dict = {}

    for x in range(70):
        cube_dict[x] = set_vertices(max_distance)

    number_of_hits = 0;
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_move = 2.0
                    
                if event.key == pygame.K_RIGHT:
                    x_move = -2.0

                #if event.key == pygame.K_UP:
                    #y_move = -0.3

               # if event.key == pygame.K_DOWN:
                    #y_move = 0.3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_move = 0
                    
                if event.key == pygame.K_RIGHT:
                    x_move = 0

                #if event.key == pygame.K_UP:
                    #y_move = 0

                #if event.key == pygame.K_DOWN:
                    #y_move = 0


        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        x = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        print (camera_x)
        print (camera_y)
        print (camera_z)
        fo = open("log/foo.txt", "a+")
        #print "Name of the file: ", fo.name
        fo.write("\nX : ")
        fo.write(str(camera_x))
        fo.write("\nY : ")
        fo.write(str(camera_y))
        fo.write("\nZ : ")
        fo.write(str(camera_z))
        fo.write("\nCube : ")
        
        
        glTranslatef(x_move,y_move,3)

                
        
        Ground()
       
        
   
        hitted=False
        track=0
        for each_cube in cube_dict:
            
            Cubes(cube_dict[each_cube])
            yo = cube_dict[each_cube][0][0]
            fo.write(str(yo))
            yo = cube_dict[each_cube][2][0]
            midpoint = yo+1
            fo.write(str(yo))
            fo.write("\npoo ")
            fo.write(str(cube_dict[each_cube][2][2]))
            fo.write("\n\n")
          
            if math.floor(camera_z) <= cube_dict[each_cube][2][2]:
               
                hitted = True
                track=track+1
            if math.floor(camera_z) >= cube_dict[each_cube][2][2]-2 and math.floor(camera_z) <= cube_dict[each_cube][2][2]+2 and cube_dict[each_cube][2][0] <= math.floor(camera_x)+0.5 and cube_dict[each_cube][2][0] >= math.floor(camera_x)-0.5: 
                number_of_hits=number_of_hits+1
        pygame.display.flip()

        if hitted == True:
            hit=hit+1

        pygame.display.set_caption("Energy Passed : "+str(track)+" | Score : " +str(number_of_hits))
      
        #drawText( track, 10,20, self.viewportDimensions[0],self.viewportDimensions[1])
        
        

main()
