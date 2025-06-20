from app.views.window import window


class main:
    def __init__(self):
        self.window = window()
        self.window.init()


if __name__ == "__main__":
    app = main()
