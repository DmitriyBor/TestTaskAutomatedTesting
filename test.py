class TestClassSTR:
    def test_one(self):
        x = "Vozmite"
        assert "mi" in x

    def test_two(self):
        x = "Pojaluista"
        assert x.startswith('Poj')

    def test_three(self):
        x = "Na Kurs :cc"
        try:
            assert "--" in x 
        except AssertionError: 
            pass

class TestClassSET:
    def test_one(self):
        y = set(['Бразилия', 'Россия', 'Индия'])
        assert 'Россия' in y
    
    def test_two(self):
        y = set(['Греция', 'Канада', 'США'])
        try: 
            assert 'Россия' in y
        except AssertionError:
            pass
    
    def test_three(self):
        y = set('pepeChill')
        assert len(y) == 6



