# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Unit of Purchase",
    "version": "1.0",
    "summary": "Purchase secondary unit",
    "depends": [
        "product",
        "purchase",
    ],
    "author": "OdooMRP team",
    "website": "http://www.odoomrp.com",
    "contributors": [
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
        "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
        "Ana Juaristi <ajuaristio@gmail.com>"
    ],
    "category": "Purchase Management",
    "data": [
        "data/product_data.xml",
        "views/product_view.xml",
        "views/purchase_view.xml",
        "views/pricelist_view.xml",
    ],
    "installable": True,
}
