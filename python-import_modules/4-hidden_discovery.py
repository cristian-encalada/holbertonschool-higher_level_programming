#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import dis
    list = dis.dis(hidden_4)
    for str in list:
        if str[:2] != "__":
            print("{}".format(str))
