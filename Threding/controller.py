import queue, threading
from datetime import datetime, timedelta
import logging
from multiprocessing.pool import ThreadPool


def _get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    return logger


end = datetime.now()  # 2021-02-18T14:29:50.344240+00:00
start = end - timedelta(days=8)


class Controller:
    def __init__(self, parameters: dict):
        self.execution_date = datetime.fromisoformat(parameters['execution_date'])  # 2021-02-18T14:29:50.344240+00:00
        self.bucket = parameters['bucket']
        self.logger = _get_logger(__name__)

    def run_service(self, task: str) -> None:
        if task == 'run_task':
            self._run_task()

    def _run_task(self):
        self.logger.info('THIS IS RUNNING IN A POOL THREAD')


class App:
    def __init__(self, controller: str, task: str, task_parameters: dict):
        self.task = task
        controller = App.__controller_dispach(controller)
        self.controller = controller(task_parameters)

    @staticmethod
    def __controller_dispach(controller: str):
        return {
            'controller': Controller
        }.get(controller)

    def run(self) -> None:
        self.controller.run_service(self.task)


class Migration:
    def __init__(self, migration_from: str, migration_to: str):
        self.queue = queue.Queue(maxsize=5)
        self.migration_from = datetime.fromisoformat(migration_from)
        self.migration_to = datetime.fromisoformat(migration_to)

    def daterange(self, from_date, to_date):
        for n in range(int((to_date - from_date).days)):
            yield from_date + timedelta(n)

    def run(self):
        runs = []
        for date in self.daterange(self.migration_from, self.migration_to):
            parameters = {
                'execution_date': date.isoformat(),  # Epoch Timestamp
                'bucket': f'mng-datahub-dev',
            }
            runs.append(parameters)


if __name__ == '__main__':
    Migration(migration_from=start.isoformat(),
              migration_to=end.isoformat()).run()
