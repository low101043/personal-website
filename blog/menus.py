from menu import Menu, MenuItem

Menu.add_item("main", MenuItem('Home', "/", weight=10))
Menu.add_item("main", MenuItem("CV", "/cv/", weight=20))
Menu.add_item("main", MenuItem("Blog", "/blog/", weight=30))
Menu.add_item("main", MenuItem("About Me", "/about/", weight=40))