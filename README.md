# 📡 Wireless Tool

Wireless Tool for ITC

*Mission*: To provide the Dartmouth community (students, faculty, and staff) with a tool to report WiFi problems.

## Designs
*TBD*

## Architecture
### Tech Stack 🥞
• Python 3.7\
• Gunicorn - server\
• Falcon - framework\
• PostgreSQL - database

#### Packages 📦
*TBD*

### Style
*TBD*

### Data Models
*TBD*

### File Structure

```
├──[wireless-tool]/ # root directory
    ├── README.md
    ├── server
    │   ├── components
    │   ├── config
    │   └── index.py # the root file of the server
    ├── bin # virtual environment        
    ├── include
    └── lib
```

For more detailed documentation on our file structure and specific functions in the code, feel free to check the project files themselves.

## Setup Steps 
1. Clone the dev branch by running `git clone https://github.com/dali-lab/wireless-tool.git --branch dev` in your terminal
2. Move into the root folder by running `cd wireless-tool`
3. Install everything by running `virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`
4. Move into the main folder by running `cd server`
5. Start the server by running `gunicorn --reload index:api`

## Deployment 🚀
*TBD*

## Authors
* Dan Clipca '23, developer
* Jai Smith '22, developer
* Benedict Tedjokusumo '23, developer
* Archita Harathi '22, designer
* Bryan Manzi '21, designer
* Grace Qu '22, designer
* Sophie Wang '22, PM

## Acknowledgments 🤝
*Thank you to our partner, Felix Windt, and the rest of the ITC team!*

---
Designed and developed by [@DALI Lab](https://github.com/dali-lab)

