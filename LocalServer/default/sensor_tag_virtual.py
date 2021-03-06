import random
import datetime

################################################################
# Virtual sensor                                               #
# Allow to instanciate a virtual sensor and generate fake datas#
################################################################
class Sensor_tag_virtual:
    ### Sensor interface ##
    ## attributs:
    # name  -> String
    # age   -> String -> "yyyy-MM-dd HH:mm:S"
    # race  -> int -> 0 = dog, 1 = cat
    # uuid  -> unique identifier
    ## methods
    # get_json() -> return a json with all measures

    def __init__(self, name, uuid, radio,race,age):
        self.name = name
        self.age = age
        self.race = race
        self.uuid = uuid
        self.radio = radio
        self.init_sensor()

    # set base values when instanciated
    def init_sensor(self):
        self.pressure = round(random.uniform(500, 700), 6)
        self.pressure_t = round(random.uniform(500, 700), 6)
        self.humidity = round(random.uniform(0, 50), 6)
        self.humidity_t = round(random.uniform(0, 50), 6)
        self.objtemp = round(random.uniform(0, 100), 6)
        self.accel_x = round(random.uniform(0, 200), 6)
        self.accel_y = round(random.uniform(0, 200), 6)
        self.accel_z = round(random.uniform(0, 200), 6)
        self.gyro_x = round(random.uniform(0, 360), 6)
        self.gyro_y = round(random.uniform(0, 360), 6)
        self.gyro_z = round(random.uniform(0, 360), 6)
        self.mag_x = round(random.uniform(0, 200), 6)
        self.mag_y = round(random.uniform(0, 200), 6)
        self.mag_z = round(random.uniform(0, 200), 6)
        self.light = round(random.uniform(0, 700), 6)
        self.battery = round(random.uniform(0, 100), 6)
        self.key1 = 0
        self.key2 = 0
        self.reed = 0
        self.buzzer = 0
        self.led_1 = 0
        self.led_2 = 0

    def get_guid(self):
        return self.uuid

    def get_is_activated(self):
        return 'true'

    def new_value(self, divider):
        way = random.randint(0, 1)
        if way == 0:
            val = round(random.uniform(0, 5) / divider, 6)
        else:
            val = -round(random.uniform(0, 5) / divider, 6)
        return val

    # To keep fake data coherent
    def keep_in_bound(self, min, max, val):
        if val > max:
            return max
        if val < min:
            return min

        return val

    def incr_pressure(self):
        self.pressure +=  self.new_value(1)
        self.pressure = self.keep_in_bound(200, 1200,self.pressure)

    def incr_pressure_t(self):
        self.pressure_t +=  self.new_value(1)
        self.pressure_t = self.keep_in_bound(200, 1200,self.pressure_t)

    def incr_humidity(self):
        self.humidity += self.new_value(10)
        self.humidity = self.keep_in_bound(0, 100,self.humidity)

    def incr_humidity_t(self):
        self.humidity_t += self.new_value(10)
        self.humidity_t = self.keep_in_bound(0, 100,self.humidity_t)

    def incr_accel_x(self):
        self.accel_x += self.new_value(100)
        self.accel_x = self.keep_in_bound(0, 10,self.accel_x)

    def incr_accel_y(self):
        self.accel_y +=  self.new_value(100)
        self.accel_y = self.keep_in_bound(0, 10,self.accel_y)

    def incr_accel_z(self):
        self.accel_z +=  self.new_value(100)
        self.accel_z = self.keep_in_bound(0, 10,self.accel_z)

    def incr_gyro_x(self):
        self.gyro_x +=  self.new_value(1)
        self.gyro_x = self.keep_in_bound(0, 360,self.gyro_x)

    def incr_gyro_y(self):
        self.gyro_y +=  self.new_value(1)
        self.gyro_y = self.keep_in_bound(0, 360,self.gyro_y)

    def incr_gyro_z(self):
        self.gyro_z +=  self.new_value(1)
        self.gyro_z = self.keep_in_bound(0, 360,self.gyro_z)

    def incr_mag_x(self):
        self.mag_x +=  self.new_value(1)
        self.mag_x = self.keep_in_bound(0, 360,self.mag_x)

    def incr_mag_y(self):
        self.mag_y +=  self.new_value(1)
        self.mag_y = self.keep_in_bound(0, 360,self.mag_y)

    def incr_mag_z(self):
        self.mag_z +=  self.new_value(1)
        self.mag_z = self.keep_in_bound(0, 360,self.mag_z)

    def incr_light(self):
        self.light +=  self.new_value(1)
        self.light = self.keep_in_bound(0, 1200,self.light)

    # Increment all sensors measure randomly
    def incr_all(self):
        self.incr_pressure()
        self.incr_pressure_t()
        self.incr_humidity()
        self.incr_humidity_t()
        self.incr_accel_x()
        self.incr_accel_y()
        self.incr_accel_z()
        self.incr_gyro_x()
        self.incr_gyro_y()
        self.incr_gyro_z()
        self.incr_mag_x()
        self.incr_mag_y()
        self.incr_mag_z()
        self.incr_light()

    # Parse all sensor measures in a JSON
    def get_json(self):
        self.incr_all()
        today = datetime.date.today()

        return {
            'guid': self.uuid,
            'isActive': self.get_is_activated(),
            'pressure': self.pressure,
            'pressure_t': self.pressure_t,
            'humidity': self.humidity,
            'humidity_t': self.humidity_t,
            'objtemp': 718.29,
            'accelX': self.accel_x,
            'accelY': self.accel_y,
            'accelZ': self.accel_z,
            'gyroX': self.gyro_x,
            'gyroY': self.gyro_y,
            'gyroZ': self.gyro_z,
            'magX': self.mag_x,
            'magY': self.mag_y,
            'magZ': self.mag_z,
            'light': self.light,
            'battery': self.battery,
            'key1': self.key1,
            'key2': self.key2,
            'reed': self.reed,
            'buzzer': self.buzzer,
            'LED1': self.led_1,
            'LED2': self.led_2,
            'Radio': self.radio,
            'date': today.ctime()
        }
