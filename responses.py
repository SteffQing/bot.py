
def responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("contract?", "address?"):
        return "Hello, our Contract address hasn't been created yet. Stay tuned"
    if user_message in ("website link?", "website"):
        return  "amestarter.com"
    if user_message in ("socials?", "twitter?"):
        return "Twitter -> twitter.com/amestarter"
    if user_message in "medium?":
        return "Medium -> medium.com/amestarter"
    return "I don't understand you"