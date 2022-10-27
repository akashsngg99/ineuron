ip=input("Enter Month     ")

match ip:
    case 'Jan':
        print("31 days")
    case "Feb":
        print("28 days")
    case 'Mar':
        print("31 days")
    case 'Apr':
        print("30 days")
    case 'May':
        print("31 days")
    case 'Jun':
        print("30 days")
    case 'Jul':
        print("31 days")
    case 'Aug':
        print("31 days")
    case 'Sep':
        print("30 days")
    case 'Oct':
        print("31 days")
    case 'Nov':
        print("30 days")
    case 'Dec':
        print("31 days")
    case other:
        print("Enter wrong input")
