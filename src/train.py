from dataset import SimpleDataset
from model import SimpleModel


def train():
    dataset = SimpleDataset()
    model = SimpleModel()

    print("Start training...")
    print("Dataset size:", len(dataset))

    for epoch in range(1, 6):
        print(f"Epoch {epoch}/5")

        for i in range(len(dataset)):
            x = dataset[i]
            y = model.forward(x)

            print(f"  Input: {x} -> Output: {y}")

    print("Training finished!")


if __name__ == "__main__":
    train()
