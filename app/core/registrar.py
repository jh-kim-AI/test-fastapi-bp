# -*- coding: utf-8 -*-
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.conf import settings


@asynccontextmanager
async def register_init(app: FastAPI):
    """
    Register init

    :return:
    """
    # await create_db()
    # await create_table()
    # await create_index()

    try:
        yield

    finally:
    # await drop_index()
    # await drop_table()
    # await drop_db()

        pass

def register_app():
    app = FastAPI(
        title='Nebula',
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
    )

    return app
