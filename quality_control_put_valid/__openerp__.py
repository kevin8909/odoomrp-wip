# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Advanced Open Source Consulting
#    Copyright (C) 2011 - 2014 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Quality Control Manual Validation",
    "version": "1.0",
    "depends": [
        "quality_control",
        "quality_control_ext",
    ],
    "author": "AvanzOSC",
    "category": "Custom Modules",
    "description": """
Este módulo introduce un campo chek nuevo, llamado VÁLIDO. Si el test ha tenido
éxito, el nuevo campo VALIDO será True, pero si el test no ha sido válido, el
usuario tendrá la opción de marcar este nuevo campo como valido.
    """,
    'data': [
        'views/qc_test_ext_view.xml',
    ],
    'installable': True,
}