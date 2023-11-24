from datetime import datetime, timedelta
import pytz
import time


# Establecer la zona horaria local
local_tz = pytz.timezone('America/Caracas')

session = {}
session['code_created_at'] = datetime.now(local_tz)

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(f"{min_sec_format} \n")
        time.sleep(1)
        num_of_secs -= 1
        
    print('Countdown finished.')


countdown(400)




# Comparar el tiempo transcurrido desde la creación del código
if 'code_created_at' in session and datetime.now(local_tz) > session['code_created_at'] + timedelta(minutes=5):
    # La variable de sesión ha expirado
    del session['code_created_at']
    print("El código de recuperación expiró")
