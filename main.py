from dummy_json_plugin import DummyJsonPlugin


def main():
    base_url = 'https://dummyjson.com'
    credentials = get_user_credentials()

    plugin = DummyJsonPlugin("dummyjson", base_url, credentials)
    plugin.execute()


def get_user_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    credentials = {
        'username': username,
        'password': password
    }

    return credentials


if __name__ == '__main__':
    main()
