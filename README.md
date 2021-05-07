# Telegram and MS Teams Site Monitor Bot

A simple Python script that checks availabilty of multiple sites and sends error alerts to Telegram and/or Microsoft Teams.

## Basic configuration
Copy `config_sample.py` to `config.py` and edit accordingly.

### Add sites and web services to be monitored
```python
# config.py
sites = [
  "www.google.com",
  "www.twitter.com"
]
```

### Activate messengers
```python
# config.py
clients = {
  "msteams" = False,
  "telegram" = True
}
```

## Telegram

### Create new Telegram Bot
* Create a new Telegram Bot: https://core.telegram.org/bots#6-botfather
* Create a new Telegram group in the Telegram App and add the newly created bot
* Optionally: Grant your bot group admin permissions

### Get ChatID
* Open in Browser (Replace {TOKEN} in URL with your Token): https://api.telegram.org/bot{TOKEN}/getUpdates
* Copy Chat ID

**Example JSON Responce:**
```json
chat: {
  id: "XXXXXXXXX",
  title: "my_group_name",
  type: "group",
}
```

* Set Telegram client to `True` in `config.py`
* Add Telegram Bot Token and Chat ID

```python
# Telegram
tg_token = ""
tg_chat_id = ""
```

## Microsoft Teams
* Add Teams webhook to `config.py`

```python
msteams_webhook="XXXXXXXXXXXXXX"
```

## Run Script
```
python monitor.py
```

## Setup Cronjob
Setup a cronjob that runs the script every 5 minutes.(Change script location accordingly)
Edit `/etc/crontab` and add following Line:
```
*/5 * * * * root python /opt/sitemap/monitor.py
```
