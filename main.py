import flet as ft
import parameters


def main(page: ft.Page):
    """
    A function that adds multiple DataTables to a page, each displaying different system monitoring metrics.
    """
    # the first table "CPU"
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    page.title = "System monitor"
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
                ft.DataColumn(
                    ft.Text("User mode \noperation time"), numeric=False),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(parameters.SystemParameters('cell_1')),
                        ft.DataCell(parameters.SystemParameters('cell_2')),
                        ft.DataCell(parameters.SystemParameters('cell_3')),
                        ft.DataCell(parameters.SystemParameters('cell_4')),
                        ft.DataCell(parameters.SystemParameters('cell_5')),
                        ft.DataCell(parameters.SystemParameters('cell_6')),
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
                        ft.DataCell(
                            parameters.SystemParameters('cell_cpu_core')),
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
                        ft.DataCell(parameters.SystemParameters('cell_7')),
                        ft.DataCell(parameters.SystemParameters('cell_8')),
                        ft.DataCell(parameters.SystemParameters('cell_9')),
                        ft.DataCell(parameters.SystemParameters('cell_10')),
                        ft.DataCell(parameters.SystemParameters('cell_11')),
                        ft.DataCell(parameters.SystemParameters('cell_12')),
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
                        ft.DataCell(parameters.SystemParameters('cell_13')),
                        ft.DataCell(parameters.SystemParameters('cell_14')),
                        ft.DataCell(parameters.SystemParameters('cell_15')),
                        ft.DataCell(parameters.SystemParameters('cell_16')),
                        ft.DataCell(parameters.SystemParameters('cell_17')),
                        ft.DataCell(parameters.SystemParameters('cell_18')),
                    ],
                ),
            ],
        ),
    )


if __name__ == "__main__":
    ft.app(main)
