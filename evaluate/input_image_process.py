import random
import time
from multiprocessing import Process
from api import logger

# 随机选取图片并输入


class SendImageProcess(Process):
    def __init__(self, queue, image_dir):
        super().__init__()
        self.queue = queue
        self.image_dir = image_dir
        logger.info(f"随机照片输入线程：已经启动")

    def run(self):
        while True:
            if self.queue.qsize() <= 10:
                image_path = self.select_random_image()
                self.queue.put(image_path)
                logger.info(f"随机照片输入线程：图像 {image_path} 被添加到了输入图像队列中")
            else:
                logger.info(f"随机照片输入线程：输入图像队列满，添加失败")
            time.sleep(random.randint(10, 30))

    def select_random_image(self):
        image_list = []
        selected_image = random.choice(image_list)
        return selected_image
