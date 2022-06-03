def color_grad(c_1,c_2,length):
    d_r = (c_2[0]-c_1[0])/length
    d_g = (c_2[1]-c_1[1])/length
    d_b = (c_2[2]-c_1[2])/length
    
    colors= []
    
    for i in range(length):
        colors.append((c_1[0]+d_r*i,c_1[1]+d_g*i,c_1[2]+d_b*i))
        
    return colors


def palette(stops = [[(0,0,0),0],[(255,255,255),1000],[(0,0,0),2000]]):
    counter = 0 
    final = []
    
    for s in range(len(stops)-1):
        length = stops[s+1][1]-stops[s][1]
        gradient = color_grad(stops[s][0],stops[s+1][0],length)
        counter_1 = counter
        for color in gradient:
            final.append(color)
            counter +=1
        
    return final
    
if __name__ == '__main__':
    
    import pygame
    pygame.init()


    screen = pygame.display.set_mode([500, 80])


    running = True
    while running:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        
        #to_draw = color_grad((159,133,85),(134,3,155),500)
        to_draw = palette([[[0,0,0],0],[[255,0,0],75],[[255,255,0],150],[[255,255,255],250],[[255,255,0],350],[[255,0,0],425],[[0,0,0],500]])
        
        for line in range(len(to_draw)):
            pygame.draw.line(screen,to_draw[line],(line,0),(line,80),1)

        
        pygame.display.flip()


    pygame.quit() 
    
 
    
