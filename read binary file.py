with open("DSC_0041.jpg", "rb") as fp:
    ft = open("picture.jpg", "wb")
    for i in fp:
        ft.write(i)
ft.close()
