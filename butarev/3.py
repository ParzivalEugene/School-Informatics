def main():
    path = "data/data.txt"  # path to the file
    with open(path, encoding="utf-8") as file:
        sub_data, *data = [
            int(i) if " " not in i else map(int, i.split()) for i in file.readlines()
        ]
        disk_size, _ = sub_data
        data = sorted(data, reverse=True)

        # find max users count
        users_in_disk_arr = []
        while sum(users_in_disk_arr) <= disk_size:
            users_in_disk_arr.append(data.pop())
        users_in_disk_arr.pop()

        # find max user size
        user_size = max(users_in_disk_arr) + disk_size - sum(users_in_disk_arr)
        while user_size not in data:
            user_size -= 1

        print(len(users_in_disk_arr), user_size)


if __name__ == "__main__":
    main()
