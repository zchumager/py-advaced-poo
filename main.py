def main():
    lang = "Python"
    string_format = "fstring"
    subject = "you"
    letter = "f"

    msg = (f"this is the way how {lang} "
           f"can handle multiple {string_format} lines, "
           f"so in this way {subject} can type as many lines "
           f"as {subject} need with a proper format"
           f"given by {string_format} just using the "
           f"{letter} preffix")
    print(msg)


if __name__ == "__main__":
    main()
