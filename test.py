import program


zad11=program.zad1("kujawsko-pomorskie",2011,2014,3)
zad12=program.zad1("opolskie", 2013, 2017, 1)
zad13=program.zad1("mazowieckie", 2010, 2016, 3)
zad14=program.zad1("zachodniopomorskie", 2012, 2013, 2)
zad15=program.zad1("slaskie", 2015, 2018, 1)

zad21=program.zad2("pomorskie",1)
zad22=program.zad2("wielkopolskie",2)
zad23=program.zad2("lodzkie",3)
zad24=program.zad2("mazowieckie",2)
zad25=program.zad2("malopolskie",1)


zad31=program.zad3(2010, 1)
zad32=program.zad3(2015,2)
zad33=program.zad3(2018, 1)
zad34=program.zad3(2014,2)
zad35=program.zad3(2016, 3)



def test_zad1():
    assert zad11.srednia_k(75,81)==9500.0
    assert zad12.srednia_cal(294 ,303)==6559.6
    assert zad13.srednia_k(253 ,265)==24135.714285714286
    assert zad14.srednia_m(580 ,582)==5513.0
    assert zad15.srednia_cal(442 ,449)==28427.0


def test_zad2():
    assert zad21.tr1(396 ,414, 0)==81
    assert zad22.tr2(540, 558 ,1)==74
    assert zad23.tr3(180, 198 ,2)==80
    assert zad24.tr2(252, 270 ,0)==80
    assert zad25.tr1(216, 234 ,3)==83


def test_zad3():
    assert zad31.t1(0 ,15)==1
    assert zad32.t2(5, 15)==5
    assert zad33.t1(8, 15)==5
    assert zad34.t2(4, 15)==3
    assert zad35.t3(6, 15)==5