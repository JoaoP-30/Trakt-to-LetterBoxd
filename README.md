# Trakt to Letterboxd Exporter 🎬

A simple and fast tool to export your watched movies history and ratings from [Trakt](https://trakt.tv/) to [Letterboxd](https://letterboxd.com/).

*(Leia em [Português](README.pt-br.md))*

---

## 🚀 How to Use (Step-by-Step)

Follow the steps below to generate your import file:

### 1. Download your data from Trakt
1. Go to [Trakt](https://trakt.tv/) and log in to your account.
2. Navigate to your account settings and request/download your personal data export.
3. Extract the downloaded `.zip` file on your computer.

### 2. Prepare the files
1. Locate the extracted files named **`watched-movies.json`** and **`ratings-movies.json`**.
2. Copy and paste both files into the **`in/`** folder of this project.

### 3. Run the script
Open your terminal (or command prompt) inside the project folder and run:

```bash
python main.py
```

### 4. Import into Letterboxd
1. The script will generate a ready-to-use file at **`out/movies.csv`**.
2. Log in to your **Letterboxd** account and go to **Settings > Import & Export**.
3. Under the import section, select the generated `movies.csv` file and confirm.

---

## 📋 Requirements
* **Python 3** installed on your computer (no external libraries required).

---

## ⚠️ Current Limitations
* Exports **movies only** (TV shows are not supported).
* Exports watch dates and ratings, **excluding reviews/comments**.

---

## 🤝 Contributing
Found a bug or have a suggestion? Feel free to open an *Issue* or submit a *Pull Request*.

## 📄 License
This project is licensed under the [MIT License](LICENSE).