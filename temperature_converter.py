def cToFConverter():
    while True:
        cTemp=input("Please enter C degree: ")
        if cTemp:
            cTemp=float(cTemp)
            fTemp = 9*cTemp/5 +32

            print(f"{cTemp}C is converter to {fTemp}F")
            break
        else:
            print("cTemp input is empty")
            continue


def main():
    # print("hello word")
    cToFConverter()

if __name__=="__main__":
    main()
