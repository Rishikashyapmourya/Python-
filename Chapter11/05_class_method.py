class employee:
    a=1

    @classmethod
    def show(cls):
        print(f"class atrribute is {cls.a}")

e=employee()
e.a=33
e.show()