# 📚 Flash Card Learning App

An interactive **flash card application** built with **Python**, **Tkinter** (for GUI), and **Pandas** (for CSV data handling)  
to help you learn and memorize words in **any language pair**.

It shows a word in one language, flips after 3 seconds to reveal the translation, and tracks your progress by saving the words you still need to practice.

---

## 🎥 Demo
![Flash Card Demo](demo.gif)

---

## ✨ Features

- **🖥 Built with Tkinter & Pandas**  
  Uses Tkinter for a clean, interactive GUI and Pandas for reading/writing CSV files.

- **📂 Auto Data Loading with Fallback**  
  Loads `words_to_learn.csv` if available (from your previous session)  
  Else, loads default `french_words.csv` (or your custom CSV).

- **🎲 Random Word Selection**  
  Shows a random word pair each time.

- **⏳ Auto Flip after 3 seconds**  
  First shows the question word → flips to show the answer.

- **✔ / ❌ Button Controls**  
  - **Right** button → Word removed from the learning list.  
  - **Wrong** button → Word saved for the next session.

- **💾 Persistent Learning**  
  Only the words you marked wrong will be saved in `words_to_learn.csv` for the next session.

- **📢 Session Complete Notification**  
  Once you finish all cards, a congratulatory popup appears.

- **🌍 Multi-Language Support**  
  Not just French → English!  
  You can add **any language pair** in a CSV format:
  ```csv
  French,English
  partie,part
  histoire,history
  chercher,search
  seulement,only
  ```
  Or:
  ```csv
  Spanish,English
  hola,hello
  adiós,goodbye
  gracias,thank you
  ```

---

## 📁 Project Structure

```
flash-card-project/
│
├── data/
│   ├── french_words.csv
│   ├── test.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_back.png
│   ├── card_front.png
│   ├── right.png
│   └── wrong.png
│
├── demo.gif
└── main.py
```

---

## 🛠 Requirements

- Python 3.x  
- `pandas` library  
- `tkinter` (comes pre-installed with Python)

Install pandas:
```bash
pip install pandas
```

---

## 🚀 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/flash-card-project.git
   cd flash-card-project
   ```

2. Place your CSV file inside the `data/` folder.  
   Ensure it has **two columns**:  
   - First column → Question language  
   - Second column → Answer language

3. Run the program:
   ```bash
   python main.py
   ```

---

## 📄 CSV Format Example

| French     | English  |
|------------|----------|
| partie     | part     |
| histoire   | history  |
| chercher   | search   |
| seulement  | only     |

---

## 👨‍💻 Author

**Saurabh Kulshrestha**