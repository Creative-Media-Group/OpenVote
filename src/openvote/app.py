"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale.TR import tr

platform = toga.platform.current_platform


class OpenVote(toga.App):
    def startup(self):
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
            # self.formal_name = (
            #    tr(csv_file=self.file, target_key="FORMALNAME", langcode=self.lang),
            # )

        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        hometab = toga.Box(
            children=[
                toga.Label(
                    "OpenVote",
                    style=Pack(font_size=50, text_align="center", padding=10),
                ),
            ],
            style=Pack(alignment="center", direction="column", flex=1),
        )
        container = toga.OptionContainer(
            content=[
                (
                    tr(csv_file=self.file, target_key="HELLO", langcode=self.lang),
                    hometab,
                )
            ]
        )
        container.style.direction = "column"
        self.main_window = toga.MainWindow(title=self.formal_name)
        container.current_tab = 0
        self.main_window.content = container
        self.main_window.show()


def main():
    return OpenVote()
