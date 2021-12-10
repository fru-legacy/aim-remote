from aim import Run

class Run:
    def test(self):
        my_run = Run(
            repo='/home/administrator/tools',
            experiment='experiment_fru2',
            run_hash='testhash3',
            system_tracking_interval = None
        )
        print("test")