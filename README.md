# aim-remote

> :warning: **This is a proof of concept**: You probably dont want to use this project without reading the code

```shell
pip3 install git+https://github.com/fru/aim-remote
```

Facade to access aim from a remote server. Start aim as usual and also:

```shell
aim-remote up --security-token Passtoken12345
```

Now you can replace the aim package with aimremote. Add the security_token and url to the Run() call.

```python
from aimremote import Run, Distribution
from torch import tensor

my_run = Run(
    repo='/home/administrator/tools',
    experiment='experiment_fru12345',
    run_hash='fru123456',
    security_token = 'Passtoken12345',
    url = 'http://localhost:4900'
)

my_run['hparams'] = {'batch_size': 43}
print(my_run['hparams'])

for step in range(10):
    value = step * 10
    my_run.track(
        value,
        name='loss',
        step=step,
        epoch=0,
        context={
            'subset': 'test'
        },
    )

for step in range(10):
    n = step / 10.
    my_run.track(
        Distribution(tensor([[n, -n], [n, n]])),
        name='gradients',
        step=step,
        epoch=0
    )
```
