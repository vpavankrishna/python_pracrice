import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # Overwrites the same line
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Main function
def main():
    try:
        seconds = int(input("Enter the time in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()