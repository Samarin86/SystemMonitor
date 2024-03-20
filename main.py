import asyncio
import flet as ft
import psutil
import time
from psutil._common import bytes2human


class SystemParameters(ft.Text):
    def __init__(self, parameter_number):
        super().__init__()
        self.parameter_number = parameter_number

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_parameters)

    def will_unmount(self):
        self.running = False

    async def update_parameters(self):
        while self.running:
            print(self.parameter_number)
            if self.parameter_number == 1:
                self.value = f"{psutil.cpu_percent(interval=1)} %"
                self.update()
            if self.parameter_number == 2:
                self.value = f"{psutil.cpu_freq().current}"
                self.update()
            if self.parameter_number == 3:
                self.value = f"{psutil.virtual_memory().total}"
                self.update()
            if self.parameter_number == 4:
                self.value = f"{psutil.virtual_memory().available}"
                self.update()
            if self.parameter_number == 5:
                self.value = f"{psutil.virtual_memory().used}"
                self.update()
            if self.parameter_number == 6:
                self.value = f"{psutil.virtual_memory().free}"
                self.update()

            await asyncio.sleep(0.2)


def main(page: ft.Page):
    page.add(
        ft.DataTable(
            width=1700,
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
                ft.DataColumn(ft.Text("CPU usage")),
                ft.DataColumn(ft.Text("CPU frequency")),
                ft.DataColumn(ft.Text("T"), numeric=True),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(SystemParameters(1)),
                        ft.DataCell(SystemParameters(2)),
                        ft.DataCell(SystemParameters(3)),
                        ft.DataCell(SystemParameters(4)),
                        ft.DataCell(SystemParameters(5)),
                        ft.DataCell(SystemParameters(6)),
                    ],
                ),
            ],
        ),
    )


ft.app(main)
