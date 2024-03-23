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
        self.page.run_task(self.update_parameters_first_table)
        self.page.run_task(self.update_parameters_second_table)
        self.page.run_task(self.update_parameters_thirty_table)
        self.page.run_task(self.update_parameters_fourth_table)

    def will_unmount(self):
        self.running = False

    async def update_parameters_first_table(self):
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
            await asyncio.sleep(0.5)

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
            await asyncio.sleep(0.5)
