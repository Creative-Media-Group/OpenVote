import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale.TR import tr


platform = toga.platform.current_platform


class OpenVote(toga.App):
    def switchtotab(self, tab):
        self.container.current_tab = tab

    def startup(self):
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
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
                    style=Pack(font_size=50, text_align="center", padding=10),
                ),
                toga.Button(
                    tr(
                        csv_file=self.file,
                        target_key="DISTRICTCOUNCILELECTION",
                        langcode=self.lang,
                    ),
                    on_press=lambda _: self.switchtotab(1),
                    style=Pack(text_align="center", padding=10),
                    icon="openvote",
                ),
            ],
            style=Pack(alignment="center", direction="column", flex=1),
        )
        tab2 = toga.Box(children=[])
        self.container = toga.OptionContainer(
            content=[
                (
                    tr(csv_file=self.file, target_key="HELLO", langcode=self.lang),
                    hometab,
                ),
                (
                    tr(
                        csv_file=self.file,
                        target_key="DISTRICTCOUNCILELECTION",
                        langcode=self.lang,
                    ),
                    tab2,
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
