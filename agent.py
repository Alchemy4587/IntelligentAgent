import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

min_x, min_y = 0, 0
max_x, max_y = WIDTH, HEIGHT



def canMove(new_x, new_y, world, visited):
    # Check if the new position is within bounds
    if min_x <= new_x < max_x and min_y <= new_y < max_y:
        row = (new_y) // 40  # Adjusted for y-offset starting at 40
        col = new_x // 40

        # Check if the cell is free and not already visited
        if world[row][col] != 0:
            for node in visited:
                if(node[0]==row and node[1]==col):
                    return False
            print(f"Presently at [{row}, {col}]. Can move.")
            return True
    return False
def getIndex(x,y,visited):
    prev = [(y) // 40, x // 40]
    for node in visited:
        if node[0] == prev[0] and node[1] == prev[1]:
            return visited.index(node)


class Agent:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.foundTarget = False
        self.noPath = False
        self.rect = self.image.get_rect(topleft=(x, y))
        self.visited = [[(y) // 40, x // 40,None]]  # Store as [row, col]

    def move(self, world):
        print(self.visited)
        directions = [
            (0, -40),  # Up
            (40, 0),  # Right
            (0, 40),  # Down
            (-40, 0)  # Left
        ]

        for direction in directions:

            prev_index= getIndex(self.x,self.y,self.visited)
            new_x = self.x + direction[0]
            new_y = self.y + direction[1]

            if canMove(new_x, new_y, world, self.visited):
                self.x, self.y = new_x, new_y
                row = (self.y) // 40
                col = self.x // 40
                self.visited.append([row, col,prev_index])

                if(world[row][col]==2):
                    self.foundTarget= True

                print(f"Moved to: [{row}, {col}]")
                return

        # Backtrack if no direction is possible
        if len(self.visited) > 1:
         # Remove current position from visited
            index=getIndex(self.x,self.y,self.visited)
            if(index==0):
                self.noPath = True
                return
            position = self.visited[index]
            next = self.visited[position[2]]
            self.x = next[1] * 40
            self.y = (next[0] * 40) 

            print(f"Backtracked to: [{self.x}, {self.y}]")
        else:
            print("No movement possible; already at starting point.")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
