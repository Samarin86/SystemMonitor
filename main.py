import asyncio
import flet as ft
import psutil
import time
from psutil._common import bytes2human


class Counting(ft.Text):
    def __init__(self, cpu_percent):
        super().__init__()
        self.cpu_percent = cpu_percent

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_cpu_loading)

    def will_unmount(self):
        self.running = False

    async def update_cpu_loading(self):
        while self.cpu_percent:
            cpu_load = psutil.cpu_percent(interval=1)
            self.value = f"{cpu_load} %"
            self.update()
            await asyncio.sleep(0.2)


gen_cpu = psutil.cpu_percent(interval=1)
def main(page: ft.Page):
    # page.add(Counting(gen_cpu))

    page.add(
        ft.DataTable(
            width=700,
            bgcolor="brown",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "blue"),
            horizontal_lines=ft.border.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=[
                ft.DataColumn(ft.Text("CPU")),
                ft.DataColumn(ft.Text("Second")),
                ft.DataColumn(ft.Text("Diff"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(Counting(gen_cpu)),
                        ft.DataCell(ft.Text("Test")),
                        ft.DataCell(ft.Text("Test")),
                    ],
                ),
            ],
        ),
    )

ft.app(main)
