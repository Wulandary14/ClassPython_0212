class PersegiPanjang:
    def __init__(self, panjang, lebar):
        if panjang == 0 or lebar == 0 :
            raise ValueError("Nilai panjang dan lebar tidak boleh 0!")

        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"persegi panjang dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"

# main
persegi = PersegiPanjang(3, 2)