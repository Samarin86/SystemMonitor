import asyncio
import flet as ft
import psutil
from psutil._common import bytes2human


class SystemParameters(ft.Text):
    def __init__(self, parameter_number):
        super().__init__()
        self.parameter_number = parameter_number

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_parameters)
        self.page.run_task(self.update_parameters_second_table)
        self.page.run_task(self.update_parameters_thirty_table)
        self.page.run_task(self.update_parameters_fourth_table)

    def will_unmount(self):
        self.running = False

    async def update_parameters(self):
        while self.running:
            if self.parameter_number == 'cell_1':
                self.value = f"{psutil.cpu_percent(interval=1)} %"
                self.update()
            if self.parameter_number == 'cell_2':
                self.value = f"{psutil.cpu_freq().current}"
                self.update()
            if self.parameter_number == 'cell_3':
                self.value = f"{psutil.cpu_count(logical=False)}"
                self.update()
            if self.parameter_number == 'cell_4':
                self.value = f"{psutil.cpu_count()}"
                self.update()
            if self.parameter_number == 'cell_5':
                self.value = f"{[x / psutil.cpu_count() * 100 for x in psutil.getloadavg()][0]:.2f}"
                self.update()
            if self.parameter_number == 'cell_6':
                self.value = f"{psutil.cpu_times_percent(interval=None, percpu=False)[0]}"
                self.update()
            await asyncio.sleep(0.2)

    async def update_parameters_second_table(self):
        while self.running:
            if self.parameter_number == 'cell_cpu_core':
                self.value = f"{psutil.cpu_percent(interval=1, percpu=True)} %"
                self.update()
            await asyncio.sleep(0.2)

    async def update_parameters_thirty_table(self):
        while self.running:
            # print(self.parameter_number)
            if self.parameter_number == 'cell_7':
                self.value = f"{psutil.virtual_memory().total:,}"
                self.update()
            if self.parameter_number == 'cell_8':
                self.value = f"{psutil.virtual_memory().available:,}"
                self.update()
            if self.parameter_number == 'cell_9':
                self.value = f"{psutil.virtual_memory().used:,}"
                self.update()
            if self.parameter_number == 'cell_10':
                self.value = f"{psutil.virtual_memory().free:,}"
                self.update()
            if self.parameter_number == 'cell_11':
                self.value = f"{psutil.swap_memory().total:,}"
                self.update()
            if self.parameter_number == 'cell_12':
                self.value = f"{psutil.swap_memory().used:,}"
                self.update()
            await asyncio.sleep(0.4)

    async def update_parameters_fourth_table(self):
        while self.running:
            print(self.parameter_number)
            if self.parameter_number == 'cell_13':
                self.value = f"{psutil.cpu_stats()[0]}"
                self.update()
            if self.parameter_number == 'cell_14':
                self.value = f"{psutil.cpu_stats()[1]}"
                self.update()
            if self.parameter_number == 'cell_15':
                self.value = f"{psutil.cpu_stats()[2]}"
                self.update()
            if self.parameter_number == 'cell_16':
                self.value = f"{psutil.cpu_stats()[3]}"
                self.update()
            if self.parameter_number == 'cell_17':
                self.value = f"{psutil.disk_io_counters(perdisk=False, nowrap=True).read_count}"
                self.update()
            if self.parameter_number == 'cell_18':
                self.value = f"{psutil.disk_io_counters(perdisk=False, nowrap=True).read_bytes}"
                self.update()
            await asyncio.sleep(0.2)


def main(page: ft.Page):
    page.add(
        ft.DataTable(
            width=1700,
            bgcolor="brown",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(2, "orange"),
            horizontal_lines=ft.border.BorderSide(1, "orange"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_color={"hovered": "0x30FF0000"},
            data_row_max_height=100,
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=20,
            columns=[
                ft.DataColumn(ft.Text("CPU usage")),
                ft.DataColumn(ft.Text("CPU frequency")),
                ft.DataColumn(ft.Text("CPU cores")),
                ft.DataColumn(ft.Text("CPU threads")),
                ft.DataColumn(ft.Text("Average system \nload in 5 minutes")),
                ft.DataColumn(ft.Text("User mode \noperation time"), numeric=False),
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
    # the second table "Streaming downloads"
    page.add(
        ft.DataTable(
            width=1700,
            bgcolor="brown",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(2, "orange"),
            horizontal_lines=ft.border.BorderSide(1, "orange"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=70,
            columns=[
                ft.DataColumn(ft.Text("Streaming downloads")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(SystemParameters('cell_cpu_core')),
                    ],
                ),
            ],
        ),
    )
    # thirty table "RAM"
    page.add(
        ft.DataTable(
            width=1700,
            bgcolor="brown",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(2, "orange"),
            horizontal_lines=ft.border.BorderSide(1, "orange"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=70,
            columns=[
                ft.DataColumn(ft.Text("Total RAM")),
                ft.DataColumn(ft.Text("Available RAM")),
                ft.DataColumn(ft.Text("Used RAM")),
                ft.DataColumn(ft.Text("Free RAM")),
                ft.DataColumn(ft.Text("Shared Swap memory")),
                ft.DataColumn(ft.Text("Swap memory used")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(SystemParameters('cell_7')),
                        ft.DataCell(SystemParameters('cell_8')),
                        ft.DataCell(SystemParameters('cell_9')),
                        ft.DataCell(SystemParameters('cell_10')),
                        ft.DataCell(SystemParameters('cell_11')),
                        ft.DataCell(SystemParameters('cell_12')),
                    ],
                ),
            ],
        ),
    )
    # fourth table "sensors"
    page.add(
        ft.DataTable(
            width=1700,
            bgcolor="brown",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(2, "orange"),
            horizontal_lines=ft.border.BorderSide(1, "orange"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=70,
            columns=[
                ft.DataColumn(ft.Text("Number of context switches")),
                ft.DataColumn(ft.Text("Number of interrupts")),
                ft.DataColumn(ft.Text("Number of software \ninterrupts")),
                ft.DataColumn(ft.Text("Number of system calls")),
                ft.DataColumn(ft.Text("Number of reads")),
                ft.DataColumn(ft.Text("Number of bytes read")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(SystemParameters('cell_13')),
                        ft.DataCell(SystemParameters('cell_14')),
                        ft.DataCell(SystemParameters('cell_15')),
                        ft.DataCell(SystemParameters('cell_16')),
                        ft.DataCell(SystemParameters('cell_17')),
                        ft.DataCell(SystemParameters('cell_18')),
                    ],
                ),
            ],
        ),
    )


ft.app(main)
