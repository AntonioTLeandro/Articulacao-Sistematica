# -*- coding: utf-8 -*-
"""
/***************************************************************************
 articulacaosistematica
                                 A QGIS plugin
 Gloria vai passar o material
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-03-11
        copyright            : (C) 2022 by Antonio Teles
        email                : antoniot.leandro@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load articulacaosistematica class from file articulacaosistematica.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .articulacaosistematica import articulacaosistematica
    return articulacaosistematica(iface)
