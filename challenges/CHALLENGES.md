# Optional Challenges - Lab 8

**These challenges are optional.** Try them once Lab 8 passes every test. They are
not assessed, and they do not affect your lab result.

| File | Challenge |
|---|---|
| `password_function.py` | Password Check Function |
| `caesar_shift.py` | Caesar Shift (harder) |

## Password Check Function

Turn your Lab 4 password checker into a reusable function. Open
`password_function.py` and complete `password_check(password)`:

1. Use the `password` parameter instead of `input()`.
2. Check the same four rules as Lab 4, in the same order, with the same messages:
   - `Error: Password must be at least 8 characters long.`
   - `Error: Password must contain at least one lowercase letter.`
   - `Error: Password must contain at least one uppercase letter.`
   - `Error: Password must contain exactly one digit.`
3. **Return** (do not print) every error that applies, one per line, as a single
   string. Put `"\n"` between messages. No `"\n"` after the last one.
4. If there are no errors, return `Password is valid.`

Remember that a function ends as soon as it reaches a `return`. You need a way to
collect every message first, then return them all at once.

For example, `print(password_check("hi"))` shows:

```
Error: Password must be at least 8 characters long.
Error: Password must contain at least one uppercase letter.
Error: Password must contain exactly one digit.
```

Do not rename the `def` line. The tests call the function by its name.

## Caesar Shift (harder)

A Caesar cipher hides a message by moving every letter the same number of places
through the alphabet. With a shift of 3, `a` becomes `d` and `z` wraps around to
`c`. Open `caesar_shift.py` and complete both functions.

1. Write `shift_letter(letter, shift)`. It takes one character and returns it
   moved `shift` places through the alphabet.
   - `shift_letter("c", 4)` returns `"g"`
   - Wrap around past `z`: `shift_letter("x", 5)` returns `"c"`
   - Capitals stay capitals: `shift_letter("M", -3)` returns `"J"`
   - Anything that is not a letter (spaces, digits, punctuation) comes back unchanged.
2. Write `caesar_shift(message, shift)`. It returns the whole message shifted.
   It must call `shift_letter()` for each character, not repeat its code.
   - `caesar_shift("Meet at noon!", 3)` returns `"Phhw dw qrrq!"`
   - A negative shift decodes: `caesar_shift("Phhw dw qrrq!", -3)` returns `"Meet at noon!"`
   - A shift bigger than 26 still works: a shift of 30 is the same as a shift of 4.

Hints:

- Start with `alphabet = "abcdefghijklmnopqrstuvwxyz"`. `alphabet.index("c")`
  gives `2`, the position of `"c"`.
- `%` keeps a position inside the alphabet: `(23 + 5) % 26` is `2`.
- `.lower()` and `.upper()` change a letter's case, and `.isupper()` tells you
  whether it was a capital.
- Get `shift_letter()` passing first. It is tested on its own.

Do not rename either `def` line. The tests call the functions by name.

## Running your program

Open the challenge file and press the Run button in the top right corner of VS
Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B**, the same as for the lab. The Lab 8 results appear first.
Scroll down to the **OPTIONAL CHALLENGES** section for these.

`SKIP` means you have not started that challenge yet. It is not an error.

## Reminders

- These are optional. Finish Lab 8 first.
- Comment as you go.
- Returned text is matched exactly, including `Error: ` and the period.
