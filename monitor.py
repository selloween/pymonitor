import requests
import pymsteams
from config import sites, clients


def send_message(text):

    if clients['msteams'] is True:
        
        print("msteams active")

        from config import msteams_webhook

        msteams = pymsteams.connectorcard(msteams_webhook)

        if clients['msteams'] is True:

            msteams.text(text)
            msteams.send()
    
    if clients['telegram'] is True:

        print("telegram active")

        from config import tg_token, tg_chat_id

        message = 'https://api.telegram.org/bot' + tg_token + '/sendMessage?chat_id=' + tg_chat_id + '&parse_mode=Markdown&text=' + text

        response = requests.get(message)

        return response.json()


def check_site(site):

    try:
        response = requests.get(site, timeout=5)

        if response.status_code == 200:

            status = 200

        else:

            status = "***HTTP Status for " + site + ":*** " + "``` " + str(response.status_code) + "```"

    except requests.exceptions.HTTPError as e:

        status = "***HTTP Error for " + site + ":*** " + "``` " + str(e) + "```"

    except requests.exceptions.ConnectionError as e:

        status = "***Connection Error for " + site + ":*** " + "``` " + str(e) + "```"

    except requests.exceptions.Timeout as e:

        status = "***Timeout Error for " + site + ":*** " + "``` " + str(e) + "```"

    except requests.exceptions.RequestException as e:

        status = "***Unknown Error for " + site + ":*** " + "``` " + str(e) + "```"

    return status


def main():

    for site in sites:

        status = check_site(site)

        print(site, str(status))

        if status is not 200:

            send_message(str(status))


send_message("Test")
