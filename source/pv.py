"""PV simulator"""
import time


def main():
    try:
        while True:
            print('PV Simulator...')
            time.sleep(1)
    except KeyboardInterrupt:
        pass  # exit gracefully when interrupted with CTRL+C


if __name__ == '__main__':
    main()
