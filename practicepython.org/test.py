def test():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4

print(test())