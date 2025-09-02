from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout, QTextEdit, QDialog, QLineEdit, QMessageBox, QHBoxLayout, QListWidget
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
import os

def ac_pencere():
    # QApplication başlat
    app = QApplication([])

    # Ana pencereyi oluştur
    pencere = QMainWindow()
    pencere.setWindowTitle("HızlıYaz - Ana Pencere")
    
    # Boyut: 1100x800 piksel, sabit yap
    pencere.setFixedSize(1100, 800)
    pencere.setMaximumSize(1100, 800)
    pencere.setMinimumSize(1100, 800)

    # Merkezi widget oluştur
    merkezi_widget = QWidget()
    pencere.setCentralWidget(merkezi_widget)

    # Resmi yükle
    resim_yolu = os.path.join(os.path.dirname(__file__), "..", "veri", "resim", "hızlıyaz.png")
    resim = QPixmap(resim_yolu)
    
    # Resmi pencere boyutuna tam dolduracak şekilde ölçekle
    olceklendirilmis_resim = resim.scaled(1100, 800, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
    
    # QLabel ile resmi arka plan olarak göster
    resim_label = QLabel(merkezi_widget)
    resim_label.setPixmap(olceklendirilmis_resim)
    resim_label.setGeometry(0, 0, 1100, 800)

    # Düğmeler için layout ve widget oluştur
    dugme_widget = QWidget(merkezi_widget)
    dugme_widget.setGeometry(183, 222, 1100, 400)  # 5cm-0.01mm sağa (183 piksel), 6cm aşağı (222 piksel)
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # Yatayda ortaya hizala

    # Düğmeleri oluştur
    yeni_proje = QPushButton("Yeni Proje Aç")
    gecmis_proje = QPushButton("Geçmiş Projeyi Yükle")
    yardim = QPushButton("Yardım")
    cikis = QPushButton("Çıkış")

    # Kahve çekirdeği rengi ve kırmızı çıkış için stiller
    mat_stil = "QPushButton { background-color: %s; color: #ffffff; border: 1px solid #333333; border-radius: 8px; padding: 10px; font-size: 16px; min-width: 200px; min-height: 40px; } QPushButton:hover { background-color: %s; } QPushButton:pressed { background-color: %s; }"
    cikis_stil = "QPushButton { background-color: #f44336; color: white; border: none; border-radius: 8px; padding: 5px; font-size: 14px; min-width: 80px; min-height: 25px; } QPushButton:hover { background-color: #d32f2f; } QPushButton:pressed { background-color: #b71c1c; }"

    # Düğmelere stil uygula
    kahve_rengi = "#3F2A1D"  # Kahve çekirdeği
    kahve_hover = "#4F3726"
    kahve_pressed = "#2F1E14"
    yeni_proje.setStyleSheet(mat_stil % (kahve_rengi, kahve_hover, kahve_pressed))  # Kahve çekirdeği
    gecmis_proje.setStyleSheet(mat_stil % (kahve_rengi, kahve_hover, kahve_pressed))  # Kahve çekirdeği
    yardim.setStyleSheet(mat_stil % (kahve_rengi, kahve_hover, kahve_pressed))  # Kahve çekirdeği
    cikis.setStyleSheet(cikis_stil)  # Kırmızı

    # Düğmelere sabit boyut uygula
    for dugme in [yeni_proje, gecmis_proje, yardim, cikis]:
        dugme.setFixedSize(200, 40)

    # Yardım düğmesi için OKUBENİ.txt dosyasını açma işlevi
    def yardim_dosyasi_ac():
        dosya_yolu = os.path.join(os.path.dirname(__file__), "..", "veri", "metin", "yardım", "OKUBENİ.txt")
        try:
            with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
                icerik = dosya.read()
        except FileNotFoundError:
            icerik = "OKUBENİ.txt dosyası bulunamadı."
        except Exception as e:
            icerik = f"Dosya açılırken hata oluştu: {str(e)}"

        # Yeni bir pencerede içeriği göster
        yardim_penceresi = QDialog(pencere)
        yardim_penceresi.setWindowTitle("Yardım - OKUBENİ")
        yardim_penceresi.setFixedSize(700, 900)  # 700x900 sabit boyut
        yardim_penceresi.setStyleSheet("background-color: #FFF8E1;")  # Kâğıt sarısı arka plan
        
        # Metin alanı oluştur
        metin_alani = QTextEdit(yardim_penceresi)
        metin_alani.setGeometry(10, 10, 680, 880)  # Pencereye uygun boyut
        metin_alani.setReadOnly(True)
        metin_alani.setFont(QFont("Arial", 14))  # Font boyutu 14px
        metin_alani.setText(icerik)
        metin_alani.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Kaydırma çubuğu
        
        yardim_penceresi.exec()

    # Yeni Proje Aç düğmesi için pop-up ve kaydetme işlevi
    def yeni_proje_ac():
        # Pop-up penceresi oluştur
        proje_penceresi = QDialog(pencere)
        proje_penceresi.setWindowTitle("Yeni Proje Aç")
        proje_penceresi.setFixedSize(400, 400)  # 400x400 sabit boyut
        proje_penceresi.setStyleSheet("background-color: #FFF8E1;")  # Kâğıt sarısı arka plan

        # Layout oluştur
        proje_layout = QVBoxLayout()
        proje_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        proje_layout.setSpacing(20)

        # Proje Adı etiketi
        proje_adi_label = QLabel("Proje Adı")
        proje_adi_label.setFont(QFont("Arial", 16))
        proje_layout.addWidget(proje_adi_label)

        # Proje adı giriş çubuğu
        proje_adi_girisi = QLineEdit()
        proje_adi_girisi.setPlaceholderText("Proje adını girin (ör: orhan 001)")
        proje_adi_girisi.setFixedSize(300, 40)
        proje_adi_girisi.setFont(QFont("Arial", 14))
        proje_layout.addWidget(proje_adi_girisi)

        # Kaydet düğmesi
        kaydet_dugmesi = QPushButton("Kaydet")
        kaydet_dugmesi.setFixedSize(200, 40)
        kaydet_dugmesi.setStyleSheet(cikis_stil)  # Kırmızı stil
        proje_layout.addWidget(kaydet_dugmesi)

        # Yazma penceresi açma işlevi
        def yazma_penceresi_ac(proje_adi):
            # Ana pencereyi gizle
            pencere.hide()
            
            # Yazma penceresi oluştur
            yazma_penceresi = QDialog()
            yazma_penceresi.setWindowTitle(f"Proje: {proje_adi}")
            yazma_penceresi.setFixedSize(800, 980)  # 800x980 piksel
            yazma_penceresi.setMaximumSize(800, 980)
            yazma_penceresi.setMinimumSize(800, 980)
            yazma_penceresi.setStyleSheet("background-color: #FFF8E1;")  # Kâğıt sarısı arka plan

            # Layout oluştur
            yazma_layout = QVBoxLayout()
            yazma_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            yazma_layout.setSpacing(10)
            yazma_layout.addStretch()  # Düğmeyi alta sabitle

            # Metin alanı oluştur
            metin_alani = QTextEdit()
            metin_alani.setFont(QFont("Arial", 14))  # 14px Arial
            metin_alani.setStyleSheet("background-color: white; border: 1px solid #333333;")
            metin_alani.setFixedSize(780, 870)  # 780-20 (kenarlık), 800-80 (düğme için)
            metin_alani.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            metin_alani.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            yazma_layout.addWidget(metin_alani)

            # Düğme layout’u
            dugme_layout = QHBoxLayout()
            dugme_layout.setSpacing(20)

            # Kaydet düğmesi
            yazma_kaydet = QPushButton("Kaydet")
            yazma_kaydet.setFixedSize(200, 40)
            yazma_kaydet.setStyleSheet(cikis_stil)  # Kırmızı stil
            dugme_layout.addWidget(yazma_kaydet)

            yazma_layout.addLayout(dugme_layout)

            # Kaydet işlevi (direkt ana pencereye dönme ile)
            def yazma_kaydet_fonk():
                proje_dosyasi = os.path.join(os.path.dirname(__file__), "..", "veri", "metin", "projeler", f"{proje_adi}.txt")
                try:
                    with open(proje_dosyasi, 'w', encoding='utf-8') as dosya:
                        dosya.write(metin_alani.toPlainText())
                    yazma_penceresi.close()
                    pencere.show()
                except Exception as e:
                    QMessageBox.critical(yazma_penceresi, "Hata", f"Kayıt sırasında hata oluştu: {str(e)}")

            # Düğmeye işlev bağla
            yazma_kaydet.clicked.connect(yazma_kaydet_fonk)

            # Layout’u uygula
            yazma_penceresi.setLayout(yazma_layout)
            yazma_penceresi.exec()

        # Kaydet düğmesi işlevi
        def kaydet_proje():
            proje_adi = proje_adi_girisi.text().strip()
            if not proje_adi:
                QMessageBox.warning(proje_penceresi, "Hata", "Proje adı boş olamaz!")
                return
            
            proje_dosyasi = os.path.join(os.path.dirname(__file__), "..", "veri", "metin", "projeler", f"{proje_adi}.txt")
            try:
                # Dosya zaten varsa hata göster
                if os.path.exists(proje_dosyasi):
                    QMessageBox.warning(proje_penceresi, "Hata", f"'{proje_adi}.txt' zaten var! Lütfen başka bir isim girin.")
                    return
                
                # Yeni dosyayı oluştur (boş)
                with open(proje_dosyasi, 'w', encoding='utf-8') as dosya:
                    dosya.write("")  # Boş dosya
                proje_penceresi.accept()  # Pop-up’ı kapat
                yazma_penceresi_ac(proje_adi)  # Yazma penceresini aç
            except Exception as e:
                QMessageBox.critical(proje_penceresi, "Hata", f"Dosya oluşturulurken hata oluştu: {str(e)}")

        # Kaydet düğmesine işlev bağla
        kaydet_dugmesi.clicked.connect(kaydet_proje)

        # Layout’u pencereye uygula
        proje_penceresi.setLayout(proje_layout)
        proje_penceresi.exec()

    # Geçmiş Projeyi Yükle düğmesi için işlevi
    def gecmis_proje_yukle():
        proje_klasoru = os.path.join(os.path.dirname(__file__), "..", "veri", "metin", "projeler")
        if not os.path.exists(proje_klasoru):
            QMessageBox.warning(pencere, "Hata", "Projeler klasörü bulunamadı!")
            return

        # Proje dosyalarını listele
        proje_dosyalar = [f for f in os.listdir(proje_klasoru) if f.endswith(('.txt', '.md', '.docx'))]
        if not proje_dosyalar:
            QMessageBox.warning(pencere, "Hata", "Hiç proje dosyası bulunamadı!")
            return

        # Proje seçme dialogu
        secim_penceresi = QDialog(pencere)
        secim_penceresi.setWindowTitle("Geçmiş Projeleri Yükle")
        secim_penceresi.setFixedSize(400, 400)  # 400x400 piksel
        secim_penceresi.setStyleSheet("background-color: #FFF8E1;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Liste widget'ı
        liste = QListWidget()
        liste.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Kaydırma çubuğu ekle
        liste.addItems(proje_dosyalar)
        layout.addWidget(liste)

        # Düğme layout’u
        dugme_layout = QHBoxLayout()
        dugme_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        dugme_layout.setSpacing(20)

        # Yükle düğmesi
        yukle_dugme = QPushButton("Yükle")
        yukle_dugme.setFixedSize(80, 25)  # Daha küçük boyut
        yukle_dugme.setStyleSheet(cikis_stil)  # Kırmızı stil
        dugme_layout.addWidget(yukle_dugme)

        # Sil düğmesi
        sil_dugme = QPushButton("Sil")
        sil_dugme.setFixedSize(80, 25)  # Aynı boyut
        sil_dugme.setStyleSheet(cikis_stil)  # Kırmızı stil
        dugme_layout.addWidget(sil_dugme)

        layout.addLayout(dugme_layout)

        def yukle_secimi():
            secili_dosya = liste.currentItem()
            if secili_dosya:
                proje_adi = secili_dosya.text().replace('.txt', '').replace('.md', '').replace('.docx', '')
                proje_dosyasi = os.path.join(proje_klasoru, secili_dosya.text())
                try:
                    with open(proje_dosyasi, 'r', encoding='utf-8') as dosya:
                        icerik = dosya.read()
                    # Ana pencereyi gizle
                    pencere.hide()
                    # Yazma penceresi aç
                    yazma_penceresi = QDialog()
                    yazma_penceresi.setWindowTitle(f"Proje: {proje_adi}")
                    yazma_penceresi.setFixedSize(800, 980)
                    yazma_penceresi.setMaximumSize(800, 980)
                    yazma_penceresi.setMinimumSize(800, 980)
                    yazma_penceresi.setStyleSheet("background-color: #FFF8E1;")

                    # Layout oluştur
                    yazma_layout = QVBoxLayout()
                    yazma_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    yazma_layout.setSpacing(10)
                    yazma_layout.addStretch()

                    # Metin alanı oluştur
                    metin_alani = QTextEdit()
                    metin_alani.setFont(QFont("Arial", 14))
                    metin_alani.setStyleSheet("background-color: white; border: 1px solid #333333;")
                    metin_alani.setFixedSize(780, 870)
                    metin_alani.setText(icerik)
                    metin_alani.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
                    metin_alani.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
                    yazma_layout.addWidget(metin_alani)

                    # Düğme layout’u
                    dugme_layout = QHBoxLayout()
                    dugme_layout.setSpacing(20)

                    # Kaydet düğmesi
                    yazma_kaydet = QPushButton("Kaydet")
                    yazma_kaydet.setFixedSize(200, 40)
                    yazma_kaydet.setStyleSheet(cikis_stil)
                    dugme_layout.addWidget(yazma_kaydet)

                    yazma_layout.addLayout(dugme_layout)

                    # Kaydet işlevi
                    def yazma_kaydet_fonk():
                        try:
                            with open(proje_dosyasi, 'w', encoding='utf-8') as dosya:
                                dosya.write(metin_alani.toPlainText())
                            yazma_penceresi.close()
                            pencere.show()
                        except Exception as e:
                            QMessageBox.critical(yazma_penceresi, "Hata", f"Kayıt sırasında hata oluştu: {str(e)}")

                    # Düğmeye işlev bağla
                    yazma_kaydet.clicked.connect(yazma_kaydet_fonk)

                    # Layout’u uygula
                    yazma_penceresi.setLayout(yazma_layout)
                    secim_penceresi.accept()
                    yazma_penceresi.exec()
                except Exception as e:
                    QMessageBox.critical(pencere, "Hata", f"Dosya yüklenirken hata oluştu: {str(e)}")
            else:
                QMessageBox.warning(secim_penceresi, "Uyarı", "Lütfen bir proje seçin!")

        def sil_secimi():
            secili_dosya = liste.currentItem()
            if secili_dosya:
                cevap = QMessageBox.question(secim_penceresi, "Onay", f"'{secili_dosya.text()}' dosyasını silmek istediğinize emin misiniz?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if cevap == QMessageBox.StandardButton.Yes:
                    proje_dosyasi = os.path.join(proje_klasoru, secili_dosya.text())
                    try:
                        os.remove(proje_dosyasi)
                        liste.takeItem(liste.currentRow())  # Listeyi güncelle
                        QMessageBox.information(secim_penceresi, "Başarılı", "Dosya silindi!")
                    except Exception as e:
                        QMessageBox.critical(secim_penceresi, "Hata", f"Dosya silinirken hata oluştu: {str(e)}")
            else:
                QMessageBox.warning(secim_penceresi, "Uyarı", "Lütfen bir proje seçin!")

        # Düğmelere işlev bağla
        yukle_dugme.clicked.connect(yukle_secimi)
        sil_dugme.clicked.connect(sil_secimi)

        # Layout’u uygula
        secim_penceresi.setLayout(layout)
        secim_penceresi.exec()

    # Çıkış, Yardım ve Yeni Proje Aç düğmelerine işlev ekle
    cikis.clicked.connect(pencere.close)
    yardim.clicked.connect(yardim_dosyasi_ac)
    yeni_proje.clicked.connect(yeni_proje_ac)
    gecmis_proje.clicked.connect(gecmis_proje_yukle)

    # Düğmeleri ve aralıkları layout’a ekle
    layout.addWidget(yeni_proje)
    layout.addSpacing(11)  # 3mm ≈ 11 piksel
    layout.addWidget(gecmis_proje)
    layout.addSpacing(11)  # 3mm ≈ 11 piksel
    layout.addWidget(yardim)
    layout.addSpacing(37)  # 10mm ≈ 37 piksel (Çıkış için)
    layout.addWidget(cikis),

    # Mottoyu layout içinde sabit konuma ekle
    motto_label = QLabel("Yazı yazmak için neden üye olayım?")
    motto_label.setStyleSheet("""
        color: #3F2A1D;
        font-family: 'Comic Sans MS', 'Dancing Script', cursive;
        font-size: 18px;
        font-style: italic;
    """)
    motto_label.setFixedHeight(35)
    motto_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Ortala
    layout.addWidget(motto_label, alignment=Qt.AlignmentFlag.AlignCenter)  # Layout’a ekle
  

    # Layout’u düğme widget’ına uygula
    dugme_widget.setLayout(layout)

    
    # Pencereyi göster
    pencere.show()
    
    # Uygulamayı çalıştır
    app.exec()

if __name__ == "__main__":
    ac_pencere()
