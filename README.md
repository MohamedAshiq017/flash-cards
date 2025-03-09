#  Flash Card App - Learn Anything with Ease!

A **Tkinter-based Flash Card App** that helps you memorize words or concepts using spaced repetition. By default, it helps you learn **French-English translations**, but you can modify it for **any subject**—math formulas, historical facts, programming terms, or anything else!

##  Features
- Randomly selects a word for learning.
- Flips the card after **3 seconds** to show the answer.
- **Mark words as known** to remove them from the learning list.
- Saves progress in `words_to_learn.csv` so you don’t repeat known words.

##  Customize for Any Subject!
### Change the flashcard topic by modifying:
1. **`french_words.csv`** (or create your own CSV file in the same format)
   - This file contains **two columns**:  
     - **Column 1:** The word/concept you want to learn.  
     - **Column 2:** The corresponding answer/definition.

2. **Edit `main.py` to load your own dataset**  
   - Find this part in the code:
     ```python
     original_data = pandas.read_csv("./data/french_words.csv")
     ```
   - Replace `"french_words.csv"` with your own CSV file.

3. **Modify the labels on the flashcards**  
   - Find this part in `main.py`:
     ```python
     canvas.itemconfig(lang, text="French", fill="black")
     ```
   - Change `"French"` to your desired category (e.g., `"Math Formula"`).

##  Project Structure
```
 Flash Card App
│──  main.py          # Handles GUI, word selection, and interactions
│──  french_words.csv # Default dataset (French-English words)
│──  words_to_learn.csv (auto-generated) # Saves progress
│──  images           # Stores card images & button icons
```

##  How to Use
1. **Run** `main.py`.
2. The app will show a **word/question**.
3. Wait **3 seconds** for the card to flip or manually flip it.
4. Click  if you know it or  to keep it in rotation.
5. The app removes known words and tracks progress.

##  Requirements
- Python 3.x
- `pandas` module
- `tkinter` (built-in in Python)

## ▶️ Run the App
Clone the repository and run:

```bash
python main.py
```

##  Learn Smarter, Not Harder!
A simple **spaced repetition** flashcard app to improve your knowledge on **any topic**! Modify it to suit your learning needs.

---
 
