from datetime import date

class CarnavalDomain():

    def calcular(self, ano):
        if ano == 0 :
            raise ValueError

        x = 24
        y = 5
        a = ano % 19
        b = ano % 4
        c = ano % 7 
        d = ( 19 * a + x ) % 30
        e = ( 2 * b + 4 * c + 6 * d + y ) % 7
        if ( (d + e ) > 9 ):
            dia = d + e - 9
            mes = 4
            data_pascoa = date(ano, mes, dia )
            carnaval = date.fromordinal(data_pascoa.toordinal()-47 )
        else:
            dia = d + e + 22
            mes = 3
            data_pascoa = date(ano, mes, dia )
            carnaval = date.fromordinal(data_pascoa.toordinal()-47 )

        return carnaval
