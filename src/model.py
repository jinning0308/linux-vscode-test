class SimpleModel:
    def __init__(self):
        self.name = "Simple AI Model"

    def forward(self, x):
        return x * 2


if __name__ == "__main__":
    model = SimpleModel()

    result = model.forward(5)

    print("Model:", model.name)
    print("Input:", 5)
    print("Output:", result)
