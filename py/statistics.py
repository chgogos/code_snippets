import data_loader


def mean(data):
    return sum(data) / len(data)


if __name__ == "__main__":
    data = data_loader.load_data()
    print(f"Mean: {mean(data)}")
