import logging
import sys
import os
import json
import uvicorn
import psycopg2
from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException, Response
import debugpy

debugpy.listen(("0.0.0.0", 5678))
print("Waiting for client to attach...")
debugpy.wait_for_client()

logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG)

app = FastAPI()
conn = None

@dataclass
class Icon:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    shape: str = ""


icons: dict[str, Icon] = {}

try:
    with open("data/icons.json", encoding="utf8") as file:
        icons_raw = json.load(file)
        for icon_raw in icons_raw:
            icon = Icon(**icon_raw)
            icons[icon.id] = icon
except IOError:
    logging.error('error reading data file!')
except:
    logging.error(f'unknown error loading data {sys.exc_info()[0]}')


@app.get("/")
def read_root() -> Response:
    logging.info('root requested.')
    logging.info(f'environment db_user:{os.environ.get("DB_USER")}')
    return Response("The server is running.")


@app.get("/icons/{icon_id}", response_model=Icon)
def read_item(icon_id: str) -> Icon:
    if icon_id not in icons:
        logging.warning('icon not found')
        raise HTTPException(status_code=404, detail="Icon not found")
    logging.info(f'icon read: {icons[icon_id].name}')
    return icons[icon_id]

# main program
def main() -> None:
    """ starts the server and starts logs """
    uvicorn.run('main:app', host='127.0.0.1', port=8080, log_level='info')
    logging.info("server started!")

try:
    conn = psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT")
    )
except:
    print('DB connection issue...')
    logging.warning('DB connection issues..')
    raise Exception("DB connection issues..")
    with conn.cursor() as cursor:
        cursor.execute('SELECT VERSION()')
        logging.info(cursor.fetchone())
        logging.info("db connected")


if __name__ == '__main__':
    main()