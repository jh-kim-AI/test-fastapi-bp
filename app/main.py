# -*- coding: utf-8 -*-
import uvicorn
from path import Path

from app.common.log import log
from app.core.conf import settings
from app.core.registrar import register_app


app = register_app()

if __name__ == "__main__":
    try:
        # ASCII Art Generator, http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Nebula
        log.info(
            r"""\n
 /$$   /$$           /$$                 /$$            /$$$$$$  /$$$$$$$  /$$$$$$
| $$$ | $$          | $$                | $$           /$$__  $$| $$__  $$|_  $$_/
| $$$$| $$  /$$$$$$ | $$$$$$$  /$$   /$$| $$  /$$$$$$ | $$  \ $$| $$  \ $$  | $$  
| $$ $$ $$ /$$__  $$| $$__  $$| $$  | $$| $$ |____  $$| $$$$$$$$| $$$$$$$/  | $$  
| $$  $$$$| $$$$$$$$| $$  \ $$| $$  | $$| $$  /$$$$$$$| $$__  $$| $$____/   | $$  
| $$\  $$$| $$_____/| $$  | $$| $$  | $$| $$ /$$__  $$| $$  | $$| $$        | $$  
| $$ \  $$|  $$$$$$$| $$$$$$$/|  $$$$$$/| $$|  $$$$$$$| $$  | $$| $$       /$$$$$$
|__/  \__/ \_______/|_______/  \______/ |__/ \_______/|__/  |__/|__/      |______/
            """
        )
        uvicorn.run(
            app=f'{Path(__file__).stem}:app',
            host=settings.UVICORN_HOST,
            port=settings.UVICORN_PORT,
            reload=settings.UVICORN_RELOAD,
        )

    except Exception as e:
        log.error(f'❌ FastAPI start filed: {e}')
