import sys

from PySide6.QtWidgets import QApplication

from component_library.component_item_view import ComponentItemView

temp = [
    {
      "author": "FreeCAD@gmail.com",
      "created_at": "2023-06-13T15:55:03",
      "description": None,
      "id": "fac97ccd-dc22-4415-986c-cc0684a7c286",
      "license_id": "b89cd636-1d7c-446f-85a5-eb4de75534d5",
      "maintainer": "FreeCAD@gmail.com",
      "name": "photoresistor",
      "rating": 5,
      "thumbnail": "https://raw.githubusercontent.com/FreeCAD/FreeCAD-library/master/Electronics%20Parts/Photoresistor/Photoresistor.jpeg",
      "updated_at": "2023-06-13T15:55:03",
      "version": "1"
    },
    {
      "author": "FreeCAD@gmail.com",
      "created_at": "2023-06-13T15:55:03",
      "description": None,
      "id": "fac97ccd-dc22-4415-986c-cc0684a7c286",
      "license_id": "b89cd636-1d7c-446f-85a5-eb4de75534d5",
      "maintainer": "FreeCAD@gmail.com",
      "name": "photoresistor2",
      "rating": 5,
      "thumbnail": "https://i.stack.imgur.com/jwicy.png",
      "updated_at": "2023-06-13T15:55:03",
      "version": "1"
    },
    {
      "author": "FreeCAD@gmail.com",
      "created_at": "2023-06-13T15:55:03",
      "description": None,
      "id": "fac97ccd-dc22-4415-986c-cc0684a7c286",
      "license_id": "b89cd636-1d7c-446f-85a5-eb4de75534d5",
      "maintainer": "FreeCAD@gmail.com",
      "name": "photoresistor3",
      "rating": 5,
      "thumbnail": "https://cdn.sstatic.net/Img/teams/teams-illo-free-sidebar-promo.svg?v=47faa659a05e",
      "updated_at": "2023-06-13T15:55:03",
      "version": "1"
    },
    {
      "author": "FreeCAD@gmail.com",
      "created_at": "2023-06-13T15:55:03",
      "description": None,
      "id": "fac97ccd-dc22-4415-986c-cc0684a7c286",
      "license_id": "b89cd636-1d7c-446f-85a5-eb4de75534d5",
      "maintainer": "FreeCAD@gmail.com",
      "name": "photoresistor4",
      "rating": 5,
      "thumbnail": "https://i.stack.imgur.com/Bzi9K.png",
      "updated_at": "2023-06-13T15:55:03",
      "version": "1"
    }
]

app = QApplication(sys.argv)
window = ComponentItemView(temp)
sys.exit(app.exec())
