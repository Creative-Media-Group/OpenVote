import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale import tr


platform = toga.platform.current_platform


class OpenVote(toga.App):
    def switchtotab(self, tab):
        self.container.current_tab = tab

    def startup(self):
        self.mypath = self.paths.app.absolute()
        self.file = f"{self.mypath}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        hometab = toga.Box(
            children=[
                toga.Label(
                    "OpenVote",
                    style=Pack(font_size=50, text_align="center", margin=10),
                ),
                toga.Button(
                    tr(
                        csv_file=self.file,
                        target_key="DISTRICTCOUNCILELECTION",
                        langcode=self.lang,
                    ),
                    on_press=lambda _: self.switchtotab(1),
                    style=Pack(text_align="center", margin=10),
                ),
                toga.Button(
                    tr(
                        csv_file=self.file,
                        target_key="FEDERALELECTION",
                        langcode=self.lang,
                    ),
                    on_press=lambda _: self.switchtotab(2),
                    style=Pack(text_align="center", margin=10),
                ),
            ],
            style=Pack(align_items="center", direction="column", flex=1),
        )
        district_tab = toga.Box(children=[])
        federal_tab = toga.Box(children=[])
        self.container = toga.OptionContainer(
            content=[
                toga.OptionItem(
                    tr(csv_file=self.file, target_key="HELLO", langcode=self.lang),
                    hometab,
                    icon=toga.Icon(
                        tr(
                            csv_file=self.file,
                            target_key="HELLO_PATH",
                            langcode=self.lang,
                        ).format(path=self.mypath)
                    ),
                ),
                toga.OptionItem(
                    tr(
                        csv_file=self.file,
                        target_key="DISTRICTCOUNCILELECTION",
                        langcode=self.lang,
                    ),
                    district_tab,
                    icon=toga.Icon(
                        tr(
                            csv_file=self.file,
                            target_key="DISTRICTCOUNCILELECTION_PATH",
                            langcode=self.lang,
                        ).format(path=self.mypath)
                    ),
                ),
                toga.OptionItem(
                    tr(
                        csv_file=self.file,
                        target_key="FEDERALELECTION",
                        langcode=self.lang,
                    ),
                    federal_tab,
                    icon=toga.Icon(
                        tr(
                            csv_file=self.file,
                            target_key="FEDERALELECTION_PATH",
                            langcode=self.lang,
                        ).format(path=self.mypath)
                    ),
                ),
            ]
        )
        self.container.style.direction = "column"
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.container.current_tab = 0
        self.main_window.content = self.container
        self.main_window.show()


def main():
    return OpenVote()
