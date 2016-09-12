import os
import pygame,random
from  pygame.locals import *
from sys import exit
from random import randint
import level1
import level2
import level3
 

# making out the starting screen

while True:
     pygame.init()
     screen=pygame.display.set_mode((640,480),0,24)
     caption=pygame.display.set_caption("Deadly Snake")
     f=pygame.font.SysFont("comicsansms",50)
     text1=f.render("Deadly Snake",True,(0,255,0))
     clock=pygame.time.Clock()
     start=pygame.font.SysFont("comicsansms",30)
     text2=start.render("Press s to start",True,(0,255,0))
     q=pygame.font.SysFont("comicsansms",30)
     text3=q.render("Press q to quit",True,(0,255,0))
     s=[[300,200],[280,200],[260,200],[240,200],[220,200],[200,200],[180,200],[180,220],[160,220],[140,220],[120,220],[120,240],[100,240]]
     a=[100,240]
     pygame.draw.rect(screen,(255,0,0),Rect(a,[20,20]),0)
     screen.blit(text1,(60,60))
     screen.blit(text2,(300,300))
     screen.blit(text3,(300,350))
     for i in s:
         pygame.draw.rect(screen,(0,255,0),Rect(i,[20,20]),0)
         pygame.display.flip()
         clock.tick(10)
     pygame.display.flip()

    #event handling (Key events)
     while True:
         for i in pygame.event.get():
             if i.type==QUIT:
                 exit()
         pressed=pygame.key.get_pressed()
         if pressed[K_q]:
             exit()
         if pressed[K_s]:
             break
         

    
     while True:
        press=pygame.key.get_pressed()
        for i in pygame.event.get():
            if i.type==QUIT or  press[K_q]:
                exit()
        screen.fill((0,0,0))
        mousepress=pygame.mouse.get_pressed()
        l1=pygame.font.SysFont("comicsansms",50)
        l2=pygame.font.SysFont("comicsansms",30)
        l3=pygame.font.SysFont("comicsansms",30)
        l4=pygame.font.SysFont("comicsansms",30)
        l5=pygame.font.SysFont("comicsansms",30)
        r2=Rect((100,200),l2.size("Press 1 for Level 1 "))
        r3=Rect((100,250),l3.size("Press 2 for Level 2 "))
        r4=Rect((100,300),l3.size("Press 3 for Level 3 "))
        r5=Rect((100,350),l3.size("Press m for Multiplayer "))
        screen.blit(l1.render("Select Your Level",True,(0,255,0)),(100,100))
        screen.blit(l2.render("Press 1 for Level 1 ",True,(0,255,0)),(100,200))
        screen.blit(l3.render("Press 2 for level 2 ",True,(0,255,0)),(100,250))
        screen.blit(l4.render("Press 3 for level 3 ",True,(0,255,0)),(100,300))
        screen.blit(l5.render("Press m for multiplayer ",True,(0,255,0)),(100,350))
        pygame.display.update()
         
        if press[K_1] or  (r2.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
                level1.main()
        if press[K_2] or  (r3.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
                level2.main()
        if press[K_3] or  (r4.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
                level3.main()
        if press[K_m] or  (r5.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
                sounds = {
                        "eat": None,
                        "crash": None,
                        }

                def load_sound(path, name):
                    fullname = os.path.join('data', name)
                    sound = pygame.mixer.Sound(fullname)
                    return sound

                def load_resources(path="data"):
                    sounds["eat"] = load_sound(path, "eat.wav")
                    sounds["die"] = load_sound(path, "die.wav")
                    sounds["alarm"] = load_sound(path, "attention.wav")
                
                def collide(x1, x2, y1, y2, w1, w2, h1, h2):
                    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
                        return True
                    else:
                        return False

                FIELD_WIDTH = 800
                FIELD_HEIGHT = 600        
                APPLE_SIZE = 10
                SEGMENT_SIZE = 20
                INITIAL_SNAKE_LENGTH = 10
                ADVANTAGE = 5
                ADVANTAGE_CNT = 300
                NUM_APPLES = 4

                colors = {
                    "red": (255,0,0),
                    "green": (0,255,0),
                    "blue": (0,0,255),
                    "yellow": (255, 255, 0),
                    "white": (255,255,255),
                    "black": (0,0,0),
                    "magenta": (255,0,255),
                    "cyan": (0,255,255),
                }

                class Dir:
                    
                    DOWN = "down"
                    UP = "up"
                    RIGHT = "right"
                    LEFT = "left"
                    
                    @staticmethod
                    def to_P2(direction):
                        return {Dir.DOWN: P2(0, 1),
                                Dir.UP: P2(0,-1),
                                Dir.RIGHT: P2(1, 0),
                                Dir.LEFT: P2(-1,0),
                               }[direction]

                class P2(object):
                    def __init__(self, x, y):
                        self.x = x
                        self.y = y
                    def __add__(self, other):
                        return P2(self.x + other.x, self.y + other.y)
                    def __sub__(self, other):
                        return P2(self.x - other.x, self.y - other.y)
                    def __mul__(self, factor):
                        return P2(self.x*factor, self.y*factor)
                        
                    def __eq__(self, other):
                        return self.x == other.x and self.y == other.y
                        
                    def __str__(self):
                        return "P2(%s,%s)" % (self.x, self.y)
                        
                class MyRect(object):
                    def __init__(self, upperleft, size):
                        self.upperleft = uppperleft
                        self.size = size

                    def contains(self, p):
                        return p.x >= self.upperleft.x \
                           and p.y >= self.upperleft.y \
                           and p.x < self.upperleft.x + self.size.x \
                           and p.y < self.upperleft.y + self.size.y           

                    def collides_with(self, other):
                        print "TODO"
                        return False
                    
                           
                class Snake(object):
                    def __init__(self, headpos, length, direction, color):
                        self.to_grow = 0
                        self.grow_speed = 1
                        self.direction = direction
                        taildir = Dir.to_P2(direction) * (-SEGMENT_SIZE)
                        segments = []
                        pos = headpos
                        for i in range(length):
                            segments.append(pos)
                            pos += taildir
                        self.segments = segments
                        self.slow_factor = 1
                        self.wait_cycles = 1
                        self.segment_image = pygame.Surface((SEGMENT_SIZE, SEGMENT_SIZE))
                        self.segment_image.fill(color)
                        #print "Created " + self.dump()
                    
                    def length(self):
                        return len(self.segments)
                        
                    def dump(self):
                        o = []
                        o.append("Snake(len=%d)" % self.length())
                        for s in self.segments: o.append("(%d,%d)" % (s.x, s.y))
                        return "".join(o)

                class PlayerSnake(Snake):
                    pass

                class BotSnake(Snake):
                    pass    

                class PlayerBase(object):
                    def __init__(self, name, color, snakeClass):
                        self.name = name
                        self.score = 0
                        self.sum_score = 0
                        self.snake = None
                        self.snakeClass = snakeClass
                        self.color = color

                    def createSnake(self, headpos, direction):
                        self.snake = self.snakeClass(headpos, INITIAL_SNAKE_LENGTH, direction, self.color)

                    def in_game_update(self, game):
                        pass    
                            
                class Human(PlayerBase):
                    def __init__(self, name, color, controls):
                        super(Human, self).__init__(name, color, PlayerSnake)
                        self.controls = controls

                    def in_game_update(self, game):
                        snake = self.snake
                        controls = self.controls
                        for key in game.keys_pressed:
                                if key == controls[Dir.UP] and snake.direction != Dir.DOWN: snake.direction = Dir.UP
                                elif key == controls[Dir.DOWN] and snake.direction != Dir.UP: snake.direction = Dir.DOWN
                                elif key == controls[Dir.LEFT] and snake.direction != Dir.RIGHT: snake.direction = Dir.LEFT
                                elif key == controls[Dir.RIGHT] and snake.direction != Dir.LEFT: snake.direction = Dir.RIGHT
                        
                class Bot(PlayerBase):        
                    """
                    The bot snake crawls straight forward
                    but takes care not to run into the border.
                    It does not avoid other snakes.
                    """
                    def __init__(self, name, color):
                        super(Bot, self).__init__(name, color, BotSnake)

                    def in_game_update(self, game):
                        d = self.snake.direction
                        head = self.snake.segments[0]
                        if d == Dir.DOWN and head.y > FIELD_HEIGHT - 2*SEGMENT_SIZE or d == Dir.UP and head.y < SEGMENT_SIZE:
                            #print head
                            self.choose_dir(head.x, FIELD_WIDTH, Dir.LEFT, Dir.RIGHT)
                        elif d == Dir.RIGHT and head.x > FIELD_WIDTH - 2*SEGMENT_SIZE or d == Dir.LEFT and head.x < SEGMENT_SIZE:
                            #print head
                            self.choose_dir(head.y, FIELD_HEIGHT, Dir.UP, Dir.DOWN)
                                
                    def choose_dir(self, pos, maxpos, decrease, increase):
                        print "choose_dir", pos, decrease, "or", increase
                        if pos < 2 * SEGMENT_SIZE:
                            print increase
                            self.snake.direction = increase
                        elif pos > maxpos - 2*SEGMENT_SIZE:
                            print decrease
                            self.snake.direction = decrease
                        else:
                            d = random.choice([decrease, increase])
                            print "rnd", d
                            self.snake.direction = d

                        
                arrowKeys = {Dir.UP: K_UP, Dir.DOWN: K_DOWN, Dir.LEFT: K_LEFT, Dir.RIGHT: K_RIGHT}
                wasdKeys =  {Dir.UP: K_w, Dir.DOWN: K_s, Dir.LEFT: K_a, Dir.RIGHT: K_d}
                
                players = [Human("TESSIO", colors["blue"], arrowKeys), Human("CLEMENZA", colors["green"], wasdKeys)]

                class Game(object):
                    def __init__(self):
                        self.key_pressed = []
                        self.apples = []
                        for i in range(NUM_APPLES):
                            self.spawn_apple()
                        self.living = []
                        self.survivor = None
                        self.survival_countdown = 300 
                        self.spawn_apple()
                        self.leader = None
                        self.advantage_count = None
                        self.over = False

                    def spawn(self, player):
                        player.sum_score += player.score
                        player.score = 0
                        self.living.append(player)
                        
                    def die(self, player):
                        print "Player %s died." % player.name
                        sounds["die"].play()
                        self.living.remove(player)
                        
                        (r,g,b) = player.color
                        r = r/4
                        g = g/4
                        b = b/4
                        img = pygame.Surface((SEGMENT_SIZE, SEGMENT_SIZE))
                        img.fill((r,g,b))
                        player.snake.segment_image = img
                        
                    def spawn_apple(self):
                        self.apples.append (P2(random.randint(0, FIELD_WIDTH - APPLE_SIZE), random.randint(0, FIELD_HEIGHT - APPLE_SIZE)))

                    def update(self):
                        self.over = False
                        
                        self.keys_pressed = []
                        for e in pygame.event.get():
                            if e.type == QUIT:
                                sys.exit(0)
                            elif e.type == KEYDOWN:
                                self.keys_pressed.append(e.key)

                        
                        sorted_by_score = self.living[:]
                        sorted_by_score.sort(key=lambda p: -p.score)
                    
                        if len(sorted_by_score) > 1:
                            new_leader = sorted_by_score[0]
                            if sorted_by_score[0].score >= sorted_by_score[1].score + ADVANTAGE:
                                if new_leader != self.leader:
                                    self.leader = new_leader
                                    self.advantage_count = ADVANTAGE_CNT
                                    sounds["alarm"].play()
                                else:
                                    self.advantage_count -= 1
                                    if self.advantage_count == 0:
                                        print "Game ends - %s has kept the leadership for %s frames!" % (self.leader.name, ADVANTAGE_CNT)
                                        self.over = True
                                self.leader = sorted_by_score[0]
                        else:
                            self.leader = None
                            self.advantage_count = None
                         
                        if not self.living:
                            "Game ends - noone left alive"
                            self.over = True
                        elif len(self.living) == 1:
                            if not self.survivor:
                                self.survivor = self.living[0]
                            else:
                                self.survival_countdown -= 1
                                if not self.survival_countdown:
                                    print "Game ends: %s is the last survivor" % self.survivor.name
                                    self.survivor.score += 10
                                    self.over = True
                    
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                pygame.init()
                load_resources("data")
                s=pygame.display.set_mode((FIELD_WIDTH, FIELD_HEIGHT))
                pygame.display.set_caption('Deadly Snake')
                appleimage = pygame.Surface((APPLE_SIZE, APPLE_SIZE))
                appleimage.fill(colors["red"])
                font = pygame.font.SysFont('Arial', 20)
                clock = pygame.time.Clock()

                def play_level():
                    game=Game()
                    for pnum, player in enumerate(players):
                        headpos = P2(FIELD_WIDTH/2, FIELD_HEIGHT/2) + P2(2*pnum*SEGMENT_SIZE, 0)
                        direction = [Dir.UP, Dir.DOWN][pnum%2]
                        player.createSnake(headpos, direction)   
                        game.spawn(player)
                    players[0].snake.slow_factor = 6
                    players[1].snake.slow_factor = 6 

                    while not game.over:
                        clock.tick(60)
                        game.update()
                        
                        if K_ESCAPE in game.keys_pressed:
                            print "Game cancelled."
                            for player in game.living[:]:
                                game.die(player)
                                    
                        for player in game.living:
                            player.in_game_update(game)

                            snake = player.snake
                            head = snake.segments[0]
                            
                            for other_player in players:
                                other_snake = other_player.snake
                                for segment in other_snake.segments:
                                    
                                    collision = (segment == head)
                                    if collision and not (segment is head): 
                                        print "%s runs into %s" % (player.name, other_player.name)
                                        #print "%s head @ %s, %s segment @ %s" % (player.name, head, other_player.name, segment)
                                        game.die(player)
                                        if other_player is not player:
                                            other_player.score += 5
                            
                            
                            for apple in game.apples:
                                if collide(head.x, apple.x, head.y, apple.y, SEGMENT_SIZE, APPLE_SIZE, SEGMENT_SIZE, APPLE_SIZE):
                                    #print "%s eats apple @ %s" % (player.name, apple)
                                    sounds["eat"].play()
                                    game.apples.remove(apple)
                                    player.score += 1
                                    snake.to_grow += 1
                                    game.spawn_apple()

                            
                            if head.x < 0 or head.x > FIELD_WIDTH - SEGMENT_SIZE or head.y < 0 or head.y > FIELD_HEIGHT - SEGMENT_SIZE:
                                print "%s runs into border." % player.name
                                game.die(player)

          
                            snake = player.snake
                            snake.wait_cycles -= 1
                            if snake.wait_cycles > 0:
                                continue 
                            snake.wait_cycles = snake.slow_factor
                            
                            
                            d = Dir.to_P2(snake.direction) * SEGMENT_SIZE
                            old_head = snake.segments[0]
                            new_head = old_head + d
                            
                            snake.segments.insert(0, new_head)
                            if snake.to_grow > 0 and True:
                                snake.to_grow -= 1
                            else:
                                snake.segments.pop() 
                        
                    
                        s.fill((0, 0, 0))
                        for plnum, player in enumerate(players):
                            snake = player.snake
                            img = snake.segment_image
                            for segment in snake.segments:
                                s.blit(img, (segment.x, segment.y))
                            txt = font.render("%s: %s" % (player.name, player.score), True, colors["yellow"]) 
                            s.blit(txt, (10 + 400*(plnum%2), 10+(400*int(plnum/2)%2)))
                        for apple in game.apples:
                            s.blit(appleimage, (apple.x, apple.y))
                        
          
                        if game.advantage_count is not None:
                            txt = font.render("*" * int(game.advantage_count/2), True, game.leader.color)
                            s.blit(txt, (10, 30))
                        
                        pygame.display.update()
                        

                    pygame.time.wait(2000)
                    print "Scores:"
                    for player in players:
                        player.sum_score += player.score
                        print "%20s %10d %10d" % (player.name, player.score, player.sum_score)
                        player.score = 0

                for stage in range(5):
                    play_level()
                        
                sys.exit(0)
                 
             
