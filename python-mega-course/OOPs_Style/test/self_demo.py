class A:
    def __init__(i,temp):
        i.value=temp
        print("class instantiate")
    def view(i):
        print("i am viewing from view method:"+str(i.value))

a=A(100)
a.view()
