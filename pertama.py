import shapefile


class Pertama:

    def __init__(self):
        self.pertama = shapefile.Writer('pertama', shapeType=shapefile.POLYGON)
        self.pertama.shapeType
        self.pertama.field('nama_ruangan', 'C')
    # Jangan keatas

    def baak(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-4, 0], [2, 0], [2, 8], [-4, 8], [-4, 0]]])

    def bauk(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[2, 0], [13, 0], [13, 8], [2, 8], [2, 0]]])
    # Buat fungsinya dibawah ini
    def gudangL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16,14], [-16, 16], [-9, 16], [-9, 14], [-16,14]]])

    def tanggaL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, 12], [-16, 14], [-9, 14], [-9, 12], [-16, 12]]])
     # Buat fungsinya dibawah ini

    def ruang117(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, 8], [-16, 12], [-9, 12], [-9, 8], [-16, 8]]])

    def ruang116(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, 4], [-16, 8], [-9, 8], [-9, 4], [-16, 4]]])

    def ruang115(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, 0], [-16, 4], [-9, 4], [-9, 0], [-16, 0]]])




    


     # Buat yang dari 101 ke bawah aja ya :*
    def gudangR(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18,14], [18, 16], [25, 16], [25, 14], [18,14]]])

    def tanggaR(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, 12], [18, 14], [25, 14], [25, 12], [18, 12]]])
    def ruang101(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, 8], [18, 12], [25, 12], [25, 8], [18, 8]]])
    
    def ruang104(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -4], [18, 0], [25, 0], [25, -4], [18, -4]]])

    # Jangan kebawah
    def close(self):
        self.pertama.close()
