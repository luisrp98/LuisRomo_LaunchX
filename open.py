def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print("No existe ese archivo")

if __name__ == '__main__':
    main()