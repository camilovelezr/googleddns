# Google Dynamic DNS Updater - Python - Julia
This repo includes scripts in Python and Julia to automatically update a Google Domains domain's DDNS.
Follow instructions [here](https://support.google.com/domains/answer/6147083?hl=en) to set up DDNS for your domain.
These scripts make requests to Google Domains API and update your Dynamic DNS record.

# How to use the scripts
Both scripts achieve the same result: they update the IP to which the host is linked.

`ip.py` runs faster than `ip.jl` (they are both very fast anyway).
## 1. Configuration
Regardless of which script you use, edit `config.json` and include your credentials and hostname.

## 2.a Python Requirements
The only requirement is [Requests](https://docs.python-requests.org/en/latest/). You can install it with `pip install requests` or by running `pip install -r requirements.txt`.

## 2.b Julia Requirements
There is a `Project.toml` file includded. You can use it to activate and instantiate an environment with all requirements.
To do this, you should uncomment some code included in `ip.jl`.
If you prefer to install requirements in your base environment:
```
julia> ]
(v@1.7) pkg> add HTTP URIs JSON Memento
```
## 3.a Run Python Script
Run `python ip.py`
## 3.b Run Julia Script
Run `julia ip.jl`

---
# Logging
`ip.py` will log every call to the API in `gddnspy.log`

`ip.jl` will log every call to the API in `gddnsjl.log`
