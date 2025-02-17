import obd
import pygame
import pyttsx3
import csv
import platform
from datetime import datetime
from pid_config import PIDS, DEFAULT_PIDS

# Detect system
system = platform.system()
if system == "Windows":
    # Windows specific settings
    print("Running on Windows")
else:
    # Raspberry Pi specific settings
    print("Running on Raspberry Pi")
    import RPi.GPIO as GPIO  # Example library for Raspberry Pi GPIO

# Initialize OBD-II connection (SAE J1850 VPW protocol assumed)
connection = obd.OBD(protocol=obd.protocols.SAE_J1850_VPW)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Futuristic Instrument Cluster")

# Initialize Text-to-Speech
engine = pyttsx3.init()

# Data logging setup
log_file = open('datalog.csv', mode='w')
log_writer = csv.writer(log_file)
log_writer.writerow(['Time', 'PID', 'Value'])

# Current PIDs to display
current_pids = DEFAULT_PIDS.copy()

def check_thresholds(pid, value):
    if pid in PIDS and value > PIDS[pid]['threshold']:
        engine.say(f"Warning: {pid} is above threshold!")
        engine.runAndWait()

def log_data(pid, value):
    log_writer.writerow([datetime.now(), pid, value])

def get_obd_data():
    data = {}
    for pid in current_pids:
        command = getattr(obd.commands, PIDS[pid]['command'])
        response = connection.query(command)
        if response.value:
            data[pid] = response.value.magnitude
            check_thresholds(pid, data[pid])
            log_data(pid, data[pid])
    return data

def draw_gauge(screen, label, value, position):
    font = pygame.font.Font(None, 36)
    text = font.render(f"{label}: {value}", True, (255, 255, 255))
    screen.blit(text, position)

def draw_histogram(screen, data, position):
    max_value = max(data.values()) if data else 1
    bar_width = 50
    gap = 10
    x, y = position
    for pid, value in data.items():
        bar_height = int((value / max_value) * 100)
        pygame.draw.rect(screen, (0, 255, 0), (x, y - bar_height, bar_width, bar_height))
        x += bar_width + gap

def draw_ui(screen, data):
    screen.fill((0, 0, 0))
    y_offset = 50
    for pid in current_pids:
        draw_gauge(screen, pid, data.get(pid, 'N/A'), (50, y_offset))
        y_offset += 100
    draw_histogram(screen, data, (400, 200))
    pygame.display.flip()

def handle_touch(event):
    global current_pids
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if 700 <= x <= 780 and 10 <= y <= 50:
            # Toggle PID selection screen
            current_pids = pid_selection_screen()

def pid_selection_screen():
    selected_pids = current_pids.copy()
    font = pygame.font.Font(None, 36)
    while True:
        screen.fill((0, 0, 0))
        y_offset = 50
        for pid in PIDS.keys():
            color = (0, 255, 0) if pid in selected_pids else (255, 0, 0)
            text = font.render(pid, True, color)
            screen.blit(text, (50, y_offset))
            y_offset += 50
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 200:
                    index = (y - 50) // 50
                    pid_list = list(PIDS.keys())
                    if index < len(pid_list):
                        pid = pid_list[index]
                        if pid in selected_pids:
                            selected_pids.remove(pid)
                        else:
                            selected_pids.append(pid)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return selected_pids

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_touch(event)

    data = get_obd_data()
    draw_ui(screen, data)
    pygame.time.wait(100)

log_file.close()
pygame.quit()