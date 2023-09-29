import obd
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int


class LiveData: 

    # creating an asychronous runtime
    connection = obd.Async()

    def new_val(response):
        return response
    

    #keeping track of RPM
    def rpm_live():
        LiveData.connection.watch(obd.commands.RPM,callback=LiveData.new_val)


    def gen_DTC():
        codes = LiveData.connection.query(obd.commands.GET_DTC)
        return codes.value
    

    #percent
    def fuel_live():
        LiveData.connection.watch(obd.commands.FUEL_LEVEL,callback=LiveData.new_val)
    #kmh


    def speed_live():
        LiveData.connection.watch(obd.commands.SPEED,callback=LiveData.new_val)
    

    #L/h
    def fuel_rate_live():
        LiveData.connection.watch(obd.commands.FUEL_RATE,callback=LiveData.new_val)


    #celsiui
    def oil_temp_live():
        LiveData.connection.watch(obd.commands.OIL_TEMP,callback=LiveData.new_val)
    


    #celsius
    def coolant_temp_live():
        LiveData.connection.watch(obd.commands.COOLANT_TEMP, callback=LiveData.new_val)
    

    def intake_temp_live():
        LiveData.connection.watch(obd.commands.INTAKE_TEMP, callback=LiveData.new_val)

