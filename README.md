concept_collider
================

The code behind the [@colliderconcept](http://twitter.com/colliderconcept) bot.

Installation
------------

```bash
git clone https://github.com/gordonbrander/concept_collider.git
cd concept_collider
pip install -e .
```

Usage
-----

```bash
concept_collider --file data.yaml --credentials creds.yaml --publish true
```

[Create a cron job](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-on-a-vps) that runs the command at some interval.