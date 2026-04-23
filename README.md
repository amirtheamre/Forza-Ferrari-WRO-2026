
Engineer's Documentation
====

 This repository contains materials from the Forza Ferrari team participating in the Future Engineers section, creating a self-driving car, for the 2026 WRO season.

 ## Content

* `t-photos` contains 2 photos of the team (one of which is official and the other unofficial, both photos include all team members)
* `v-photos` contains 6 photos of the robot (on each side of the robot, top and bottom), as well as detailed instructions for assembling the main components of our robot
* `video` contains a file video.md with a link to a video of the robot riding
* `schemes` contains photos with all the electrical components that were used and how they are used in our robot and are interconnected
* `src` contains the code, the program for all components of the robot with explanations in the code
* `other` description of how the components were connected to each other and how the interaction is performed

## Our motivation:

 We are two friends and both Formula 1 fans, specifically of the Ferrari team (which is quite evident from our name). Recently, there was a significant event in motorsport, the first race of Formula 1 cars controlled by artificial intelligence (Abu Dhabi Autonomous Racing League (A2RL)). Equally important, this race took place on the track in Abu Dhabi, UAE, one of the most challenging and demanding tracks in terms of driving skills. 
 
 After witnessing this, we became curious about whether it was possible for us to design a vehicle that is also fully autonomous. In the category of Future Engineers, WRO, we will have the opportunity to fully test our ideas with limited access to resources compared to the A2RL races.
 
 As a result, you will be able to see the outcomes of our efforts in this Github repository.
 
## Introduction

 The first version of our robot for participation in the regional qualifiers was created from parts of the LEGO EV3 set, however, faced with major problems and critical errors, we decided to completely reconsider our decision. Later, we discovered the LEGO SPIKE sets, which, unlike the LEGO EV3 set, continued to be supported by LEGO, and the parts of this set were of higher quality compared to the parts of the LEGO EV3 set. 
 
 In addition to the LEGO SPIKE set, we considered other possible solutions, such as using Raspberry PI Zero W, using artificial intelligence and a camera to turn and avoid obstacles in the Obstacle Challenge round, and others, but we lacked the skills to implement our ideas. As a result, the prototypes we assembled were worse than the original robot, assembled from parts of the LEGO EV3 set. After that, we decided to try out the parts from the LEGO SPIKE set. The following is a description of the solution that we have prepared for the Regional stage of the World Robotics Olympiad.
 
 ## Our solution   
 
 The robot was assembled from the parts of the LEGO Spke kit, on one block, the hub from this edition. The following motors and sensors were used: large motor, medium motor, ultrasonic light sensor, 3 distance sensor. The wires were connected in series, prioritizing each part accordingly. The program for the robot was written using the block code of the SPIKE App program. The rotary system was implemented using sensors that measured the distance to the inner and outer walls, with sufficient proximity to the outer wall and the absence of the inner wall in the sensor's field of view, a turn is performed.
 
 To identify special signals of various colors (red and green), distance and color sensors are located on the front of our robot. When approaching the signs, the color sensor works optimally, and by determining the color of the sign through a conditional operator, it gives a signal to turn and drive the robot.

 The rotary system was implemented using a large motor from the LEGO Spike set, our robot is rear-wheel drive, the rear-mounted middle motor starts the movement of the robot's rear wheels, we decided that this type of robot drive would be the most optimal.


 Документация Инженера
====

 Данный репозиторий содержит материалы команды FORZA FERRARI, участвующщей в секции Future Engineers, создания самоуправляемой машины, сезона 2026 WRO.

 ## Контент

* `t-photos`содержит 2 фото комадны (одно из которых официальное, а другое неофициально, оба фото включают всех участников команды)
* `v-photos` содержит 6 фоток робота (с каждой стороны робота, сверху и снизу), а также дополнительно привидены подробный инструкции по сборке основных компонентов нашего робота
* `video` содержит файл video.md с ссылкой на видео с ездой робота
* `schemes` содержит фото со всеми электрическими компонентами, который были использованы и как они используются в нашем роботе и связаны между собой
* `src` содержит код, программу для всех компонентов робота с пояснениями в коде
* `other` описание того как были соединены компоненты между собой и как производится взаимодействие

 ## Наша мотивация:

 Мы два друга и оба фанаты формулы 1, в частности команды Феррари, (что довольно понятно из нашего названия). И недавно в мотоспорте произошло великое событие, первая гонка среди болидов формулы-1, под управлением искусственного интеллекта (Abu Dhabi Autonomous Racing League (A2RL)). Что не менее важно, данная гонка проходила на трассе в Абу-Даби, ОАЭ, одной из самых сложных и требующих невероятной техники вождения трасс. 
 
 После увиденного нами, нам стало интересно, а возможно ли нам самим сконструировать транспорт, который также полностью автономно. В категории Future Engineers, WRO, мы сможем полностью протестировать наши идеи, в условиях меньшого доступа к ресурсам, нежели в гонках A2RL.
 
 Как итог, вы сможете увидеть результаты наших трудов в данном репозитории Github.
	

 
 ## Введение

 Первая версия нашего робота для участия на региональных отборчных была создана из деталей набора LEGO EV3, однако столкнувшись с большими проблемами и критическими ошибками нами было принято решение полностью пересмотреть наше решение. Позже мы обнаружили наборы LEGO SPIKE, которые в отличии от набора LEGO EV3 продолжал поддерживаться компанией LEGO, а также детали данного набора были более высокого качества по сравнению с деталями набора LEGO EV3. 
 
 Помимо набора LEGO SPIKE мы рассматривали и другие возможные решения, такие как использование Raspberry PI Zero W, использование искусственного интеллекта и камеры для организации поворота и объезда препятствий на раунде Obstacle Challenge и другие, однако для реализации наших идей нам не хватало умений. Вследствии чего, собранные нами прототипы были хуже, чем изначальный робот, собранный из деталей набора LEGO EV3. После чего мы приняли решение попробовать детали из набора LEGO SPIKE. Далее последует описание решения, которое было подготовлено нами на региональный этап World Robotics Olympiad.   
 
 ## Наше решение

 Робот был собран из деталей комплекта LEGO Spke, на одном блоке, хабе из данного издания. Были использованы следующие моторы и датчики: большой мотор, средний мотор, ультразвуковой датчик света, датчик расстояния в количестве 3 штук. Провода были подключены последовательно, отдавая приоритет каждой детали соответственно. Программа для робота была написана используя блок-код, программы SPIKE App. Поворотная система была реализована при помощи датчиков, датчиков цвета которые измеряли расстояние до внутренних и внешних стен, при достаточном приближении к внешней стене и отсутствия внутренней стены в поле видимости датчика совершается поворот.
 
 Для опознования специальных сигналов различных цветов (красного и зеленого) на передней части нашего робота расположены датчики расстояния и цвета, при необходимом приближении к знакам датчик цвета работает оптимально, а также определяя цвет знака через условный оператор подает сигнал к повороту и езде робота.  
 
 Поворотная система была реализована при помощи использования большого мотора из набора LEGO Spike, наш робот заднеприводный, расположенный сзади средний мотор начинает движение задних колес робота, мы решили что данный тип привода робота будет наиболее оптимальным.

 
