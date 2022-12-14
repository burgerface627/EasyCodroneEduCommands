from codrone_edu.drone import *
import time

drone = Drone()


class Easy:
    # noinspection PyMethodMayBeStatic
    def start(self):  # pairs the drone and makes it takeoff
        drone.pair()
        drone.takeoff()

    # noinspection PyMethodMayBeStatic
    def move(self, direction, power, duration):  # used to execute a move in one line of code
        """

        :param direction: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power: int from -100 to 100, 360 to -360 for turns
        :param duration: positive float
        :return:
        """
        if direction == "forward":
            drone.set_pitch(power)
        elif direction == "backward":
            drone.set_pitch(-power)
        elif direction == "left":
            drone.set_roll(-power)
        elif direction == "right":
            drone.set_roll(power)
        elif direction == "up":
            drone.set_throttle(power)
        elif direction == "down":
            drone.set_throttle(-power)
        if direction == "turn_left":
            drone.turn_degree(-power, duration)
        elif direction == "turn_right":
            drone.turn_degree(power, duration)
        drone.move(duration)

    # noinspection PyMethodMayBeStatic
    def combo_move_2(self, direction1, power1, direction2, power2, duration):  # allows two movements in one line
        """

        :param direction1: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power1: int 100 to -100
        :param direction2: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power2: int 100 to -100
        :param duration: positive float
        :return:
        """
        if direction1 == "forward":
            drone.set_pitch(power1)
        elif direction1 == "backward":
            drone.set_pitch(-power1)
        elif direction1 == "left":
            drone.set_roll(-power1)
        elif direction1 == "right":
            drone.set_roll(power1)
        elif direction1 == "up":
            drone.set_throttle(power1)
        elif direction1 == "down":
            drone.set_throttle(-power1)
        elif direction1 == "turn_left":
            drone.set_yaw(power1)
        elif direction1 == "turn_right":
            drone.set_yaw(-power1)

        if direction2 == "forward":
            drone.set_pitch(power2)
        elif direction1 == "backward":
            drone.set_pitch(-power2)
        elif direction2 == "left":
            drone.set_roll(-power2)
        elif direction2 == "right":
            drone.set_roll(power2)
        elif direction2 == "up":
            drone.set_throttle(power2)
        elif direction2 == "down":
            drone.set_throttle(-power2)
        elif direction2 == "turn_left":
            drone.set_yaw(power2)
        elif direction2 == "turn_right":
            drone.set_yaw(-power2)
        drone.move(duration)

    # noinspection PyMethodMayBeStatic
    def combo_move_3(self, direction1, power1, direction2, power2, direction3, power3, duration):
        """

        :param direction1: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power1: int 100 to -100
        :param direction2: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power2: int 100 to -100
        :param direction3: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power3: int 100 to -100
        :param duration: positive float
        :return:
        """
        # combine 3 movements into one line of code
        if direction1 == "forward":
            drone.set_pitch(power1)
        elif direction1 == "backward":
            drone.set_pitch(-power1)
        elif direction1 == "left":
            drone.set_roll(-power1)
        elif direction1 == "right":
            drone.set_roll(power1)
        elif direction1 == "up":
            drone.set_throttle(power1)
        elif direction1 == "down":
            drone.set_throttle(-power1)
        elif direction1 == "turn_left":
            drone.set_yaw(power1)
        elif direction1 == "turn_right":
            drone.set_yaw(-power1)

        if direction2 == "forward":
            drone.set_pitch(power2)
        elif direction1 == "backward":
            drone.set_pitch(-power2)
        elif direction2 == "left":
            drone.set_roll(-power2)
        elif direction2 == "right":
            drone.set_roll(power2)
        elif direction2 == "up":
            drone.set_throttle(power2)
        elif direction2 == "down":
            drone.set_throttle(-power2)
        elif direction2 == "turn_left":
            drone.set_yaw(power2)
        elif direction2 == "turn_right":
            drone.set_yaw(-power2)

        if direction3 == "forward":
            drone.set_pitch(power3)
        elif direction3 == "backward":
            drone.set_pitch(-power3)
        elif direction3 == "left":
            drone.set_roll(-power3)
        elif direction3 == "right":
            drone.set_roll(power3)
        elif direction3 == "up":
            drone.set_throttle(power3)
        elif direction3 == "down":
            drone.set_throttle(-power3)
        elif direction3 == "turn_left":
            drone.set_yaw(power3)
        elif direction3 == "turn_right":
            drone.set_yaw(-power3)
        drone.move(duration)

    # noinspection PyMethodMayBeStatic
    def combo_move_4(self, direction1, power1, direction2, power2, direction3, power3, direction4, power4, duration):
        """

        :param direction1: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power1: int 100 to -100
        :param direction2: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power2: int 100 to -100
        :param direction3: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power3: int 100 to -100
        :param direction4: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power4: int 100 to -100
        :param duration: positive float
        :return:
        """
        # combine 4 movements into one line of code
        if direction1 == "forward":
            drone.set_pitch(power1)
        elif direction1 == "backward":
            drone.set_pitch(-power1)
        elif direction1 == "left":
            drone.set_roll(-power1)
        elif direction1 == "right":
            drone.set_roll(power1)
        elif direction1 == "up":
            drone.set_throttle(power1)
        elif direction1 == "down":
            drone.set_throttle(-power1)
        elif direction1 == "turn_left":
            drone.set_yaw(power1)
        elif direction1 == "turn_right":
            drone.set_yaw(-power1)

        if direction2 == "forward":
            drone.set_pitch(power2)
        elif direction1 == "backward":
            drone.set_pitch(-power2)
        elif direction2 == "left":
            drone.set_roll(-power2)
        elif direction2 == "right":
            drone.set_roll(power2)
        elif direction2 == "up":
            drone.set_throttle(power2)
        elif direction2 == "down":
            drone.set_throttle(-power2)
        elif direction2 == "turn_left":
            drone.set_yaw(power2)
        elif direction2 == "turn_right":
            drone.set_yaw(-power2)

        if direction3 == "forward":
            drone.set_pitch(power3)
        elif direction3 == "backward":
            drone.set_pitch(-power3)
        elif direction3 == "left":
            drone.set_roll(-power3)
        elif direction3 == "right":
            drone.set_roll(power3)
        elif direction3 == "up":
            drone.set_throttle(power3)
        elif direction3 == "down":
            drone.set_throttle(-power3)
        elif direction3 == "turn_left":
            drone.set_yaw(power3)
        elif direction3 == "turn_right":
            drone.set_yaw(-power3)

        if direction4 == "forward":
            drone.set_pitch(power4)
        elif direction4 == "backward":
            drone.set_pitch(-power4)
        elif direction4 == "left":
            drone.set_roll(-power4)
        elif direction4 == "right":
            drone.set_roll(power4)
        elif direction4 == "up":
            drone.set_throttle(power4)
        elif direction4 == "down":
            drone.set_throttle(-power4)
        elif direction4 == "turn_left":
            drone.set_yaw(power4)
        elif direction4 == "turn_right":
            drone.set_yaw(-power4)
        drone.move(duration)

    # noinspection PyMethodMayBeStatic
    def set_lights(self, r, g, b, brightness):
        drone.set_drone_LED(r, g, b, brightness)
        drone.set_controller_LED(r, g, b, brightness)
        time.sleep(0.05)

    # noinspection PyMethodMayBeStatic
    def turn(self, direction, degrees, duration):
        """

        :param direction: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param degrees: int 360 to -360
        :param duration: positive float
        :return:
        """
        # turn at en exact angle
        if direction == "right":
            drone.turn_degree(-degrees, duration)
        elif direction == "left":
            drone.turn_degree(degrees, duration)

    # noinspection PyMethodMayBeStatic
    def accurate_move(self, direction, distance, power):
        """

        :param direction: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param distance: int in inches, how long you want to turn for if turning
        :param power: int 100 to -100, 360 to -360 if turning
        :return:
        """
        # move for an exact distance
        if direction == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power)
            true_distance = distance_calc + distance
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power)
            true_distance = distance_calc - distance
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power)
            true_distance = distance_calc - distance
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power)
            true_distance = distance_calc + distance
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power)
            true_distance = distance_calc + distance
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power)
            true_distance = distance_calc - distance
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction == "turn_right":
            drone.turn_degree(-power, distance)
        elif direction == "turn_left":
            drone.turn_degree(power, distance)

    # noinspection PyMethodMayBeStatic
    def accurate_combo_move_2(self, direction1, distance1, power1, direction2, distance2, power2, duration):
        """

        :param duration: positive float
        :param power2: int 100 to -100
        :param power1: int 100 to -100
        :param direction1: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param distance1: distance in inches
        :param direction2: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param distance2: distance in inches
        :return:
        """
        if direction1 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction1 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction1 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction1 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction1 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction1 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction1 == "turn_right":
            drone.turn_degree(-power1, duration)
        elif direction1 == "turn_left":
            drone.turn_degree(power1, duration)

        if direction2 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction2 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction2 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction2 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction2 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction2 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction2 == "turn_right":
            drone.turn_degree(-power2, duration)
        elif direction2 == "turn_left":
            drone.turn_degree(power2, duration)

    # noinspection PyMethodMayBeStatic
    def accurate_combo_move_3(self, direction1, distance1, power1, direction2, distance2, power2, direction3, distance3,
                              power3,
                              duration):
        """

        :param distance3: distance in inches
        :param distance2: distance in inches
        :param distance1: distance in inches
        :param direction1: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power1: int 100 to -100
        :param direction2: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power2: int 100 to -100
        :param direction3: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power3: int 100 to -100
        :param duration: positive float
        :return:
        """
        # combine 3 movements into one line of code
        if direction1 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction1 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction1 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction1 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction1 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction1 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction1 == "turn_right":
            drone.turn_degree(-power1, duration)
        elif direction1 == "turn_left":
            drone.turn_degree(power1, duration)

        if direction2 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction2 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction2 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction2 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction2 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction2 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction2 == "turn_right":
            drone.turn_degree(-power2, duration)
        elif direction2 == "turn_left":
            drone.turn_degree(power2, duration)

        if direction3 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power3)
            true_distance = distance_calc + distance3
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction3 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power3)
            true_distance = distance_calc - distance3
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction3 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power3)
            true_distance = distance_calc - distance3
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction3 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power3)
            true_distance = distance_calc + distance3
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction3 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power3)
            true_distance = distance_calc + distance3
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction3 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power3)
            true_distance = distance_calc - distance3
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction3 == "turn_right":
            drone.turn_degree(-power3, duration)
        elif direction3 == "turn_left":
            drone.turn_degree(power3, duration)

    # noinspection PyMethodMayBeStatic
    def accurate_combo_move_4(self, direction1, distance1, power1, direction2, distance2, power2, direction3, distance3,
                              power3,
                              direction4, distance4, power4, duration):
        """

        :param distance4: distance in inches
        :param distance3: distance in inches
        :param distance2: distance in inches
        :param distance1: distance in inches
        :param direction1: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power1: int 100 to -100
        :param direction2: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power2: int 100 to -100
        :param direction3: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power3: int 100 to -100
        :param direction4: str(forward, backward, left, right, up, down, turn_left, turn_right)
        :param power4: int 100 to -100
        :param duration: positive float
        :return:
        """
        # combine 4 movements into one line of code
        if direction1 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction1 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction1 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction1 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction1 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power1)
            true_distance = distance_calc + distance1
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction1 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power1)
            true_distance = distance_calc - distance1
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction1 == "turn_right":
            drone.turn_degree(-power1, duration)
        elif direction1 == "turn_left":
            drone.turn_degree(power1, duration)

        if direction2 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction2 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction2 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction2 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction2 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power2)
            true_distance = distance_calc + distance2
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction2 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power2)
            true_distance = distance_calc - distance2
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction2 == "turn_right":
            drone.turn_degree(-power2, duration)
        elif direction2 == "turn_left":
            drone.turn_degree(power2, duration)

        if direction3 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power3)
            true_distance = distance_calc + distance3
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction3 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power3)
            true_distance = distance_calc - distance3
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction3 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power3)
            true_distance = distance_calc - distance3
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction3 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power3)
            true_distance = distance_calc + distance3
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction3 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power3)
            true_distance = distance_calc + distance3
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction3 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power3)
            true_distance = distance_calc - distance3
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction3 == "turn_right":
            drone.turn_degree(-power3, duration)
        elif direction3 == "turn_left":
            drone.turn_degree(power3, duration)

        if direction4 == "forward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(power4)
            true_distance = distance_calc + distance4
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction4 == "backward":
            distance_calc = drone.get_pos_z(unit="in")
            drone.set_pitch(-power4)
            true_distance = distance_calc - distance4
            while true_distance < distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_z(unit="in")
        elif direction4 == "left":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(-power4)
            true_distance = distance_calc - distance4
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_x(unit="in")
        elif direction4 == "right":
            distance_calc = drone.get_pos_x(unit="in")
            drone.set_roll(power4)
            true_distance = distance_calc + distance4
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_x(unit="in")
        elif direction4 == "up":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(power4)
            true_distance = distance_calc + distance4
            while true_distance > distance_calc:
                drone.move(0.05)
                distance_calc = drone.get_pos_y(unit="in")
        elif direction4 == "down":
            distance_calc = drone.get_pos_y(unit="in")
            drone.set_throttle(-power4)
            true_distance = distance_calc - distance4
            while true_distance < distance_calc:
                drone.move(0.05)
                drone.get_pos_y(unit="in")
        elif direction4 == "turn_right":
            drone.turn_degree(-power4, duration)
        elif direction4 == "turn_left":
            drone.turn_degree(power4, duration)
