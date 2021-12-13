# python -m aimremote.cli up --security-token Passtoken12345 --port 4902 & 
# pip uninstall aim-remote -y && pip install . && python ./example/simple.py
# aim-remote up --security-token Passtoken12345 --port 4902
# visit localhost:4902/docs

from aimremote import Run, Distribution
from torch import tensor

my_run = Run(
    repo='/home/administrator/tools',
    experiment='experiment_234????',
    run_hash='fru_1234567',
    security_token = 'Passtoken12345',
    url = 'http://localhost:4902'
)

my_run['hparams'] = {'batch_size': 43}

print(my_run['hparams'])

for step in range(10):
    value = step * 11
    my_run.track(
        value,       # Current value to track
        name='loss', # The metric name
        step=step,   # Step index (optional)
        epoch=0,     # Epoch (optional)
        context={    # Metric context (optional)
            'subset': 'test',
            'test': 'fru'
        },
    )

for step in range(10):
    n = step / 10.
    my_run.track(
        Distribution(tensor([[n, -n], [n, n]])),
        name='gradients', # The name of distributions
        step=step,   # Step index (optional)
        epoch=0,     # Epoch (optional)
        context={    # Context (optional)
            'type': 'weights',
        }
    )
