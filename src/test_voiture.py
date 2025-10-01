from voiture import Voiture

class TestVoiture:

    def test_accelere_incremente_vitesse(self):
        # GIVEN
        v = Voiture("4L", "verte")
        
        # WHEN
        v.accelere(5)
        
        # THEN
        assert v.vitesse == 5

    def test_accelere_limite_increment(self):
        # GIVEN
        v = Voiture("4L", "verte")
        
        # WHEN
        v.accelere(20)
        
        # THEN
        assert v.vitesse == 10
