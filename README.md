# Bidirectional-Conditional-Insertion-Sort (BCIS) & Counting Sort

Compares two sorting algorithms' running time in millisecond and its memory usage for small (500), medium (500), and large (50000) sized data where each data has 3 variants, sorted, randomized, and reversed. Data elements ranges from 0 to 50000.

- `driver.py` : Executes both sorting algorithms, prints running time and memory usage for each datasets/sorting algorithm.
- `sorters.py` : BCIS and Counting Sort implementation.
- `datasets.py` : Generates datasets for comparison.
- `analysis_datasets` : Generated datasets used for comparison.
- `output.txt` : Comparison results.

### Run
1. `python -m venv env`
2. `env\Scripts\activate.bat`
3. `pip install -r requirements.txt`
4. `python driver.py`

### Referensi
Adnan Saher Mohammed, S¸ahin Emrah Amrahov, and Fatih V C¸ elebi. *Bidirectional Conditional Insertion Sort algorithm; An efficient progress on the classical insertion sort*. Future Generation Computer Systems, 71:102–112, 2017.

##### Rayhan Putra Randi <br> 2106705644 <br> DAA - A | Kode Asdos 1
