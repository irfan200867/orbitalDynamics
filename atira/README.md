# Simulasi evolusi orbit asteroid Atira

Simulasi evolusi orbit asteroid Atira, khususnya **2020 AV2** dan **2021 PH27**. Data $a$ , $e$ , $i$ , $\Omega$ , dan $\omega$ diunduh *real time* saat *running*, 
sedangkan $\sigma_a$ , $\sigma_e$ , $\sigma_i$ , $\sigma_{\Omega}$ , dan $\sigma_{\omega}$ , berdasarkan fitur yang disediakan modul python [REBOUND](https://github.com/hannorein/rebound), dicatat dari [pangkalan data benda kecil di Horizons System, NASA JPL](https://ssd.jpl.nasa.gov/tools/sbdb_query.html).

Daftar file:
1. **asteroids.py**, file modul yang dipanggil oleh salah satu dari dua file di bawah ini
2. **combination.py**, untuk *running* dengan pantauan di layar, atau
3. **combination0.py**, untuk *running* tanpa pantauan di layar (luaran disimpan di file sehingga dapat ditinggal)
