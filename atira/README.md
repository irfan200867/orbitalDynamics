# Simulasi evolusi orbit asteroid Atira

## Tinjauan Newtonian

Simulasi evolusi orbit asteroid Atira, khususnya **2020 AV2** dan **2021 PH27**. Data $a$, $e$, $i$, $\Omega$ , dan $\omega$ diunduh *real time* saat *running*, 
sedangkan $\sigma_a$, $\sigma_e$, $\sigma_i$, $\sigma_{\Omega}$, dan $\sigma_{\omega}$, berdasarkan fitur yang disediakan modul python [REBOUND](https://github.com/hannorein/rebound), dicatat dari [pangkalan data benda kecil di Horizons System, NASA JPL](https://ssd.jpl.nasa.gov/tools/sbdb_query.html). Ini berarti, nilai parameter $a$, sebagai contoh, dapat berada pada nilai $a - 1 \times \sigma_a$, $a + 0 \times \sigma_a$, dan $a + 1 \times \sigma_a$. Demikian juga 4 (empat) parameter orbit lainnya. Berdasarkan itu, maka 5 (lima) parameter orbit objek yang dikaji menghasilkan kemungkinan *cloning* sebanyak $3^5 = 243$.

### Daftar file
1. **asteroids.py**, file modul yang dipanggil oleh salah satu dari dua file di bawah ini
2. **combination.py**, untuk *running* dengan pantauan di layar, atau
3. **combination0.py**, untuk *running* tanpa pantauan di layar (luaran disimpan di file sehingga dapat ditinggal)

### Cara penggunaan

Contoh cara penggunaan di UNIX-like OS dengan menggunakan `python3`

```bash
python3 combination.py 19 1E6 1000
```

dengan tujuan *running* asteroid Atira nomor urut **19** (di `asteroids.py`), waktu integrasi `1E6` tahun dan *step* penampilan/penyimpanan hasil sebanyak `1000` titik. Cara lain yang identik (jika moda file `755` diberlakukan ke `combination.py` atau `combination0.py`:

```bash
./combination.py 19 1E6 1000
```

Khusus untuk penggunaan `combination0.py` (*submit job* agar dapat ditinggalkan *logout* dari workstation):

```bash
python3 combination0.py 19 1E6 1000 > /dev/null 2>&1 &
```

atau

```bash
./combination0.py 19 1E6 1000 > /dev/null 2>&1 &
```

(dan setelah ini aman dapat logout).


## Tinjauan Post-Newtonian

Dalam *progress* (menggunakan [REBOUNDX](https://github.com/dtamayo/reboundx))
