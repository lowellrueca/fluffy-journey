from starlite.app import Starlite as App
from starlite.router import Router
from starlite.types import ControllerRouterHandler
from typing import List


def startup():
    from service.events import on_startup, on_shutdown
    from service.controllers import SteelController

    on_startup = [on_startup]
    on_shutdown = [on_shutdown]
    route_handlers: List[ControllerRouterHandler] = [
        Router(path="/api/products", route_handlers=[SteelController])
    ]

    app: App = App(
        route_handlers=route_handlers, 
        on_startup=on_startup, 
        on_shutdown=on_shutdown
    )

    return app
