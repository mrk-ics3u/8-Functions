# Lab 8 - Conversion Functions

You will write three functions, then a short main program that uses them.

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. Write `miles_to_km(miles)`. It returns the distance in kilometres, using `miles * 1.61`. If `miles` is negative, it returns `None`.
3. Write `time_in_seconds(minutes, seconds)`. It returns the total time in seconds. If either parameter is negative, it returns `None`.
4. Write `letter_count(text, letter)`. It returns how many times `letter` appears in `text`. Assume `letter` is a single character. Do **not** use `.count()`; use a loop.
5. Give each function a short description in triple quotes, as in the lesson.
6. Below the functions, ask `Enter a distance in miles: ` (a whole number), then print `Kilometres: ____` with the result of `miles_to_km()`.
7. Ask `Enter minutes: ` and then `Enter seconds: ` (whole numbers), then print `Total seconds: ____` with the result of `time_in_seconds()`.
8. Ask `Enter some text: ` and then `Enter a letter to count: `, then print `Letter count: ____` with the result of `letter_count()`.

Spell the function names exactly as written. Do not use `input()` or `print()`
inside the functions. The functions receive values through their parameters and
`return` the answer.

If a function returns `None`, your program prints it as is, for example
`Kilometres: None`.

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Positive values
```

When a test fails it shows what was expected and what your program printed. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you write any code.
- Write comments as you go, inside the functions as well as in the main program.
- Tests check your output exactly. `kilometres: 16.1` is not the same as `Kilometres: 16.1`.
- `letter_count()` is case sensitive: `'S'` and `'s'` are different letters.

## Optional challenges

Finished early? Try the optional challenges in the `challenges` folder. Open `challenges/CHALLENGES.md` for instructions. They are not assessed and do not affect your lab result.
