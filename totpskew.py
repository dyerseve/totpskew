import pyotp
import time
import keyboard

def generate_totp(secret, time_step=30, skew=0):
    """
    Generate a TOTP code with a clock skew.
    
    :param secret: The shared secret key.
    :param time_step: The time step in seconds. Default is 30 seconds.
    :param skew: The clock skew in seconds. Default is 0 seconds.
    :return: The TOTP code.
    """
    current_time = int(time.time() + skew)
    totp = pyotp.TOTP(secret, interval=time_step)
    return totp.at(current_time)

def main():
    secret = 'type_secret'  # This should be a base32 encoded string
    time_step = 30  # 30 seconds is the default time step
    skew = 0  # Adjust for a 10-second clock skew
    print("Press 'a' to generate TOTP code.")
    print("Press '+' to add 60 seconds to the skew.")
    print("Press '-' to subtract 30 seconds from the skew.")
    print("Press 'q' to quit.")

    while True:
        if keyboard.is_pressed('a'):
            totp_code = generate_totp(secret, time_step, skew)
            print(f'TOTP code: {totp_code}')
            time.sleep(0.5)  # Debounce delay
        elif keyboard.is_pressed('+'):
            skew += 30
            print(f'Skew increased to {skew} seconds.')
            time.sleep(0.5)  # Debounce delay
        elif keyboard.is_pressed('-'):
            skew -= 30
            print(f'Skew decreased to {skew} seconds.')
            time.sleep(0.5)  # Debounce delay
        elif keyboard.is_pressed('q'):
            print("Quitting...")
            break
        time.sleep(0.1)  # Reduce CPU usage

if __name__ == "__main__":
    main()
