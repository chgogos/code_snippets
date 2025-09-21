import data_loader

if __name__ == "__main__":
    data = data_loader.load_data()
    mean = sum(data) / len(data)
    print(f"Mean: {mean}")
