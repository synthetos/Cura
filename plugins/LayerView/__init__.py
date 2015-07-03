# Copyright (c) 2015 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.

from . import LayerView, LayerViewProxy
from PyQt5.QtQml import qmlRegisterType, qmlRegisterSingletonType

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "type": "view",
        "plugin": {
            "name": "Layer View",
            "author": "Ultimaker",
            "version": "1.0",
            "description": catalog.i18nc("Layer View plugin description", "Provides the Layer view.")
        },
        "view": {
            "name": catalog.i18nc("Layers View mode", "Layers"),
            "view_panel": "LayerView.qml"
        }
    }

def createLayerViewProxy(engine, script_engine):
    return LayerViewProxy.LayerViewProxy()

def register(app):
    layer_view = LayerView.LayerView()
    qmlRegisterSingletonType(LayerViewProxy.LayerViewProxy, "UM", 1, 0, "LayerView", layer_view.getProxy)
    return { "view": LayerView.LayerView() }
