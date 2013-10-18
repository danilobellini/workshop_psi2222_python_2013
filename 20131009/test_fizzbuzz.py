# FizzBuzz
# py.test

def fb(n):
    out = ""
    if n % 3 == 0:
        out += "Fizz"
    if n % 5 == 0:
        out += "Buzz" 
    else:
        out = n

    return out

def test_fb_um():
    assert 1 == fb(1)

def test_fb_dois():
    assert 2 == fb(2)

def test_fb_tres():
    assert "Fizz" == fb(3)

def test_fb_quatro():
    assert 4 == fb(4)

def test_fb_cinco():
    assert "Buzz" == fb(5)

def test_fb_seis():
    assert "Fizz" == fb(6)

def test_fb_nove():
    assert "Fizz" == fb(9)

def test_fb_dez():
    assert "Buzz" == fb(10)

def test_fb_doze():
    assert "Fizz" == fb(12)

def test_fb_quinze():
    assert "FizzBuzz" == fb(15)

def test_fb_dezoito():
    assert "Fizz" == fb(18)

def test_fb_vinte():
    assert "Buzz" == fb(20)

def test_fb_vinte_e_um():
    assert "Fizz" == fb(21)

def test_fb_vinte_e_quatro():
    assert "Fizz" == fb(24)

def test_fb_vinte_e_cinco():
    assert "Buzz" == fb(25)

def test_fb_vinte_e_sete():
    assert "Fizz" == fb(27)

def test_fb_trinta():
    assert "FizzBuzz" == fb(30)
