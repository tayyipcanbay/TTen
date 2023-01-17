import requests

# get the image from images folder
image = open("images/question.png", "rb")

# send the image to the server
r = requests.post(
    "http://localhost:3131/upload",
    files={
        "file": image,
    },
    #send token
    headers={
        "token": "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"
    }
)
print(r.text)
