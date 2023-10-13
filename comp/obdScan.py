import obd
# from obd import OBDCommand, Unit
# from obd.protocols import ECU
from obd.utils import bytes_to_int


class LiveData: 

    # creating an asychronous runtime
    connection = obd.OBD()

    rpm_d = obd.commands.RPM
    fuel_lev = obd.commands.FUEL_LEVEL
    speed = obd.commands.SPEED
    fuel_rat = obd.commands.FUEL_RATE
    oil_temp = obd.commands.OIL_TEMP
    coolant_temp = obd.commands.COOLANT_TEMP
    intake_temp = obd.commands.INTAKE_TEMP
    throttle_position = obd.commands.THROTTLE_POS
    air_rate = obd.commands.MAF
    fuel_pres = obd.commands.FUEL_PRESSURE


    # def new_val(response):
    #     return response
    

    #keeping track of RPM
    def rpm_live(self):
        # LiveData.connection.watch(obd.commands.RPM,callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.rpm_d)
        return res.value


    def gen_DTC(self):
        codes = LiveData.connection.query(obd.commands.GET_DTC)
        return codes.value
    

    #percent
    def fuel_live(self):
        # LiveData.connection.watch(obd.commands.FUEL_LEVEL,callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.fuel_lev)
        return res.value
    #kmh


    def speed_live(self):
        # LiveData.connection.watch(obd.commands.SPEED,callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.speed)
        return res.value
    

    #L/h
    def fuel_rate_live(self):
        # LiveData.connection.watch(obd.commands.FUEL_RATE,callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.fuel_rat)
        return res.value


    #celsiui
    def oil_temp_live(self):
        # LiveData.connection.watch(obd.commands.OIL_TEMP,callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.oil_temp)
        return res.value
    


    #celsius
    def coolant_temp_live(self):
        # LiveData.connection.watch(obd.commands.COOLANT_TEMP, callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.coolant_temp)
        return res.value
    

    #celsius
    def intake_temp_live(self):
        # LiveData.connection.watch(obd.commands.INTAKE_TEMP, callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.intake_temp)
        return res.value

    
    # percent
    def throttle_pos_live(self):
        # LiveData.connection.watch(obd.commands.THROTTLE_POS, callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.throttle_pos_live)
        return res.value


    # grams/s
    def airflow_rate_live(self):
        # LiveData.connection.watch(obd.commands.MAF, callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.air_rate)
        return res.value
    

    #kilopascal
    def fuel_press_live(self):
        # LiveData.connection.watch(obd.commands.FUEL_PRESSURE, callback=LiveData.new_val)
        res = LiveData.connection.query(LiveData.fuel_pres)
        return res.value
    
    

    def clear_the_codes(self):
        LiveData.connection.query(obd.commands.CLEAR_DTC)
        
        codeList = LiveData.gen_DTC()

        if len(codeList) != 0:
            return "Code Clear Either Failed or They perstained"
        else:
            return "Codes Cleared Succesfully"
    


