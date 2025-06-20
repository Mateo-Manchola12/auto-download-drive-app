import dearpygui.dearpygui as dpg

def show_error_popup(message: str):
    with dpg.window(label="Error", modal=True, no_close=False, width=350, height=120) as popup_id:
        dpg.add_text(message)
        dpg.add_button(label="Cerrar", callback=lambda: dpg.delete_item(popup_id))


def show_info_popup(message: str):
    with dpg.window(label="Información", modal=True, no_close=False, width=350, height=120) as popup_id:
        dpg.add_text(message)
        dpg.add_button(label="Cerrar", callback=lambda: dpg.delete_item(popup_id))
