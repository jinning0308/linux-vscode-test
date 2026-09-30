class SimpleDataset:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]


if __name__ == "__main__":
    dataset = SimpleDataset()

    print("Dataset size:", len(dataset))
    print("First sample:", dataset[0])
