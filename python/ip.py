import logging
import json
import requests
import os
from pathlib import Path

"""
Set up logging
"""
logging.basicConfig(
    format="%(asctime)s -  %(message)s", datefmt="%d-%b-%y %H:%M:%S",
)
logger = logging.getLogger("googleddns")
fhandler = logging.FileHandler("gddnspy.log")
fformat = logging.Formatter("%(asctime)s -  %(message)s", datefmt="%d-%b-%y %H:%M:%S")
fhandler.setFormatter(fformat)
fhandler.setLevel("INFO")
logger.setLevel("INFO")
logger.addHandler(fhandler)


def config():
    path = Path(os.path.realpath(__file__))
    path = path.parent.parent.joinpath("config.json")
    with open(path, "rb") as f:
        config = json.loads(f.read())
    return config


def main():
    r = requests.get("https://domains.google.com/checkip")
    ip = r.content.decode(r.encoding)
    c = config()
    url = f"https://{c['username']}:{c['password']}@domains.google.com/nic/update"
    rp = requests.post(url, {"hostname": c["hostname"], "myip": ip})
    rp.raise_for_status()
    logger.info(
        "hostname: %s IP: %s response: %s"
        % (c["hostname"], ip, rp.content.decode(rp.encoding))
    )


if __name__ == "__main__":
    main()
