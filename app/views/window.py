import dearpygui.dearpygui as dpg
from app.utils.drive_link import convert_drive_link
from app.helpers.popups import show_error_popup, show_info_popup


class window:
    def __init__(self):
        self.input_id = None
        self.converted_link_id = None
        self.copy_button_id = None
        self.theme_id = None

    def init(self):
        self.setupWindow()
        with dpg.window(label="Conversor de enlaces de Google Drive", width=700, height=420, pos=(30, 30)):
            self.setupMenu()
        self.launchWindow()

    def setupWindow(self):
        dpg.create_context()
        dpg.create_viewport(title="Conversor de enlaces de Google Drive", width=780, height=520)
        dpg.setup_dearpygui()
        self.apply_theme()

    def launchWindow(self):
        dpg.show_viewport()
        dpg.start_dearpygui()

    def setupMenu(self):
        dpg.add_spacer(height=10)
        dpg.add_text("Conversor de enlaces de Google Drive", color=(0, 120, 220), bullet=True)
        dpg.add_spacer(height=5)
        with dpg.group(horizontal=True):
            dpg.add_text("Instrucciones:", color=(120, 120, 120))
        dpg.add_text("1. Sube el archivo a Google Drive.", indent=10)
        dpg.add_text("2. En la opción de compartir, selecciona 'Cualquiera con el enlace'.", indent=10)
        dpg.add_text("3. Copia el enlace y pégalo aquí abajo.", indent=10)
        dpg.add_spacer(height=10)
        self.input_id = dpg.add_input_text(
            label="Enlace de Google Drive",
            hint="Pega el enlace aquí",
            width=500,
            on_enter=True,
            callback=self.convertButtonHelper
        )
        dpg.add_spacer(height=5)
        dpg.add_button(label="Convertir enlace", callback=self.convertButtonHelper, width=180)
        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_spacer(height=10)
        dpg.add_text("Enlace convertido:", color=(0, 120, 0))
        self.converted_link_id = dpg.add_input_text(
            label="",
            default_value="",
            width=500,
            readonly=True,
            callback=self.copy_to_clipboard
        )
        self.copy_button_id = dpg.add_button(label="Copiar al portapapeles", callback=self.copy_to_clipboard, user_data=None, width=180)
        dpg.add_text("Haz click en el campo o en el botón para copiar el enlace.", color=(120,120,120), indent=10)
        dpg.add_spacer(height=10)

    def convertButtonHelper(self, sender=None, app_data=None, user_data=None):
        try:
            link = dpg.get_value(self.input_id)
            if not link or not isinstance(link, str):
                show_error_popup("Por favor, ingresa un enlace válido.")
                dpg.set_value(self.converted_link_id, "")
                return
            converted_link = convert_drive_link(link)
            dpg.set_value(self.converted_link_id, converted_link)
            show_info_popup("Enlace convertido correctamente. Haz click para copiar.")
        except Exception as e:
            dpg.set_value(self.converted_link_id, "")
            show_error_popup(str(e))

    def copy_to_clipboard(self, sender, app_data=None, user_data=None):
        value = dpg.get_value(self.converted_link_id)
        if value:
            dpg.set_clipboard_text(value)
            show_info_popup("¡Enlace copiado al portapapeles!")
        else:
            show_error_popup("No hay enlace para copiar.")

    def apply_theme(self):
        # Tema simple y moderno
        with dpg.theme() as self.theme_id:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (245, 247, 250), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (0, 120, 220), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (0, 150, 255), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 120, 220), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 150, 255), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 90, 180), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, (30, 30, 30), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (230, 240, 255), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (200, 220, 255), category=dpg.mvThemeCat_Core)
        dpg.bind_theme(self.theme_id)
