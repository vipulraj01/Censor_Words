with open ("Censor.txt") as f:
    content = f.read()

    content = content.replace("donkey","@#$%^&")

    with open ("Censor.txt","w") as f:
        f.write(content)