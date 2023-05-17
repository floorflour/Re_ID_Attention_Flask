import time
from multiprocessing import Process
from typing import List, Tuple
from api import logger

# 从输入


class RecvImageProcess(Process):
    def __init__(self, db, relay_queue, processing_functions: List[Tuple[str, callable]]):
        super().__init__()
        self.db = db
        self.relay_queue = relay_queue
        self.processing_functions = processing_functions

    def run(self):
        while True:
            image_path = self.queue.get()
            input_time = time.time()
            self.db.store_image_path(image_path, input_time)
            success = False
            for func_name, func in self.processing_functions:
                try:
                    processed_image = func(image_path)
                    self.relay_queue.put(processed_image)
                    success = True
                    self.db.record_success(image_path, func_name)
                    break
                except Exception as e:
                    # Log the error message
                    self.db.record_failure(image_path, func_name, str(e))
            if not success:
                self.db.record_failure(
                    image_path, "all_strategies", "All processing strategies failed.")
                # Raise an exception or perform some other error handling


class ProcessingStrategies():
    @staticmethod
    def strategy_1(image_path: str) -> None:
        # logic to process image using strategy 1
        pass

    @staticmethod
    def strategy_2(image_path: str) -> None:
        # logic to process image using strategy 2
        pass

    @staticmethod
    def strategy_3(image_path: str) -> None:
        # logic to process image using strategy 3
        pass

    @staticmethod
    def strategy_4(image_path: str) -> None:
        # logic to process image using strategy 4
        pass

    @staticmethod
    def strategy_5(image_path: str) -> None:
        # logic to process image using strategy 5
        pass

    @staticmethod
    def register_strategies(recv_process: RecvImageProcess) -> None:
        recv_process.processing_functions.append(
            ("strategy_1", ProcessingStrategies.strategy_1))
        recv_process.processing_functions.append(
            ("strategy_2", ProcessingStrategies.strategy_2))
        recv_process.processing_functions.append(
            ("strategy_3", ProcessingStrategies.strategy_3))
        recv_process.processing_functions.append(
            ("strategy_4", ProcessingStrategies.strategy_4))
        recv_process.processing_functions.append(
            ("strategy_5", ProcessingStrategies.strategy_5))
