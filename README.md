# Telegram Site Monitor Bot

A simple Python script that checks availabilty of multiple sites and sends error alerts to Telegram.

### Create new Telegram Bot
* Create a new Telegram Bot: https://core.telegram.org/bots#6-botfather
* Create a new Telegram group in the Telegram App and add the newly created bot
* Optionally: Grant your bot group admin permissions

### Get ChatID

* Open in Browser (Replace {TOKEN} in URL with your Token): https://api.telegram.org/bot{TOKEN}/getUpdates
* Copy Chat ID

**Example:**
```json
chat: {
  id: XXXXXXXXX,
  title: "my_group_name",
  type: "group",
}
```

### Configuration
* Copy `config_sample.py` to `config.py` and edit `token` and `chat_id`.
* Add the URLs of sites to be monitored in `config.py`

**Example:**
```python
token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
chat_id = 'XXXXXXXXX'
sites = ["https://www.google.com", "https://www.github.com"]
```

### Run Script
```
python monitor.py
```

### Setup a Cronjob
Setup a cronjob that runs the script every minute.(Change script location accordingly)
Edit `/etc/crontab` and add following Line:
```
* * * * * root python /opt/telegram-site-monitor-bot/monitor.py
```





