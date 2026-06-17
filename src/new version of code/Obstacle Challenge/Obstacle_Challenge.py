from pybricks.hubs import PrimeHub
from pybricks.messaging import AppData
from pybricks.parameters import Direction, Port, Color
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.tools import wait
from ustruct import unpack

# НАСТРОЙКА компонентов робота
# SETTING UP THE ROBOT COMPONENTS
hub = PrimeHub()
motor_steer = Motor(Port.B, Direction.CLOCKWISE)
motor_drive = Motor(Port.F, Direction.COUNTERCLOCKWISE) 

color_sensor = ColorSensor(Port.D)

# ПОДКЛЮЧЕНИЕ ИИ 
# AI CONNECTION
print(" waiting Bluetooth")
app = AppData([(1, 2)])
app.configure(1, 0, 'G2WUK8YVw')
wait(3000) 
print("ИИ готов")

# функция стабилизации курса для движения по отрицательным угловым координатам с нормализацией ошибки поворота рулевого сервопривода.
# heading stabilization function for navigating negative angular coordinates with steering error normalization.
def turn_to_angle(target):
    kp = -1.5
    
    while True:
        yaw_angle = hub.imu.heading()
        error = target - yaw_angle
        
        if error > 180:
            error -= 360
        elif error < -180:
            error += 360
            
        if abs(error) < 2:
            break
            
        steering = error * kp
        
        if steering > 52:
            steering = 52
        elif steering < -52:
            steering = -52
            
        motor_steer.track_target(steering)
        motor_drive.dc(40) 
        wait(10)

#ПОДГОТОВКА К СТАРТУ 
#PREPARING FOR THE START
wait(1000)
motor_steer.track_target(0)
hub.imu.reset_heading(0)
motor_drive.dc(35)

route = [90, 180, -90, 0]
current_target_angle = 0 #Угол, который робот должен держать на прямой  #The angle the robot should maintain on a straight line

# ГЛАВНЫЙ ЦИКЛ (2 КРУГА) 
# MAIN CYCLE (2 CIRCLES)
for lap in range(2):
    print(f"Начинаю круг {lap + 1}")
    
    for target_angle in route:
        # Переменные для объезда препятствий на прямой
        # Variables for avoiding obstacles on a straight line
        avoiding = False
        avoid_end_encoder = 0
        avoid_dir = 0 

        # прямо и проверка ИИ, пока не увидит линию
        # straight and check the AI ​​until it sees the line
        while True:
            # ПРОВЕРКА ЛИНИИ (Выход из цикла) \
            # LINE CHECK (Exit from the loop)
            detected_color = color_sensor.color()
            reflection = color_sensor.reflection()
            
            # Если видит линию И при этом не находится в процессе объезда
            # If it sees the line AND is not in the process of going around
            if not avoiding and (detected_color == Color.RED or reflection < 60):
                break
                
            # ЧТЕНИЕ ИИ 
            # READING AI
            data = app.get_bytes(1)
            pred = 4
            if data:
                try: 
                    pred, _ = unpack('BB', data)
                except: 
                    pass
            
            # Если видит блок (0 - Зеленый, 1 - Красный)
            # If it sees a block (0 - Green, 1 - Red)
            if not avoiding and pred in [0, 1]:
                avoid_dir = -1 if pred == 0 else 1 # Зеленый уходит влево (-1), Красный вправо (1) # Green goes left (-1), Red goes right (1)
                avoiding = True
                avoid_end_encoder = motor_drive.angle() + 450 # Дистанция объезда (градусы мотора) # Detour distance (motor degrees)
                
            # УПРАВЛЕНИЕ РУЛЕМ НА ПРЯМОЙ 
            # STEERING CONTROL ON A STRAIGHT LINE
            error = current_target_angle - hub.imu.heading()
            if error > 180: error -= 360
            elif error < -180: error += 360
            
            steering = 0
            
            # Небольшой П-регулятор, чтобы робот не сбивался с курса на прямой
            # A small P-controller to keep the robot on course when driving straight
            if abs(error) > 1.5: 
                steering = error * (-1.0) # Коэффициент слабее, чем в поворотах # The coefficient is weaker than in corners
                
            # Если объезжает, жестко добавляет угол руля в нужную сторону
            # If it goes around, it rigidly adds the steering angle to the desired direction
            if avoiding:
                steering += (avoid_dir * 40)
                # Проверяет, проехал ли нужную дистанцию для объезда
                # Checks whether have traveled the required distance for a detour
                if motor_drive.angle() > avoid_end_encoder:
                    avoiding = False
            
            # Ограничиваем руль 
            # Limit the steering wheel 
            motor_steer.track_target(max(min(steering, 52), -52))
            motor_drive.dc(40)
            wait(10)
             
        # Выполняет поворот на заданный угол
        # Performs a turn at a specified angle
        turn_to_angle(target_angle)
        current_target_angle = target_angle # Обновляет текущий курс # Updates the current rate
        
        # Съезжаеи с линии, чтобы не прочитать ее второй раз
        # Move off the line so as not to read it a second time
        motor_steer.track_target(0)
        motor_drive.dc(35)
        wait(400)

# ФИНИШ 
# FINISH
wait(2000)
motor_drive.dc(0)
motor_steer.track_target(0)
print("Гонка завершена!")