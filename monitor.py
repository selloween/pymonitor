import requests
import logging
from config import token, chat_id, sites

def sendtext(message):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' +message

    response = requests.get(send_text)
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
    
for site in sites:
    status = check_site(site)
    print(site, str(status))
    if status is not 200:
        sendtext(str(status))
