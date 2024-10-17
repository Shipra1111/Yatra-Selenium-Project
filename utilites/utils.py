class Utils:
    def assertlistitemtext(self , list , value):

        for stop in list:
            print("The text is" + stop.text)
            assert stop.text == value
            print("assert pass")
