import time
from datetime import datetime,timedelta
import pytz

# Obtener la zona horaria UTC
utc_tz = pytz.timezone('UTC')

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(f"{min_sec_format} \n")
        time.sleep(1)
        num_of_secs -= 1
        
    print('Countdown finished.')

inp = int(input('Input number of seconds to countdown: '))
countdown(inp)


def mi_funcion():
    session = {}

    session['code_created_at'] = datetime.now()

    # Convertir la fecha/hora a un objeto offset-aware en UTC
    session['code_created_at'] = session['code_created_at'].replace(tzinfo=pytz.UTC)


    print(datetime.now())
    print(session['code_created_at'])

    print("   ")
    print(datetime.now(pytz.utc))
    
    if 'code_created_at' in session and datetime.now(pytz.utc) > session['code_created_at'] + timedelta(minutes=5):
            # La variable de sesión ha expirado
            
            del session['code_created_at']
            

            print("El codigo de recuperacion expiro")

mi_funcion()
