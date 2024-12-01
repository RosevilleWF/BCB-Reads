from typing import List, Callable


class Menu:

    # Any variable declared in __init__ can be referenced with self.*
    def __init__(self,
                 display_name: str,
                 message: str | None,
                 action: Callable = None,
                 child_menus=None,  # Array of menus please,
                 ):
        self.display_name = display_name
        self.message = message
        self.children = child_menus
        self.action = action

    def show_name(self):
        print(self.display_name)

    # When we select this menu, what does it do? Shows message, then does action
    def select_action(self):
        if self.action is not None:
            self.action()
        self.menu_loop()

    # Wait for input and act upon it
    def menu_loop(self) -> None:

        # NO KIDS? GET OUDDA HERE
        if self.children is None:
            return

        select_index: int = -1

        while select_index == -1:
            for index, menu in enumerate(self.children):
                print(f"{index}: {menu.display_name}")

            user_input = input(self.message)

            # If this is a number see if it's an index number for our menu
            if user_input.isdigit():
                if len(self.children) > int(user_input) >= 0:
                    select_index = int(user_input)
            else:
                selected_children: List[Menu] = []
                for menu in self.children:
                    if user_input in menu.display_name:
                        selected_children.append(menu)

                # If more than one option matches, GTFO
                if len(selected_children) > 1:
                    for index, menu in enumerate(selected_children):
                        print(f"{index} {menu.display_name}")
                    continue

                # This matches with an option, select it!
                if len(selected_children) == 1:
                    select_index = 0

        if select_index is not None:
            print(f"You selected \'{self.children[select_index].display_name}\'")

        menu = self.children[select_index]
        menu.select_action()
