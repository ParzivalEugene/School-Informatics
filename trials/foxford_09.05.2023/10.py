find = "каждый, каждого, каждому, каждым, каждом, каждая, каждую, каждой, каждое, каждые, каждых, каждыми".split(
    ", "
)
with open("data/10.txt", encoding="utf-16") as file:
    data = file.read().split()
    print(len([i for i in data if i.lower() in find]))
