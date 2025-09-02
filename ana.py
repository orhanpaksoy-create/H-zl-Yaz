import sys
import os

# Proje yolunu ekle ki iç klasörleri import edebilelim
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sistem.pencereler.anapencere import ac_pencere

if __name__ == "__main__":
    ac_pencere()
