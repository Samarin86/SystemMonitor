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
        self.page.run_task(self.update_parameters_two)

    def will_unmount(self):
        self.running = False

    async def update_parameters(self):
        while self.running:
            # print(self.parameter_number)
            if self.parameter_number == 'cell_1':
                self.value = f"{psutil.cpu_percent(interval=1)} %"
                self.update()
            if self.parameter_number == 'cell_2':
                self.value = f"{psutil.cpu_freq().current}"
                self.update()
            if self.parameter_number == 'cell_3':
                self.value = f"{psutil.virtual_memory().total:,}"
                self.update()
            await asyncio.sleep(0.2)

    async def update_parameters_two(self):
        while self.running:
            if self.parameter_number == 'cell_4':
                self.value = f"{psutil.virtual_memory().available:,}"
                self.update()
            if self.parameter_number == 'cell_5':
                self.value = f"{psutil.virtual_memory().used:,}"
                self.update()
            if self.parameter_number == 'cell_6':
                self.value = f"{psutil.virtual_memory().free:,}"
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
            heading_row_height=50,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=70,
            columns=[
                ft.DataColumn(ft.Text("CPU usage")),
                ft.DataColumn(ft.Text("CPU frequency")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T"), numeric=False),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(SystemParameters('cell_1')),
                        ft.DataCell(SystemParameters('cell_2')),
                        ft.DataCell(SystemParameters('cell_3')),
                        ft.DataCell(SystemParameters('cell_4')),
                        ft.DataCell(SystemParameters('cell_5')),
                        ft.DataCell(SystemParameters('cell_6')),
                    ],
                ),
            ],
        ),
    )
# the second table
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
            heading_row_height=50,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=70,
            columns=[
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
                ft.DataColumn(ft.Text("T")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("T")),
                        ft.DataCell(ft.Text("T")),
                        ft.DataCell(ft.Text("T")),
                        ft.DataCell(ft.Text("T")),
                        ft.DataCell(ft.Text("T")),
                        ft.DataCell(ft.Text("T")),
                    ],
                ),
            ],
        ),
    )


ft.app(main)
