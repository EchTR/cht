import datetime
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%d") + " " + now.strftime("%B") + " " + now.strftime("%Y")
if __name__ == "__main__":
    print(get_time())
    input()