from aim import Run as AimRun

class Run:
    def test(self):
        my_run = AimRun(
            repo='/home/administrator/tools',
            experiment='experiment_fru2',
            run_hash='testhash3',
            system_tracking_interval = None
        )
        print("test")