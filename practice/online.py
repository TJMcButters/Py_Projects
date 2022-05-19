def online_count(dict):
    online = 0
    for key, value in dict.items():
        if value == "online":
            online += 1
    return online


def main():
    users = {
        "Jake": "online",
        "Tony": "offline",
        "Johann": "online"
    }
    
    print(online_count(users))

if __name__ == "__main__":
    main()