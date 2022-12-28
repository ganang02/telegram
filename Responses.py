from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Hallo", "hai", "hallo", "Hai", "Hi"):
        return "Haii! Ada Yang Bisa Dibantu?"

    if user_message in ("Game", "game"):
        return "Kamu membutuhkan saran game? silahkan ketik pc/mobile"

    if user_message in ("pc"):
        return "1. Valorant, 2. Gta V Online, 3. Point Blank"

    if user_message in ("mm"):
        return "mm"

    if user_message in ("status"):
        return "BOT INI DIBUAT DARI PYTHON"

    if user_message in ("siapa namamu?"):
        return "Haii! Namaku Adalah BOTIsng"

    if user_message in ("jam"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Saya tidak mengerti apa yang kamu katakan."   